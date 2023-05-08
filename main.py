import asyncio
import discord
from discord.ext import commands
import os
import settings

logger = settings.logging.getLogger("bot")


def run():
    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), application_id='1002541803624484925',
                       activity=discord.Game(name="Spanko"))

    @bot.event
    async def on_ready():
        logger.info(f'User: {bot.user} (ID: {bot.user.id})')

    async def load():
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                await bot.load_extension(f'cogs.{file[:-3]}')

    async def main():
        await load()
        await bot.start(settings.TOKEN)

    @bot.command()
    @commands.is_owner()
    async def sync(ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        print(f'Synced {len(fmt)} commands.')
        await ctx.message.delete()

    asyncio.run(main())


if __name__ == "__main__":
    run()
