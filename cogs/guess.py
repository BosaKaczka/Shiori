import discord
from discord import app_commands
from discord.ext import commands
from random import randrange


class GUESS(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.num_to_guess = None
        self.num_max = None
        self.num_min = None
        self.attempt = None
        self.tries = None
        self.bot = bot

    async def newgame(self):
        self.num_to_guess = int(randrange(0, 1001))
        self.num_max = int(1000)
        self.num_min = int(0)
        self.attempt = 0
        self.tries = [" ", " ", " ", " "]

    @commands.Cog.listener()
    async def on_ready(self):
        print('guess is ready.')
        await self.newgame()

    @app_commands.command(name="guess", description='Try to guess the secret number')
    async def guess(self, interaction: discord.Interaction, number: int) -> None:
        self.attempt += 1
        if number == self.num_to_guess:
            embed = discord.Embed(
                title=f"🏆**{str(interaction.user)[:-5]}** has guessed the number!🏆\nThe number was **{number}**",
                color=0xffd700)
            embed.set_footer(text=f"Attempt {self.attempt}")

            await interaction.response.send_message(embed=embed, ephemeral=False)
            await self.newgame()
            return
        if self.num_max > number > self.num_to_guess:
            self.num_max = number
        if self.num_min < number < self.num_to_guess:
            self.num_min = number

        self.tries.insert(0, f"**{str(interaction.user)[:-5]}** tried **{number}**")

        embed = discord.Embed(title=f"{str(interaction.user)[:-5]} tries {number}")
        embed.set_thumbnail(url=interaction.user.avatar)
        embed.add_field(name="The Secret Number", value=f"{self.num_min} < | X | < {self.num_max}", inline=False)
        embed.add_field(name="Recent Attempts", value=f"{self.tries[1]}\n{self.tries[2]}\n{self.tries[3]}",
                        inline=False)
        embed.set_footer(text=f"Attempt {self.attempt}")

        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="secret_number", description='Check the current state of the game')
    async def check(self, interaction: discord.Interaction) -> None:

        embed = discord.Embed(title=f"Game in which you have to guess the secret number.\nCurrent state:")
        embed.add_field(name="The Secret Number", value=f"{self.num_min} < | X | < {self.num_max}", inline=False)
        embed.add_field(name="Recent Attempts", value=f"{self.tries[1]}\n{self.tries[2]}\n{self.tries[3]}",
                        inline=False)
        embed.set_footer(text=f"Attempts {self.attempt}")

        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GUESS(bot), guilds=[discord.Object(id=690938920199782420)])
