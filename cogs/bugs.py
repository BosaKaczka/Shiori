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
        embed = discord.Embed(title=f"{str(interaction.user)[:-5]} reported a bug")
        embed.add_field(name=f"**Bug description**:\n",
                        value=f"{bug_description}", inline=False)
        user_ids = [490481737651060736, 264885219918741506]
        for user_id in user_ids:
            user = await self.bot.fetch_user(user_id)
            channel = await user.create_dm()
            await channel.send(embed=embed)

        await interaction.response.send_message('Your report has been submitted', ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BUGS(bot))
