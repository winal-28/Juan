import discord
from discord.ext import commands
import random


juan = commands.Bot(command_prefix = 'j ')

@juan.event
async def on_ready():
    print('Im in.')
    await juan.change_presence(activity=discord.Game(name="j commands")), juan.remove_command('help')

@juan.command()
async def ping(ctx):
    await ctx.send('Pongina!')

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

@juan.command()
async def stfu(ctx):
    await ctx.author.send('You shut the puck up, tangina!')

@juan.command()
async def howtomakeadobo(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=Ix5Dnud1bl0')

@juan.command()
async def howtomakecaldereta(ctx):
    nl = '\n'
    await ctx.send(f'https://www.youtube.com/watch?v=7jyJZkVvyzo{nl}https://www.youtube.com/watch?v=95myX7HIxYk{nl}which one do you preper?')

@juan.command()
async def rap(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=qGGWDvxGGio')

@juan.command()
async def like(ctx):
    await ctx.send(f'Periodiccia, :flushed::rose:')

@juan.command(aliases = ['adobo', 'adoboe'])
async def abobo(ctx):
    adobo_gifsandpics = ['https://media.tenor.com/images/1f144abe4891281dd4786842488c6c33/tenor.gif', 'https://media.tenor.com/images/6ba0f60bff9518494ff0d506403320e1/tenor.gif', 'https://media.tenor.com/images/a20092b3dd11402d31e9074e103450f3/tenor.gif', 'https://media.tenor.com/images/faffe8af1ba62b56f28307cdb836e41d/tenor.gif', 'https://2.bp.blogspot.com/-fJLCy4m8OD8/T9K7PlygFqI/AAAAAAAAHrY/MeFcYoPpHcI/s1600/IMG_4536.JPG', 'https://simply-delicious-food.com/wp-content/uploads/2019/09/Easy-Chicken-Adobo-3.jpg']
    await ctx.send(f'ADOBO POTOSYAP {random.choice(adobo_gifsandpics)}')

@juan.command()
async def rice(ctx):
    rice_picsandgifs = ['https://media.tenor.com/images/93ceee83581f9c349b567807abed8d98/tenor.gif', 'https://media.tenor.com/images/54abcc48c38f29750afdbab38326ee7c/tenor.gif', 'https://media.tenor.com/images/3a08b4b5ff0c4afdf9a30dc75ffd4daf/tenor.gif', 'https://media.tenor.com/images/92b1bfc8bde13361f0ea6a7a40d6cd22/tenor.gif' ]
    await ctx.send(f'RICE {random.choice(rice_picsandgifs)}')



#@juan.event
#async def on_member_join(member):
 #   print(f'{member} is in! Kamusta Kababayan!')

#@juan.event
#async def on_member_remove(member):
 #   print(f'{member} is gone! We hope you return kababayan ;(')


juan.run('ODExNTIxMDQ2Mzc3MDA1MDY4.YCzZ3g.BAgyv91p2W1rU7qDQfzh_buym1I')

