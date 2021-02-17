import discord
from discord.ext import commands



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pongina')


client = myClient()
client.run('ODExNTIxMDQ2Mzc3MDA1MDY4.YCzZ3g.BAgyv91p2W1rU7qDQfzh_buym1I')


#bot = commands.Bot(command_prefix='j')


#@bot.command()
#async def ping(ctx):
  #  await ctx.send('pongina')

#bot.run('ODExNTIxMDQ2Mzc3MDA1MDY4.YCzZ3g.BAgyv91p2W1rU7qDQfzh_buym1I')

