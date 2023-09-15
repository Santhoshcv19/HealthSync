from django.shortcuts import render

def home(request):
    return render(request, "fitness/home.html")

def workoutlogging(request):
    return render(request, "fitness/workoutlogging.html")

