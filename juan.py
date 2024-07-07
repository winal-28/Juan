import discord
from discord.ext import commands
import random
import asyncio
#from webserver import keep_alive
import os
from dotenv import load_dotenv
from discord.ext.commands import MissingPermissions

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

juan = commands.Bot(command_prefix='j', intents=intents)


@juan.event
async def on_ready():
    print('Im in.')
    await juan.change_presence(activity=discord.Game(name="jjuancommands"))
    juan.remove_command('help')


@juan.event
async def on_member_join(ctx, member):
    await ctx.send(f'{member} is in the server!')


@juan.event
async def on_member_remove(ctx, member):
    await ctx.send(f'{member} left :(')

@juan.command()
async def test(ctx, arg):
    await ctx.send(arg)

@juan.command()
async def juancommands(ctx):
    nl = '\n'
    embed = discord.Embed(
        title="Juan Commands",
        url="https://discord.com/app",
        description=
        f"Command prefix: j {nl} Here are the list of commands:{nl} kamusta - Make me introduce myself{nl} juancommands - Shows this {nl} tangina_mo - Makes me mad >:( {nl} makemefeelbetter - comports you in my bery shitty accent{nl} adobo, rice - shows gifs of adobo and rice, {nl} president, vicepresident, traitor, mikeybustos, (more will be added) - shows you information about them, {nl} msg (insert what you want me to say here) - makes me say shit on your demand!, {nl} movie - send an interesting movie, {nl} howtomakeadobo, howtomakecaldereta, (more will be added) - sends a youtube video on how to make those popular Filipino cuisines {nl}{nl} Moderation Commands {nl}{nl} kick (insert user here) - kicks the member you want to kick {nl} ban (insert user here) - bans the member you want to kick {nl}{nl} Note: there are no unban, tempban, or mute commands yet as ALwin is still trying to find out how to. If you do know please tell him lmfao{nl}{nl} Mabuhay ang Pilipinas!",
        color=0xFF5733)
    await ctx.send(embed=embed)

#moderation commands
#kick
@juan.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    if reason is None:
        reason="no reason provided"
        try:
            await ctx.guild.kick(user)
            await ctx.send(f"User {user.mention} has been kicked for {reason}.")
        except: 
            pass

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to kick members.")

#ban
@juan.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    if reason is None:
        reason="no reason provided"
        try:
            await ctx.guild.ban(user)
            await ctx.send(f"User {user.mention} has been banned for {reason}.")
        except: 
            pass

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to ban members.")


#unban
@juan.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name,
                                               member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(
                f"{user} has been unbanned sucessfully, we hope you behave, kababayan :ok_hand:"
            )
            return


#utility commands
@juan.command()
async def ping(ctx):
    await ctx.send(f'Pongina! {round(juan.latency * 1000)}ms')


@juan.command()
async def comands(ctx):
    await ctx.send('@everyone')


@juan.command()
async def kamusta(ctx):
    await ctx.send(
        'Kamusta, kababayan! My name is Juan, I am a discord bot from the Philippines! I started being developed at exactly 2/17/2021, by ALwin#6481. I am always in development.'
    )


@juan.command()
async def tangina_mo(ctx):
    await ctx.send('tangina mo rin de puta ka >:(')


@juan.command()
async def makemefeelbetter(ctx):
    await ctx.send(
        'You are a bery nice person, you are bery good. Peel better now?')


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
    await ctx.send(
        f'https://www.youtube.com/watch?v=7jyJZkVvyzo{nl}https://www.youtube.com/watch?v=95myX7HIxYk{nl}which one do you preper?'
    )


