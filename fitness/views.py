from django.shortcuts import render, redirect,  get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import WorkoutForm, Workoutlogform, DateForm
from .models import Workout, Product, CartItem
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
    products = Product.objects.all()
    return render(request, 'fitness/supplement.html', {'products': products})

def cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'fitness/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('supplement')

def remove_from_cart(request, cart_item_id):
    try:
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass  
    return redirect('cart')

def remove_all(request, cart_item_id):
    try:
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('cart')
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





