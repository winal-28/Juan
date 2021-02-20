import discord
from discord.ext import commands
import random
import os

juan = commands.Bot(command_prefix = 'j ')

@juan.event
async def on_ready():
    print('Im in.')
    await juan.change_presence(activity=discord.Game(name="j commands")), juan.remove_command('help')

@juan.event
async def on_member_join(member, ctx):
    await ctx.send(f'{member} is in the server!')
    
@juan.event
async def on_member_remove(member, ctx):
    await ctx.send(f'{member} left :(')


    
#moderation commands

#kick
@juan.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"{user} has been kicked sucessfully :ok_hand:")

#ban
@juan.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} has been bannned sucessfully")

#unban
@juan.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f"{user} has been unbanned sucessfully, we hope you behave, kababayan :ok_hand:")
    return

#utility commands
@juan.command()
async def ping(ctx):
    await ctx.send(f'Pongina! {round(juan.latency * 1000)}ms')

@juan.command()
async def kamusta(ctx):
    await ctx.send('Kamusta, kababayan! My name is Juan, I am a discord bot from the Philipines! I started being developed at exactly 2/17/2021, by ALwin#6481. I am always in development.')


@juan.command()
async def commands(ctx):
    nl = '\n'
    embed=discord.Embed(title="Juan Commands", url="https://discord.com/app", description=f"Here are the list of commands:{nl} j kamusta - Make me introduce myself{nl} j commands - Shows this {nl} j tangina_mo - Makes me mad >:( {nl} j makemefeelbetter - comports you in my bery shitty accent{nl} j adobo, j rice - shows gifs of adobo and rice, {nl} j president, j vicepresident, j traitor, j mikeybustos, (more will be added) - shows you information about them, {nl} j msg (insert what you want me to say here) - makes me say shit on your demand!, {nl} j movie - send an interesting movie, {nl} j howtomakeadobo, j howtomakecaldereta, (more will be added) - sends a youtube video on how to make those popular Filipino cuisines {nl}{nl} Moderation Commands {nl}{nl} j kick (insert user here) - kicks the member you want to kick {nl} j ban (insert user here) - bans the member you want to kick {nl}{nl} Note: there are no unban, tempban, or mute commands yet as ALwin is still trying to find out how to. If you do know please tell him lmfao {nl} Note 2: There is currently a Tropical Depression in ALwin\'s area so he prolly wouldn't be updating me any soon unless the electricity comes back (if it gets cut off because of the wind :( ){nl}{nl} Mabuhay ang Pilipinas!", color=0xFF5733)
    await ctx.send(embed=embed)

@juan.command()
async def tangina_mo(ctx):
    await ctx.send('tangina mo rin de puta ka >:(')

@juan.command()
async def makemefeelbetter(ctx):
    await ctx.send('You are a bery nice person, you are bery good. Peel better now?')

@juan.command()
async def roast_quaccy(ctx):
    await ctx.send(f'No, I dont think I will')

@juan.command()
async def praise_yourself(ctx):
    await ctx.send(f'```This is Juan, he is very smart, be like Juan.```')

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
    await ctx.send(f'Periodiccia, :heart::rose:')

@juan.command(aliases = ['adobo', 'adoboe'])
async def abobo(ctx):
    adobo_gifsandpics = ['https://media.tenor.com/images/1f144abe4891281dd4786842488c6c33/tenor.gif', 'https://media.tenor.com/images/6ba0f60bff9518494ff0d506403320e1/tenor.gif', 'https://media.tenor.com/images/a20092b3dd11402d31e9074e103450f3/tenor.gif', 'https://media.tenor.com/images/faffe8af1ba62b56f28307cdb836e41d/tenor.gif', 'https://2.bp.blogspot.com/-fJLCy4m8OD8/T9K7PlygFqI/AAAAAAAAHrY/MeFcYoPpHcI/s1600/IMG_4536.JPG', 'https://simply-delicious-food.com/wp-content/uploads/2019/09/Easy-Chicken-Adobo-3.jpg']
    await ctx.send(f'ADOBO POTOSYAP {random.choice(adobo_gifsandpics)}')

