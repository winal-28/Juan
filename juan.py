import discord
from discord.ext import commands


juan = commands.Bot(command_prefix = 'j ')

@juan.event
async def on_ready():
    print('Im in.')
    await juan.change_presence(activity=discord.Game(name="j commands"))

@juan.command()
async def kamusta(ctx):
    await ctx.send('Kamusta, kababayan! My name is Juan, I am a discord bot from the Philipines! I started being developed at exactly 2/17/2021, by ALwin#6481')

@juan.command()
async def commands(ctx):
    nl = '\n'
    await ctx.send(f'```Here are the list of commands:{nl}{nl} j kamusta - Make me introduce myself{nl} j commands - Shows the list of commands{nl} j tangina_mo - Make me mad >:( {nl} j makemefeelbetter - comports you in my bery shitty accent{nl}{nl}For more information, DM ALwin#6481{nl}Just like Periodiccia, I also have secret commands! Good luck on finding them out lmao{nl}{nl}Sa ngalan ng Bansang Maharlika!```')

@juan.command()
async def tangina_mo(ctx):
    await ctx.send('tangina mo rin de puta ka >:(')

@juan.command()
async def makemefeelbetter(ctx):
    await ctx.send('You are a bery nice person, you are bery good. Peel better now?')

@juan.command()
async def roast_quaccy(ctx):
    await ctx.send(f'Hey ~~Quaccy~~ Periodiccia, Lets Pight!')

@juan.command()
async def praise_yourself(ctx):
    await ctx.send(f'```This is Juan, he is very smart, be like Juan```')

@juan.command()
async def nice(ctx):
    await ctx.send('nice indeed, kababayan')

#@juan.event
#async def on_member_join(member):
 #   print(f'{member} is in! Kamusta Kababayan!')

#@juan.event
#async def on_member_remove(member):
 #   print(f'{member} is gone! We hope you return kababayan ;(')


juan.run('ODExNTIxMDQ2Mzc3MDA1MDY4.YCzZ3g.BAgyv91p2W1rU7qDQfzh_buym1I')

