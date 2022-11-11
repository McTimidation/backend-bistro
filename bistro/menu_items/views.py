from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Menu_Item, Location


def get_all_menus(request):
    data = list(Menu_Item.objects.values())
    return JsonResponse(data, safe=False)

def view_by_spice(request):
    data = list(Menu_Item.objects.values().order_by('-spice_level'))
    return JsonResponse(data, safe=False)

def view_locations(request):
    data = Location.objects.all()
    # .values() => Queryset [ dict ]
    # .all() => Queryset [ ModelInstances ]
    locations = []
    for l in data:
        locations.append({
            'name': l.title,
            'menu_items': [i.title for i in l.menu_items.all()] 
        })


    print(data)
    return JsonResponse(locations, safe=False)




