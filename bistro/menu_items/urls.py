from django.urls import path

from . import views

urlpatterns = [
    path('menu_items/', views.get_all_menus),
    path('view_by_spice/', views.view_by_spice),
    path('view_locations/', views.view_locations)
]