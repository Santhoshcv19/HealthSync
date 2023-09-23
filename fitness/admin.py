from django.contrib import admin
from .models import MacroNutrients, Workout, Product, CartItem

admin.site.register(MacroNutrients)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('Workout_name', 'weight', 'sets', 'reps')

admin.site.register(Product)

admin.site.register(CartItem)