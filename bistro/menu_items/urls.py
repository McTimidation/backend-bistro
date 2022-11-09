from django.urls import path

from . import views

urlpatterns = [
    path('menu_items/', views.get_all_menus)
]