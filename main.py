import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/", intents=discord.Intents().all())


@bot.command()
async def hello(ctx):
    await ctx.reply("WhatsApp bro")

bot.run(token="MTE1NzI3MzE0NDk5NDgyNDI4Mw.GLddO3.ta6R8fCqQg4ErS7qtBfrIU1FfGP2FvW5DL6mdc")
 asfaasasf
