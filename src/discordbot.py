import discord
from discord.ext import commands
import openai
import json

token_file = open("tokens.json")
tokens = json.load(token_file)
token_file.close()

# Discord intents settings
intents = discord.Intents(messages=True, guilds=True, presences=True)

# Global client variable to access discord
client = commands.Bot(command_prefix="<", intents=intents)

# Set the API Key for OpenAI GPT-3
openai.api_key = tokens["openai"]

# Return a message made by AI using the "message" provided
def ai_text(message):
    text = "Human: " + message + "\nAI: "
    completion = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=text,
        temperature=0.7,
        max_tokens=128
    )
    return completion.choices[0].text
    
@client.event
async def on_ready():
    print(f"Logged in as {client.user}") 

@client.event
async def on_message(message):
    # If the bot sent the message, then ignore
    if message.author == client.user:
        return

    if message.channel.id == "tech-support":
        text = ai_text(message.content)
        await message.channel.send(text)

client.run(tokens["discord"])
#testing