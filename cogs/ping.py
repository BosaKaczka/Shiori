import discord
from discord import app_commands
from discord.ext import commands


class Ping(commands.Cog):
    def __int__(self, bot: commands.Bot) -> None:
        self.bot = bot

    print('done')

    # @app_commands.command(name='ping222222', description='Test')
    # async def ping2(self, interaction: discord.Interaction) -> None:
    #     await interaction.response.send_message('pong', ephemeral=True)
    #
    # @app_commands.command(name='banan')
    # @app_commands.describe(text='Text to say')
    # async def say(interaction: discord.Interaction, text: str):
    #     await interaction.response.send_message(f'Test: {text}', ephemeral=False)

    async def setup(bot: commands.Bot) -> None:
        await bot.add_cog(Ping(bot))
