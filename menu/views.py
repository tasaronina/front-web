from typing import Any
from django.views.generic import TemplateView
from .models import Menu

class ShowMenuView(TemplateView):
    template_name = "menu/show_menu.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["menu"] = Menu.objects.all()   # имя переменной совпадает с шаблоном
        return context
