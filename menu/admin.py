from django.contrib import admin
from menu.models import Category, Menu, Customer, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "group"]
    list_filter = ["group"]
    search_fields = ["name"]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "status", "created_at"]
    list_filter = ["status", "created_at"]
    inlines = [OrderItemInline]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone"]
    search_fields = ["name", "phone"]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "menu", "qty"]
    list_filter = ["order", "menu"]
