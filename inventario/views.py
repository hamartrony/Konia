from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from .models import Item
from .serializer import ItemSerializer


class ItemsView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
