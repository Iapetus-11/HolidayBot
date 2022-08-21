import asyncio
from bot.holiday_bot import HolidayBot
from bot.config import load_config

from pydantic import parse_file_as

from bot.models.holiday import Holiday


async def main():
    config = load_config()
    holidays = parse_file_as(list[Holiday], "bot/data/holidays.json")

    bot = HolidayBot(config, holidays)

    async with bot:
        await bot.start()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
