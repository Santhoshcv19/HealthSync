from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import WorkoutForm, Workoutlogform, DateForm
from .models import Workout
import csv
import datetime
import pytz

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

def quiz(request):
    return render(request, "fitness/quiz.html")

def trainers(request):
    with open("C:/Users/Santhosh CV/Downloads/SIH_Fitness-project/fitness/templates/fitness/trainers.csv", "r") as f:
        r = csv.reader(f)
        next(f)
        trainers_data = []
        for i in r:
            trainers_data.append({
                'name': i[0],
                'specialization': i[1],
                'contact':i[2],
                'code': i[3]
            })
    return render(request, 'fitness/trainers.html', {'trainers_data': trainers_data})

def filter_trainers(request):
    with open("C:/Users/Santhosh CV/Downloads/SIH_Fitness-project/fitness/templates/fitness/trainers.csv", "r") as f:
        r = csv.reader(f)
        next(f)
        l = set()  # Set of specializations
        specific_trainers_data = []
        for i in r:
            if i[1] not in l:
                l.add(i[1])
        print("What are you looking for?")
        for idx, specialization in enumerate(l, start=1):
            print(f"{idx}) {specialization}")
        print("Enter your choice number \n")
        x = int(input())
        print("\n")
        if x <= len(l):
            spec = list(l)[x - 1]  # Convert set to list and get the specialization
            f.seek(0)
            next(f)
            for i in r:
                if i[1] == spec:
                    specific_trainers_data.append({
                        'name': i[0],
                        'code': i[3]
                    })
    return render(request, 'fitness/filter_trainers.html', {'specific_trainers_data': specific_trainers_data})

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


def workoutlog(request):
    if request.method == 'GET':
        return render(request, 'fitness/workoutlog.html', {'form': Workoutlogform()})
    else:
        try:
            form = Workoutlogform(request.POST)
            newlog = form.save(commit=False)
            newlog.user = request.user
            newlog.save()
            return redirect('log')
        except ValueError:
            return render(request, 'fitness/workoutlog.html', {'form': Workoutlogform(), 'error':'Bad Data Passed in'})
        

def log(request):
    date_form = DateForm(request.GET)

    selected_date = None
    workouts = []

    if date_form.is_valid():
        selected_date = date_form.cleaned_data['selected_date']
        workouts = Workout.objects.filter(added__date=selected_date, user=request.user)

    return render(request, 'fitness/log.html', {
        'date_form': date_form,
        'selected_date': selected_date,
        'workouts': workouts,
    })        





