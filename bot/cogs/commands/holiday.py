from discord.ext import commands
from discord import app_commands
import discord
import arrow

from bot.holiday_bot import HolidayBot
from bot.models.holiday import Holiday


class HolidayCommands(commands.Cog):
    def __init__(self, bot: HolidayBot):
        self.bot = bot

    @app_commands.command(name="holidays")
    async def get_holidays(self, inter: discord.Interaction):
        """Get today's holidays"""

        holidays = list[Holiday]()

        for h in self.bot.holidays:
            if h.at.date() == arrow.utcnow().date():
                holidays.append(h)

        if len(holidays) == 0:
            await inter.response.send_message("No holidays found for today :/")
            return

        embed = self.bot.default_embed()
        embed.title = "🎁 Today's Holidays 🎉"
        embed.description = "\n".join(
            [(f"• [{h.name}]({h.link})" if h.link else f"• {h.name}") for h in holidays]
        )
        embed.timestamp = arrow.utcnow().datetime

        await inter.response.send_message(embed=embed)


async def setup(bot: HolidayBot):
    await bot.add_cog(HolidayCommands(bot))
