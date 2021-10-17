import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='.', intents= discord.Intents.all())
  
@bot.command()
async def load(ctx, extension):
    bot.load_extension(extension)
    print('Loaded ' + extension)
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(extension)
    print('Unloaded ' + extension)

bot.load_extension('cog') # Loading cog by default without need of commands.

bot.run('ODk4OTMzODI1NBF2MDczMjg2.YWraXQ.F9kMt4oafigdIGfzZ_N0GTXmcok') # Token
