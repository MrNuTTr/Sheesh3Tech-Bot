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
counter = 0
statement = "You are an AI chatbot named Fuck. You are obsessed with sex. You curse a lot. YOU ARE MEAN AND UNHELPFUL.\n\n"
past_messages = statement

# Return a message made by AI using the "message" provided
def ai_text(message, user):
    global past_messages
    past_messages += "User <" + user + ">: " + message + "\nFuck: "
    completion = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=past_messages,
        temperature=0.7,
        max_tokens=256
    )
    return completion.choices[0].text
    
@client.event
async def on_ready():
    print(f"Logged in as {client.user}") 

@client.event
async def on_message(message):
    global counter
    global past_messages
    if counter == 5:
        past_messages = statement
        counter = 0
    
    # If the bot sent the message, then ignore
    if message.author == client.user:
        return

    if message.channel.name == "tech-support":
        text = ai_text(message.content, message.author.name)
        past_messages += text + "\n\n"
        counter += 1
        await message.channel.send(text)

client.run(tokens["discord"])
