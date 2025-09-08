from rest_framework.viewsets import ModelViewSet
from menu.models import Category, Menu, Customer, Order, OrderItem
from menu.serializers import (
    CategorySerializer, MenuSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer
)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all().select_related("group")
    serializer_class = MenuSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().select_related("customer").prefetch_related("items__menu")
    serializer_class = OrderSerializer

class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all().select_related("order", "menu", "menu__group")
    serializer_class = OrderItemSerializer
