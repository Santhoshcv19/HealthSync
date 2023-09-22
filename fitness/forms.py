from django import forms
from django.forms import ModelForm
from .models import Workout

class WorkoutForm(forms.Form):
    days = forms.ChoiceField(choices=[('select', 'Select'), ('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7')])

class Workoutlogform(ModelForm):
    class Meta:
        model = Workout
        fields = ['Workout_name', 'weight', 'sets', 'reps']

class DateForm(forms.Form):
    selected_date = forms.DateField(
        label='Select a Date',
        widget=forms.TextInput(attrs={'type': 'date'}),
    )
