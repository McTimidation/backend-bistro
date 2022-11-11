from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    title = models.CharField(max_length=25)
    def __str__(self):
        return self.title


class Cuisine(models.Model):
    title = models.CharField(max_length=25)
    def __str__(self):
        return self.title

class Location(models.Model):
    title = models.CharField(max_length=30)
    menu_items = models.ManyToManyField('Menu_Item')
    def __str__(self):
        return self.title




class Menu_Item(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=150, null=True, default=None)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, null=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=9.99)
    spice_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)

    def __str__(self):
        return str(self.id) + " " + self.title








