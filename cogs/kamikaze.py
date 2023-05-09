import discord
from discord import app_commands
from discord.ext import commands


class KAMIKAZE(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('KAMIKAZE ready')

    @app_commands.command(name="kamikaze", description='Try me!')
    async def kamikaze(self, interaction: discord.Interaction) -> None:
        members = interaction.user.voice.channel.members
        for member in members:
            await member.move_to(None)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(KAMIKAZE(bot), guilds=[discord.Object(id=690938920199782420)])
