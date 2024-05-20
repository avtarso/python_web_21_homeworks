import asyncio

from telebot.async_telebot import AsyncTeleBot

from classes import CurrencyRate
from func import transform_data
from settings import BOT_TOKEN


WAIT_MESSAGE = "The request is being processed. Wait a few seconds"
TIME = 3600


if __name__ == "__main__":

    bot = AsyncTeleBot(BOT_TOKEN)

    @bot.message_handler(commands=['start'])
    async def start(message):

        await bot.send_message(message.chat.id, WAIT_MESSAGE)
        rates = CurrencyRate()
        currency_rates = await rates.get_currency_rates()
        await bot.send_message(message.chat.id, transform_data(currency_rates))

        while True:
            await asyncio.sleep(TIME)
            currency_rates = await rates.get_currency_rates()
            await bot.send_message(message.chat.id, transform_data(currency_rates))


    @bot.message_handler(commands=['ping'])
    async def ping_pong(message):

        await bot.send_message(message.chat.id, "pong")



    asyncio.run(bot.infinity_polling(allowed_updates=['message']))