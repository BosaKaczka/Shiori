import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="Test command to check if the bot is online")
    async def ping(self, ctx):
        await ctx.send("Pong!")

def setup(bot):
    bot.add_cog(Ping(bot))
