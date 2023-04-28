import discord
from discord import app_commands
from discord.ext import commands
import os
import settings

logger = settings.logging.getLogger("bot")


def run():
    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), activity=discord.Game(name="Spanko (˃ᆺ˂)"))

    @bot.event
    async def on_ready():
        logger.info(f'User: {bot.user} (ID: {bot.user.id})')
        # try:
        #     synced = await bot.tree.sync()
        #     print(f'Synced {len(synced)} command(s)')
        # except Exception as e:
        #     print(e)

    bot.run(settings.TOKEN)


if __name__ == "__main__":
    run()
