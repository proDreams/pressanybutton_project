import asyncio

from aiogram import Bot, Dispatcher


async def start():
    bot = Bot(token="ваш_токен")

    dp = Dispatcher()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
