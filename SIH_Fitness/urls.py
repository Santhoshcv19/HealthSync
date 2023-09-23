"""
URL configuration for SIH_Fitness project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from fitness import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('workoutlogging', views.workoutlogging, name='workoutlogging'),
    path('nutrient',views.nutrient, name='nutrient'),
    path('supplement',views.supplement, name='supplement'),
    path('cart', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_all/<int:cart_item_id>/', views.remove_all, name='remove_all'),
    path('bodyfat',views.bodyfat, name='bodyfat'),
    path('tips',views.tips, name='tips'),
    path('mental',views.mental, name='mental'),
    path('quiz',views.quiz, name='quiz'),
    path('trainers', views.trainers, name='trainers'),
    path('location',views.location, name='location'),
    path('routine', views.routine, name='routine'),
    path('filter_trainers', views.filter_trainers, name='filter_trainers'),
    path('workoutlog', views.workoutlog, name='workoutlog'),
    path('log', views.log, name='log'),
    path('cmgmt', views.cmgmt, name='cmgmt'),
    path('tt', views.tt, name='tt'),
    #Auth
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
