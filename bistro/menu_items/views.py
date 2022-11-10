from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Menu_Item


def get_all_menus(request):
    data = list(Menu_Item.objects.values())
    return JsonResponse(data, safe=False)


