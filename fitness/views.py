from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import WorkoutForm

def home(request):
    return render(request, "fitness/home.html")

def workoutlogging(request):
    return render(request, "fitness/workoutlogging.html")

def routine(request):
    return render(request, "fitness/routine.html")

def nutrient(request):
    return render(request, "fitness/nutrient.html")

def supplement(request):
    return render(request, "fitness/supplement.html")

def bodyfat(request):
    return render(request, "fitness/bodyfat.html")

def tips(request):
    return render(request, "fitness/tips.html")

def mental(request):
    return render(request, "fitness/mental.html")

def ctrainer(request):
    return render(request, "fitness/ctrainer.html")

def location(request):
    return render(request, "fitness/location.html")

def workoutlogging(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            selected_day = form.cleaned_data['days']
            return render(request, 'fitness/workoutlogging.html', {'form': form, 'selected_day': selected_day})
    else:
        form = WorkoutForm()
    
    return render(request, 'fitness/workoutlogging.html', {'form': form})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'




