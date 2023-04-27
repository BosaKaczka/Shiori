import discord
from discord import app_commands
from discord.ext import commands
import os
import settings

logger = settings.logging.getLogger("bot")


def run():
    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), activity=discord.Game(name="Spanko (˃ᆺ˂)"))


    # for filename in os.listdir('./cogs'):
    #     if filename.endswith('.py'):
    #         bot.load_extension(f'cogs.{filename[:-3]}')

    @bot.event
    async def on_ready():
        logger.info(f'User: {bot.user} (ID: {bot.user.id})')
        try:
            synced = await bot.tree.sync()
            print(f'Synced {len(synced)} command(s)')
        except Exception as e:
            print(e)

    @bot.tree.command(name='ping')
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong',ephemeral=True)

    @bot.tree.command(name='banan')
    @app_commands.describe(text='Text to say')
    async def say(interaction: discord.Interaction, text: str):
        await interaction.response.send_message(f'Test: {text}',ephemeral=False)

    bot.run(settings.TOKEN)


if __name__ == "__main__":
    run()
