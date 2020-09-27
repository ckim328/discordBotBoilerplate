import os 
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TKN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name==GUILD:
            break
    print('f{client.user} has connected')
    print({guild.name})

client.run(TOKEN)