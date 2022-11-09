from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Menu_Item


def get_all_menus(request):
    items = list(Menu_Item.objects.values())
    print(items)
    return JsonResponse({'data': items})


