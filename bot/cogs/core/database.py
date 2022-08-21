from discord.ext import commands

from bot.holiday_bot import HolidayBot


class Database(commands.Cog):
    def __init__(self, bot: HolidayBot):
        self.bot = bot


async def setup(bot: HolidayBot):
    await bot.add_cog(Database(bot))
