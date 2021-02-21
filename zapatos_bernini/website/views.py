import rest_framework.mixins as mixins
from rest_framework.viewsets import GenericViewSet

from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """Return all the Articles"""
    serializer_class = ItemSerializer
    queryset = Item.objects.all().order_by("name")
