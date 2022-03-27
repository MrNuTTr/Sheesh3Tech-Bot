import discord
import json

# Load the file containing needed tokens
token_file = open("tokens.json")

# Parse the json into a python object
tokens = json.load(token_file)

# Close the file
token_file.close()

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}") 

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "hlp Hi" or message.content == "hlp hi":
        await message.channel.send("Hello! Thank you for contacting C3 Tech! A tech will be able to assist you shortly!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "hlp remote" or message.content == "hlp Remote":
        await message.channel.send("Hi! Please go to help.myc3.tech and a tech will give you were code when you are at the screen that says 'please join with a code!'")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "hlp pam" or message.content == "hlp Pam":
        await message.channel.send("PIss off")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "hlp ur mum" or message.content == "hlp your mom" or message.content == "ur mom":
        await message.channel.send("My Mom? I think you mean your mom cause I did her last night and im a bot.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "hlp suicide" or message.content == "hlp Suicide":
        await message.channel.send("Suicide isnt the answer unless youre in IT because then its the right thing to do.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "hlp Bruh" or message.content == "hlp bruh":
        await message.channel.send("Bruh why am I supposed to help you huh?")


client.run(tokens["discord"])