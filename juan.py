import discord
from discord.ext import commands


client = commands.Bot(command_prefix = 'j ')

@client.event
async def on_ready():
    print('Im in.')


client.run('ODExNTIxMDQ2Mzc3MDA1MDY4.YCzZ3g.BAgyv91p2W1rU7qDQfzh_buym1I')

