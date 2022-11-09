from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=25)
    def __str__(self):
        return self.title


class Cuisine(models.Model):
    title = models.CharField(max_length=25)
    def __str__(self):
        return self.title


class Menu_Item(models.Model):
    title = models.CharField(max_length=25)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, null=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.title






