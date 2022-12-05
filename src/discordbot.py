import discord
from discord.ext import commands
import openai
import json

# Load the file containing needed tokens
token_file = open("tokens.json")
# Parse the json into a python object
tokens = json.load(token_file)
# Close the file
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

    if message.channel.id == 956535878057066587:
        text = ai_text(message.content)
        await message.channel.send(text)

client.run(tokens["discord"])