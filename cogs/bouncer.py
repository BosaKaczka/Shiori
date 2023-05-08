import discord
from discord import app_commands
from discord.ext import commands
from random import randrange


class BOUNCER(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.voice_wait_id = 1105247676733345832
        self.voice_goto_id = 696787306098589717
        self.role_name = "⛄Bałwany⛄"

    @commands.Cog.listener()
    async def on_ready(self):
        voice_channel = self.bot.get_channel(self.voice_wait_id)
        if voice_channel:
            await voice_channel.connect()
            print(f'Bouncer ready in {voice_channel.name}')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState,
                                    after: discord.VoiceState):
        if after.channel and after.channel.id == self.voice_wait_id:
            role = discord.utils.get(member.roles, name=self.role_name)
            if role or 1 == randrange(0, 101):      # 1% chance to fool bouncer
                new_channel = self.bot.get_channel(self.voice_goto_id)
                await member.move_to(new_channel)
            elif discord.utils.get(member.roles, name='Shiori BOT'):
                return
            else:
                await member.move_to(None)

    @app_commands.command(name="kamikaze", description='Try me!')
    async def kamikaze(self, interaction: discord.Interaction) -> None:
        members = interaction.user.voice.channel.members
        for member in members:
            await member.move_to(None)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BOUNCER(bot), guilds=[discord.Object(id=690938920199782420)])
