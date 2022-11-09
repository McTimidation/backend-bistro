from django.db import models

class Menu_Item(models.Model):
    title = models.CharField(max_length=25)
    
