from django.db import models

# Create your models here.

class Item(models.Model):
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField()
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://storage.googleapis.com/ds-builder-bucket/000_menu_placeholder.png')
    
    def __str__(self):
        return self.item_name

