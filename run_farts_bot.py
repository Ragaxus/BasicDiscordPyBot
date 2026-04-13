import discord
import os
from dotenv import load_dotenv  

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "farts" in message.content:
        await message.reply('Ha ha, you said "farts"')

load_dotenv()
client.run(os.environ.get('DISCORD_APP_KEY'))