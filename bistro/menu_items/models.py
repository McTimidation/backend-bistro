from django.db import models


class Menu_Item(models.Model):
    title = models.CharField(max_length=25)
    cuisine = models.ForeignKey('Cuisine', on_delete=models.CASCADE, default=None)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None)


class Category(models.Model):
    title = models.CharField(max_length=25)


class Cuisine(models.Model):
    title = models.CharField(max_length=25)


