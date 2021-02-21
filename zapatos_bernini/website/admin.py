from django.contrib import admin
from .models import (Item, Order)


class OrderAdmin(admin.ModelAdmin):
    fields = ['items']
    list_display = ('user', 'date_created', 'purchased_items', 'total_price')

    def get_queryset(self, request):
        queryset = super(OrderAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(user=request.user)

    def save_model(self, request, obj: Order, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
