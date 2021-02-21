from django.db import models
from django.db import transaction
from django.contrib.auth.models import User

from django.db.models import Sum
from django.utils import timezone
from website import mail


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.name} -- {self.price}€'


class Order(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    items = models.ManyToManyField(Item, related_name='items')

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        instance = super(Order, self).save(*args, **kwargs)
        transaction.on_commit(self.send_mail)
        return instance

    def send_mail(self):
        from .serializers import OrderSerializer
        serialized = OrderSerializer(self)
        mail.send_order(to_email=self.user.email, data=serialized.data)

    def total_price(self):
        """Return the total amount of the purchased items"""
        total = list(self.items.all().aggregate(Sum("price")).values())[0]
        return f'{total} €'

    def purchased_items(self):
        """Return names of purchased items"""
        return ', '.join(items.name for items in self.items.all())
