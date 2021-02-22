from django.contrib import admin
from .models import (Item, Order)
import logging


logger = logging.getLogger('django')


class OrderAdmin(admin.ModelAdmin):
    fields = ['items']
    list_display = ('user', 'date_created', 'purchased_items', 'total_price')

    def get_queryset(self, request):
        queryset = super(OrderAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            logger.debug("User is admin, showing all items")
            return queryset
        return queryset.filter(user=request.user)

    def save_model(self, request, obj: Order, form, change):
        logger.debug("Entering model save")
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
