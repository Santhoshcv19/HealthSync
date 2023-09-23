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
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    type = models.CharField(max_length=100, default='Protein')

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories_per_100g = models.PositiveIntegerField()  # Calories per 100 grams
    unit_name = models.CharField(max_length=20, default='grams')

class CalorieIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=100)