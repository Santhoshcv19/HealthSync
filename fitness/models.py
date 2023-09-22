from django.db import models
from django.contrib.auth.models import User

class MacroNutrients(models.Model):
    food_name = models.CharField(max_length=100)
    carbohydrates = models.CharField(max_length=100)
    protein = models.CharField(max_length=100)
    fats = models.CharField(max_length=100)

class Workout(models.Model):
    Workout_name = models.CharField(max_length=100)
    weight = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    added = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Workout_name