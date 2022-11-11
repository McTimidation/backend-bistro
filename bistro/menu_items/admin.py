from django.contrib import admin
from .models import Menu_Item

class MenuAdmin(admin.ModelAdmin):
    pass
admin.site.register(Menu_Item, MenuAdmin)
