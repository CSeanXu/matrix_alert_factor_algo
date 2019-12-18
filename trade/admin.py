from django.contrib import admin

from .models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "exchange", "symbol", "price", "amount", "value", "trade_time", "created",)
    list_editable = ("exchange", "symbol",)

    list_filter = (
        ("symbol", admin.RelatedOnlyFieldListFilter),
    )
