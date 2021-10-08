import logging
import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv

from cogs import greetings_cog

# Join Link: https://discord.com/oauth2/authorize?client_id=896062886726762517&scope=bot&permissions=8

load_dotenv()

bot = commands.Bot(command_prefix='>')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.event
async def on_ready():
    print("bot is ready")
    print([c.name for c in bot.get_cog("Greetings").get_commands()])

if __name__ == "__main__":
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    bot.add_cog(greetings_cog.Greetings(bot))
    bot.run(getenv("TOKEN"))
