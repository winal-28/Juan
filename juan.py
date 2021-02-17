import discord
from discord.ext import commands


juan = commands.Bot(command_prefix = 'j ')

@juan.event
async def on_ready():
    print('Im in.')

@juan.command()
async def kamusta(ctx):
    await ctx.send('Kamusta, kababayan. My name is Juan, I am a discord bot from the Philipines!')

@juan.command()
async def commands(ctx):
    await ctx.send(f'```Here are the list of commands: j kamusta - Make me introduce myself, j commands - Shows the list of commands, j tangina_mo - Make me mad >:( ```')

@juan.command()
async def tangina_mo(ctx):
    await ctx.send('tangina mo rin de puta ka >:(')

#@juan.event
#async def on_member_join(member):
 #   print(f'{member} is in! Kamusta Kababayan!')

#@juan.event
#async def on_member_remove(member):
 #   print(f'{member} is gone! We hope you return kababayan ;(')


juan.run('ODExNTIxMDQ2Mzc3MDA1MDY4.YCzZ3g.BAgyv91p2W1rU7qDQfzh_buym1I')