@juan.command()
async def rice(ctx):
    rice_picsandgifs = ['https://media.tenor.com/images/93ceee83581f9c349b567807abed8d98/tenor.gif', 'https://media.tenor.com/images/54abcc48c38f29750afdbab38326ee7c/tenor.gif', 'https://media.tenor.com/images/3a08b4b5ff0c4afdf9a30dc75ffd4daf/tenor.gif', 'https://media.tenor.com/images/92b1bfc8bde13361f0ea6a7a40d6cd22/tenor.gif' ]
    await ctx.send(f'RICE {random.choice(rice_picsandgifs)}')

@juan.command()
async def say(ctx):
    await ctx.send('I can see you from my fking terminal dude')

@juan.command()
async def msg(ctx, *, message):
    try:
        await ctx.message.delete()
        await ctx.send(message)
    except:
        await ctx.send("Please Give Some Message!")

@juan.command()
async def invite(ctx):
    await ctx.send(f'https://discord.com/api/oauth2/authorize?client_id=811521046377005068&permissions=0&scope=bot')


@juan.command()
async def mikeybustos(ctx):
    embed=discord.Embed(title="Mikey Bustos", url="https://duckduckgo.com/mikeybustos", description="Michael John Tumanguil Pestano Bustos is a Filipino–Canadian singer and comedian who has appeared on the reality television show Canadian Idol. He is also the owner of AntsCanada, an online shop that specialises in ant-keeping.", color=0xFF5733)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Mikeyredcarpet.jpg/220px-Mikeyredcarpet.jpg")
    await ctx.send(embed=embed)

@juan.command()
async def president(ctx):
    embed=discord.Embed(title="Rodrigo Roa Duterte", url="https://duckduckgo.com/rodrigoduterte", description="Rodrigo Roa Duterte, also known as Digong and Rody, is a Filipino politician who is the current president of the Philippines and the first from Mindanao to hold the office. He is the chairperson of PDP–Laban, the ruling political party in the Philippines.", color=0xFF5733)
    embed.set_thumbnail(url="https://duckduckgo.com/i/2c883356.jpg")
    await ctx.send(embed=embed)

@juan.command()
async def vicepresident(ctx):
    embed=discord.Embed(title="Bongbong Marcos", url="https://duckduckgo.com/bongbongmarcos", description="Ferdinand \"Bongbong\" Romualdez Marcos Jr. is a Filipino politician who most recently served as a senator in the 16th Congress. He is the second child and only son of former President and dictator Ferdinand E. Marcos and of former First Lady Imelda Romualdez-Marcos.", color=0xFF5733)
    embed.set_thumbnail(url="https://duckduckgo.com/i/ace9d772.jpg")
    await ctx.send(embed=embed)

@juan.command()
async def traitor(ctx):
    embed=discord.Embed(title="Emilio Aguinaldo", url="https://duckduckgo.com/emilioaguinaldo", description="Emilio Aguinaldo y Famy was a Filipino revolutionary, politician, and military leader who is officially recognized as the first and the youngest President of the Philippines and the first president of a constitutional republic in Asia.", color=0xFF5733)
    embed.set_thumbnail(url="https://duckduckgo.com/i/b7692918.jpg")
    await ctx.send(embed=embed)

@juan.command()
async def movie(ctx):
    embed=discord.Embed(title="Heneral Luna", url="https://duckduckgo.com/heneralluna", description="Heneral Luna is a 2015 Filipino historical biopic film depicting General Antonio Luna's leadership of the Philippine Revolutionary Army during the Philippine–American War. Directed by Jerrold Tarog and produced by Artikulo Uno Productions, the film received critical acclaim from critics, praising its cinematography, writing, acting and plot", color=0xFF5733)
    embed.set_thumbnail(url="https://duckduckgo.com/i/8934f749.jpg")
    await ctx.send(embed=embed)   








juan.run(os.environ['token'])

