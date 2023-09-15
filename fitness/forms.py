from django import forms

class WorkoutForm(forms.Form):
    days = forms.ChoiceField(choices=[('select', 'Select'), ('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7')])
