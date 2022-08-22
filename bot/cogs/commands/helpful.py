from discord.ext import commands
from discord import app_commands
import discord
import arrow

from bot.holiday_bot import HolidayBot
from bot.models.holiday import Holiday


class HelpfulCommands(commands.Cog):
    def __init__(self, bot: HolidayBot):
        self.bot = bot

    @app_commands.command(name="invite")
    async def invite(self, inter: discord.Interaction):
        embed = self.bot.default_embed()
        embed.title = "Invite Holiday Bot"
        embed.description = "**[Click Here](https://discord.com/api/oauth2/authorize?client_id=1010973203767771186&permissions=2147747904&scope=bot%20applications.commands)**"

        await inter.response.send_message(embed=embed)


async def setup(bot: HolidayBot):
    await bot.add_cog(HelpfulCommands(bot))
