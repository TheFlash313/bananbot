import discord
from discord.ext import commands
from music import Player

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="-", intents=intents)

@bot.event
async def on_ready():
  print(f"{bot.user.name} is ready.")

async def setup():
  await bot.wait_until_ready()
  bot.add_cog(Player(bot))

bot.loop.create_task(setup())
bot.run("ODg3MDExMDE1NjgwNzIwOTA2.YT97Yg.wpCFiW_MinCsV4CsRYC9Jk8KRBw")