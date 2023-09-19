import os
import discord
from discord import app_commands
from discord.ext import commands


class EMBEDS(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('embeds are ready')

    @app_commands.command(name="sound_list", description='List of all available sounds')
    async def my_command(self, interaction: discord.Interaction) -> None:
        folder_path = './sounds/'

        mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]

        embed = discord.Embed(title="🔊Available Sounds🔊")

        for mp3_file in mp3_files:
            embed.add_field(name=mp3_file[:-4], value="", inline=False)

        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EMBEDS(bot))
