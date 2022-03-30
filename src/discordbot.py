import discord
import random
import syncro
import json
from messages import rand_stuffs
import messages

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
    # If the bot sent the message, then ignore
    if message.author == client.user:
        return

    if message.content == "hlp tickets" or message.content == "hlp ticket":
        syncro.get_ticket_number()

    index = random.randint(0, len(rand_stuffs)-1)

    await message.channel.send(rand_stuffs[index])

    # If the content of the message is a key in the message dictionary
    #if message.content in messages.message_dict:
        # Then send a message that matches the key
    #    await message.channel.send(messages.message_dict[message.content])
        # Print output to the console
    #    print("Sent message in " + message.channel.name + ":" + 
    #            messages.message_dict[message.content])

client.run(tokens["discord"])