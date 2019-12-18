import asyncio
from datetime import datetime
from decimal import Decimal

from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.module_loading import import_string

from exchange.models import Exchange, Symbol
from trade.models import Trade


def ts_to_dt(ts):
    tz = timezone.get_default_timezone()

    dt = datetime.fromtimestamp(ts)
    dt = timezone.make_aware(dt, tz)
    return dt


async def main(client, symbol, exchange, arg):
    ticks = await client.ticks(symbol)
    _data = []
    for d in ticks["data"]:
        _data.extend(d["data"])

    print(len(_data))

    _trade_objs = []

    for trade in _data:
        _price = Decimal(trade["price"])
        _amount = Decimal(trade["amount"])

        _trade_objs.append(Trade(
            exchange=exchange,
            symbol=symbol,
            trade_time=ts_to_dt(trade["ts"] / 1000),
            price=_price,
            amount=_amount,
            value=_price * _amount,
        ))
    arg["arg"] = _trade_objs


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--base', required=True, type=str)
        parser.add_argument('--quote', required=True, type=str)
        parser.add_argument('--ex', required=True, type=str)

    def handle(self, *args, **options):
        str_base = options["base"].upper()
        str_quote = options["quote"].upper()
        str_ex = options["ex"]

        try:
            symbol = Symbol.objects.get(
                base__iexact=str_base,
                quote__iexact=str_quote,
            )
            ex = Exchange.objects.get(name__iexact=str_ex)

        except Symbol.DoesNotExist:
            self.stdout.write(self.style.ERROR("Symbol Does Not Exist. ({}/{})".format(str_base, str_quote)))
            if_create = input("Create? [y/N]")

            if if_create == "y":
                self.stdout.write(self.style.NOTICE("Creating..."))

                symbol = Symbol.objects.create(
                    base=str_base,
                    quote=str_quote,
                )

                self.stdout.write(self.style.NOTICE("Created Symbol [{}]".format(symbol)))
        except Exchange.DoesNotExist:
            self.stdout.write(self.style.ERROR("Exchange Does Not Exist. ({})".format(str_ex)))
        else:
            self.stdout.write(self.style.NOTICE(f"Start collecting trade of [{symbol} ON {ex}]"))

            client_class = import_string(f"exchange.client.{ex.name.lower()}.{ex.name}")

            client = client_class()

            loop = asyncio.get_event_loop()

            _arg = {
                "arg": None
            }
            loop.run_until_complete(main(client, symbol, ex, _arg))

            Trade.objects.bulk_create(_arg["arg"])
