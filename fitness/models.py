from django.db import models

class MacroNutrients(models.Model):
    food_name = models.CharField(max_length=100)
    carbohydrates = models.CharField(max_length=100)
    protein = models.CharField(max_length=100)
    fats = models.CharField(max_length=100)
