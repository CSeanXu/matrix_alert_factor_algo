from enum import Enum

from django.db import models


class SymbolFormatEnum(Enum):
    LOWERCASE = "LOWERCASE"  # btcusdt
    UPPERCASE = "UPPERCASE"  # BTCUSDT

    LOWER_HYPHEN = "LOWER_HYPHEN"  # btc-usdt
    UPPER_HYPHEN = "UPPER_HYPHEN"  # BTC-USDT

    LOWER_UNDERSCORE = "LOWER_UNDERSCORE"  # btc_usdt
    UPPER_UNDERSCORE = "UPPER_UNDERSCORE"  # BTC_USDT


class Exchange(models.Model):
    name = models.CharField(max_length=2048)
    description = models.CharField(max_length=10 ** 5, blank=True)
    url = models.URLField(blank=True)
    symbol_format = models.CharField(
        max_length=128,
        choices=((state.name, state.value) for state in SymbolFormatEnum),
        default=SymbolFormatEnum.UPPER_UNDERSCORE.name
    )

    def __str__(self):
        return f"<Exchange: {self.name}>"


class Symbol(models.Model):
    base = models.CharField(max_length=1024)
    quote = models.CharField(max_length=1024)

    def __str__(self):
        return f"<Symbol: {self.base}_{self.quote}>"
