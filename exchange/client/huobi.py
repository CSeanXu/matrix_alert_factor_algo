import aiohttp

from exchange.client import BaseClient


class Huobi(BaseClient):

    async def ticks(self, symbol):
        symbol_str = "".join([symbol.base.lower(), symbol.quote.lower()])
        url = "https://api.huobi.pro/market/history/trade?symbol={}&size=2000".format(symbol_str)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                return await r.json(content_type=None)
