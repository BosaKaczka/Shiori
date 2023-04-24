import discord
from discord_slash import SlashCommand
from discord.ext import commands
import os
import settings

logger = settings.logging.getLogger("bot")


def run():
    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), activity=discord.Game(name="Spanko (˃ᆺ˂)"))
    slash = SlashCommand(bot, sync_commands=True)

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

    @bot.event
    async def on_ready():
        logger.info(f'User: {bot.user} (ID: {bot.user.id})')

    bot.run(settings.TOKEN)


if __name__ == "__main__":
    run()
