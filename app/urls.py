from django.contrib import admin
from django.urls import path, include
from menu.views import ShowMenuView

from rest_framework.routers import DefaultRouter
from menu.api import (
    CategoryViewSet, MenuViewSet, CustomerViewSet, OrderViewSet, OrderItemViewSet
)

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("menu", MenuViewSet, basename="menu")
router.register("customers", CustomerViewSet, basename="customers")
router.register("orders", OrderViewSet, basename="orders")
router.register("order-items", OrderItemViewSet, basename="order-items")

urlpatterns = [
    path("", ShowMenuView.as_view()),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
