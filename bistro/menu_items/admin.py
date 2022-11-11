from django.contrib import admin
from .models import Menu_Item, Location

class MenuAdmin(admin.ModelAdmin):
    pass
admin.site.register(Menu_Item, MenuAdmin)

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location, MenuAdmin)
