from rest_framework import serializers
from menu.models import Category, Menu, Customer, Order, OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class MenuSerializer(serializers.ModelSerializer):
    group = CategorySerializer(read_only=True)
    group_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="group", write_only=True, required=False
    )

    class Meta:
        model = Menu
        fields = ["id", "name", "group", "group_id"]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), source="order", write_only=True
    )
    menu = MenuSerializer(read_only=True)
    menu_id = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.all(), source="menu", write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ["id", "order", "order_id", "menu", "menu_id", "qty"]

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "customer", "customer_id", "status", "created_at", "items"]
        read_only_fields = ["created_at"]
