import discord
from discord import app_commands
from discord.ext import commands


class IDEAS(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('ideas are ready.')

    @app_commands.command(name="idea", description='Let us know what would you like us to add to the Bot')
    async def bug_report(self, interaction: discord.Interaction, idea: str) -> None:
        embed = discord.Embed(title=f"Thank you for your submission")
        embed.add_field(name=f"{str(interaction.user)[:-5]}'s idea:", value=f"{idea}", inline=False)
        f = open("./feedback/ideas.txt", "a")
        f.write(f"{str(interaction.user)}\n{idea}\n\n")
        f.close()
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(IDEAS(bot), guilds=[discord.Object(id=690938920199782420)])
