from django.contrib import admin
from .models import MacroNutrients, Workout, Product, CartItem, UploadedFile, FoodItem, CalorieIntake

admin.site.register(MacroNutrients)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('Workout_name', 'weight', 'sets', 'reps')

admin.site.register(Product)

admin.site.register(CartItem)

admin.site.register(UploadedFile)

admin.site.register(FoodItem)

admin.site.register(CalorieIntake)