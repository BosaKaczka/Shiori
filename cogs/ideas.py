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
    async def idea(self, interaction: discord.Interaction, idea: str) -> None:
        embed = discord.Embed(title=f"{str(interaction.user)[:-5]}'s idea:")
        embed.add_field(name=f"{idea}", value="", inline=False)

        user_ids = [490481737651060736, 264885219918741506]
        for user_id in user_ids:
            user = await self.bot.fetch_user(user_id)
            channel = await user.create_dm()
            await channel.send(embed=embed)

        await interaction.response.send_message("Thank you for your submission", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(IDEAS(bot))