@juan.command()
async def howtomaketinola(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=pEMMBceYyMw')


@juan.command()
async def rap(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=qGGWDvxGGio')


@juan.command()
async def like(ctx):
    await ctx.send(f'Periodiccia, :heart::rose:')


@juan.command(aliases=['adobo', 'adoboe'])
async def abobo(ctx):
    adobo_gifsandpics = [
        'https://media.tenor.com/images/1f144abe4891281dd4786842488c6c33/tenor.gif',
        'https://media.tenor.com/images/6ba0f60bff9518494ff0d506403320e1/tenor.gif',
        'https://media.tenor.com/images/a20092b3dd11402d31e9074e103450f3/tenor.gif',
        'https://media.tenor.com/images/faffe8af1ba62b56f28307cdb836e41d/tenor.gif',
        'https://2.bp.blogspot.com/-fJLCy4m8OD8/T9K7PlygFqI/AAAAAAAAHrY/MeFcYoPpHcI/s1600/IMG_4536.JPG',
        'https://simply-delicious-food.com/wp-content/uploads/2019/09/Easy-Chicken-Adobo-3.jpg'
    ]
    await ctx.send(f'ADOBO POTOSYAP {random.choice(adobo_gifsandpics)}')


@juan.command()
async def rice(ctx):
    rice_picsandgifs = [
        'https://media.tenor.com/images/93ceee83581f9c349b567807abed8d98/tenor.gif',
        'https://media.tenor.com/images/54abcc48c38f29750afdbab38326ee7c/tenor.gif',
        'https://media.tenor.com/images/3a08b4b5ff0c4afdf9a30dc75ffd4daf/tenor.gif',
        'https://media.tenor.com/images/92b1bfc8bde13361f0ea6a7a40d6cd22/tenor.gif'
    ]
    await ctx.send(f'RICE {random.choice(rice_picsandgifs)}')


@juan.command()
async def kaldereta(ctx):
    kaldereta_picsandgifs = [
        'https://www.seriouseats.com/recipes/assets_c/2011/01/20110114-goatstewcebu-primary_2-thumb-625xauto-137330.jpg',
        'https://1.bp.blogspot.com/-LwCvTIP1sDc/XS6vJdaol5I/AAAAAAAATeo/gtAci_LPtXcS4u7C8zCE8BEXnEXZxR9WQCLcBGAs/s1600/2.jpg',
        'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.qXFJL3UKG7exeICGovxw3gHaHa%26pid%3DApi&f=1',
        'https://i0.wp.com/www.astigvegan.com/wp-content/uploads/2018/04/astigvegan-veganizing-kaldereta-stew-1.jpg?resize=1024%2C1024'
    ]
    await ctx.send(
        f'Nagugutom na ako tangina {random.choice(kaldereta_picsandgifs)}')


@juan.command()
async def lechon(ctx):
    lechon_picsandgifs = [
        'https://lhyziebongon.com/wp-content/uploads/2017/12/Lechon-Belly-Raw-1.jpg',
        'http://2.bp.blogspot.com/-zjSCapI0lns/Uwmx49GWd5I/AAAAAAAAEBE/yOPv0naLK0k/s1600/lechon+pieces.JPG',
        'https://coconuts.co/wp-content/uploads/2018/06/ricos-lechon-062518.jpg'
    ]
    await ctx.send(f'Ayun, may birthday! {random.choice(lechon_picsandgifs)}')


@juan.command()
async def sinigang(ctx):
    sinigang_picsandgifs = [
        'https://img.theculturetrip.com/1440x/smart/wp-content/uploads/2017/12/8741298156_33c53ac422_k.jpg',
        'https://philnews.ph/wp-content/uploads/2019/04/Sinigang-Recipe.jpg',
        'https://eatlikepinoy.com/wp-content/uploads/2019/11/sinigang.jpg',
        'https://1.bp.blogspot.com/-HtO-uqzQeBw/VMmuu9AIBWI/AAAAAAAADNM/QGFoOtjst-E/s1600/Sinigang-Recipe3.jpg'
    ]
    await ctx.send(
        f'Asim kilig, gusto ko pa! Gusto ko pang kumain ng sinigang na love namin! :heart: {random.choice(sinigang_picsandgifs)}'
    )


@juan.command()
async def joe(ctx):
    await ctx.send('joe joe joe joe joe joe joe joe joe joe joe')


@juan.command()
async def say(ctx):
    await ctx.send('Use `j msg`, I can see you from my fking terminal dude')


@juan.command()
async def msg(ctx, *, message):
    try:
        await ctx.message.delete()
        await ctx.send(message)
    except:
        await ctx.send("Please Give Some Message!")


@juan.command()
async def invite(ctx):
    await ctx.send(
        f'https://discord.com/api/oauth2/authorize?client_id=811521046377005068&permissions=0&scope=bot'
    )


@juan.command()
async def mikeybustos(ctx):
    embed = discord.Embed(
        title="Mikey Bustos",
        url="https://duckduckgo.com/mikeybustos",
        description=
        "Michael John Tumanguil Pestano Bustos is a Filipino–Canadian singer and comedian who has appeared on the reality television show Canadian Idol. He is also the owner of AntsCanada, an online shop that specialises in ant-keeping.",
        color=0xFF5733)
    embed.set_thumbnail(
        url=
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Mikeyredcarpet.jpg/220px-Mikeyredcarpet.jpg"
    )
    await ctx.send(embed=embed)


@juan.command()
async def president(ctx):
    embed = discord.Embed(
        title="Rodrigo Roa Duterte",
        url="https://duckduckgo.com/rodrigoduterte",
        description=
        "Rodrigo Roa Duterte, also known as Digong and Rody, is a Filipino politician who is the current president of the Philippines and the first from Mindanao to hold the office. He is the chairperson of PDP–Laban, the ruling political party in the Philippines.",
        color=0xFF5733)
    embed.set_thumbnail(url="https://duckduckgo.com/i/2c883356.jpg")
    await ctx.send(embed=embed)


@juan.command()
async def vicepresident(ctx):
    embed = discord.Embed(
        title="Bongbong Marcos",
        url="https://duckduckgo.com/bongbongmarcos",
        description=
        "Ferdinand \"Bongbong\" Romualdez Marcos Jr. is a Filipino politician who most recently served as a senator in the 16th Congress. He is the second child and only son of former President and dictator Ferdinand E. Marcos and of former First Lady Imelda Romualdez-Marcos.",
        color=0xFF5733)
    embed.set_thumbnail(url="https://duckduckgo.com/i/ace9d772.jpg")
    await ctx.send(embed=embed)


@juan.command()
async def traitor(ctx):
    embed = discord.Embed(
        title="Emilio Aguinaldo",
        url="https://duckduckgo.com/emilioaguinaldo",
        description=
        "Emilio Aguinaldo y Famy was a Filipino revolutionary, politician, and military leader who is officially recognized as the first and the youngest President of the Philippines and the first president of a constitutional republic in Asia.",
        color=0xFF5733)
    embed.set_thumbnail(url="https://duckduckgo.com/i/b7692918.jpg")
    await ctx.send(embed=embed)


@juan.command()
async def movie(ctx):
    embed = discord.Embed(
        title="Heneral Luna",
        url="https://duckduckgo.com/heneralluna",
        description=
        "Heneral Luna is a 2015 Filipino historical biopic film depicting General Antonio Luna's leadership of the Philippine Revolutionary Army during the Philippine–American War. Directed by Jerrold Tarog and produced by Artikulo Uno Productions, the film received critical acclaim from critics, praising its cinematography, writing, acting and plot",
        color=0xFF5733)
    embed.set_thumbnail(url="https://duckduckgo.com/i/8934f749.jpg")
    await ctx.send(embed=embed)


#keep_alive()
load_dotenv()
token = os.environ['TOKEN']
juan.run(token)
