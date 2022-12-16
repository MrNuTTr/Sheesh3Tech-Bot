from os import environ as env
import discord
from discord.ext import commands
import openai

# API Keys
discord_key = env["DISCORD_API_KEY"]
openai_key = env["OPENAI_API_KEY"]

# Discord intents settings
intents = discord.Intents(messages=True, guilds=True, presences=True)

# Global client variable to access discord
client = commands.Bot(command_prefix="<", intents=intents)

# Set the API Key for OpenAI GPT-3
openai.api_key = openai_key
counter = 0
statement = "You are an AI chatbot named Fuck. You curse a lot. YOU ARE MEAN AND UNHELPFUL.\n\n"
past_messages = statement

# Return a message made by AI using the "message" provided
def ai_text(message, user):
    global past_messages
    past_messages += "User <" + user + ">: " + message + "\nFuck: "
    completion = openai.Completion.create(
        engine="text-curie-001", 
        prompt=past_messages,
        temperature=0.9,
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

client.run(discord_key)