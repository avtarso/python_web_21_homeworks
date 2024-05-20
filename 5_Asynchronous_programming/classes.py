import aiohttp
from datetime import datetime, timedelta


class CurrencyRate:

    async def get_rate_on_date(self, date):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}') as response:
                return await response.json()


    async def fetch_rates_for_last_n_days(self, n):

        today = datetime.today()
        rates = []

        for i in range(n):
            date = (today - timedelta(days=i)).strftime('%d.%m.%Y')
            data = await self.get_rate_on_date(date)
            rates.append({date: data})

        return rates


    async def get_currency_rates(self, n_days=1, list_currencies=None):
        if list_currencies is None:
            list_currencies = ['USD', 'EUR'] # all possible currencies below
        
        raw_rates = await self.fetch_rates_for_last_n_days(n_days)

        formatted_rates = []

        for rate_data in raw_rates:

            date, data = rate_data.popitem()
            currencies = data['exchangeRate']

            currency_dict = {currency['currency']: currency for currency in currencies}
            rates = {}
            
            for cur in list_currencies:
                rate = currency_dict.get(cur)
                if rate:
                    rates[cur] = {
                            'sale': rate['saleRateNB'],
                            'purchase': rate['purchaseRateNB']
                        }

            formatted_rate = {date: rates}
            formatted_rates.append(formatted_rate)

        # print(currency_dict.keys())
        # dict_keys(['AUD', 'AZN', 'BYN', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'GEL', 'HUF', 'ILS', 'JPY', 'KZT', 'MDL', 'NOK', 'PLN', 'SEK', 'SGD', 'TMT', 'TRY', 'UAH', 'USD', 'UZS', 'XAU'])
        
        return formatted_rates
    

    async def get_possible_currencies(self):

        raw_rates = await self.fetch_rates_for_last_n_days(1)
       
        for rate_data in raw_rates:
            date, data = rate_data.popitem()
            currencies = data['exchangeRate']

            currency_dict = {currency['currency']: currency for currency in currencies}

        print(currency_dict)
        print(currency_dict.keys())
        # dict_keys(['AUD', 'AZN', 'BYN', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'GEL', 'HUF', 'ILS', 'JPY', 'KZT', 'MDL', 'NOK', 'PLN', 'SEK', 'SGD', 'TMT', 'TRY', 'UAH', 'USD', 'UZS', 'XAU'])

