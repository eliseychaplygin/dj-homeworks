from django.db import models

# Create your models here.
class Phone(models.Model):
    name_model = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    display_size = models.IntegerField()

class Samsung(models.Model):
    amount_sim_card = models.IntegerField()

class Apple(models.Model):
    touch_id = models.CharField(max_length=100)

