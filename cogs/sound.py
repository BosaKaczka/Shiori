import asyncio
import discord
from discord.ext import commands
from discord import app_commands
from discord import FFmpegPCMAudio


class SOUND(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.settings = {}

    @commands.Cog.listener()
    async def on_ready(self):
        print('sound is ready')

    @app_commands.command(name="sound", description="Set up a sound that will play after you sound a VC")
    async def set_command(
            self,
            interaction: discord.Interaction,
            sound_name: str
    ) -> None:
        user_id = interaction.user.id
        self.settings[user_id] = {
            "sound_name": sound_name,
        }
        await interaction.response.send_message(
            f"Sound sound configuration set. \nSound selected: {sound_name}\nNOTE:\nIt works on all servers. You only "
            f"need to ste up it once!",
            ephemeral=True)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        user_id = member.id
        if user_id in self.settings:
            settings = self.settings[user_id]
            sound_name = settings["sound_name"]
            if sound_name and before.channel is None and after.channel:
                channel = after.channel
                if channel:
                    try:
                        voice_client = await channel.connect()
                        source = FFmpegPCMAudio(f"./sounds/{sound_name}.mp3")
                        voice_client.play(source)
                        while voice_client.is_playing():
                            await asyncio.sleep(0.1)
                        await voice_client.disconnect()
                    except Exception as e:
                        print(f"Error: {e}")

    @app_commands.command(name="sound_test", description='Test the sounds')
    async def sound_test(self, interaction: discord.Interaction, sound_name: str) -> None:
        await interaction.response.send_message(f"Playing: {sound_name}", ephemeral=True)
        try:
            channel = interaction.user.voice.channel
            voice_client = await channel.connect()
            source = FFmpegPCMAudio(f"./sounds/{sound_name}.mp3")
            voice_client.play(source)
            while voice_client.is_playing():
                await asyncio.sleep(0.1)
            await voice_client.disconnect()
        except Exception as e:
            print(f"Error: {e}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SOUND(bot))
