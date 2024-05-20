import asyncio

from classes import CurrencyRate
from func import int_one_arg_input, transform_data


async def main(view_days: int) -> None:

    rates = CurrencyRate()
    currency_rates = await rates.get_currency_rates(n_days=view_days)
    print(currency_rates)
    print("-----------------------")
    print(transform_data(currency_rates))


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(int_one_arg_input(1, 10)))