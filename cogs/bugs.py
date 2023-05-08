import discord
from discord import app_commands
from discord.ext import commands


class BUGS(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('bugs are ready.')

    @app_commands.command(name="bug", description='Report a bug')
    async def bug_report(self, interaction: discord.Interaction, bug_description: str) -> None:
        embed = discord.Embed(title="Report has been sent")
        embed.add_field(name=f"{str(interaction.user)[:-5]} reported a bug", value=f"**Bug description**:\n{bug_description}", inline=False)
        f = open("./feedback/bugs.txt", "a")
        f.write(f"{str(interaction.user)}\n{bug_description}\n\n")
        f.close()
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BUGS(bot), guilds=[discord.Object(id=690938920199782420)])
