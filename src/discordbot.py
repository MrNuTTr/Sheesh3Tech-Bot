import discord

TOKEN = 'OTU1ODUxNzU4MzY0NjYzODQ4.YjnsUg.OtDq97E-dWNksSaWx_-qEXLgrfo'

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}') 

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hlp Hi' or message.content == 'hlp hi':
        await message.channel.send('Hello! Thank you for contacting C3 Tech! A tech will be able to assist you shortly!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hlp remote' or message.content == 'hlp Remote':
        await message.channel.send('Hi! Please go to help.myc3.tech and a tech will give you were code when you are at the screen that says "please join with a code!"')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hlp pam' or message.content == 'hlp Pam':
        await message.channel.send('PIss off')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hlp ur mum' or message.content == 'hlp your mom' or message.content == 'ur mom':
        await message.channel.send('My Mom? I think you mean your mom cause I did her last night and im a bot.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hlp suicide' or message.content == 'hlp Suicide':
        await message.channel.send('Suicide isnt the answer unless youre in IT because then its the right thing to do.')


client.run(TOKEN)