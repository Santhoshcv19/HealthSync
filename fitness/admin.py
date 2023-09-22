from django.contrib import admin
from .models import MacroNutrients, Workout

admin.site.register(MacroNutrients)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('Workout_name', 'weight', 'sets', 'reps')