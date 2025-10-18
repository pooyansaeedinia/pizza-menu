from django.shortcuts import render
from rest_framework.generics import ListAPIView

from menu.models import MenuItem
from menu.serializer import MenuItemSerializer


# Create your views here.

class PizzaListView(ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

