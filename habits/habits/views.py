from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from .forms import UserRegistrationForm, UserLoginForm
from .models import User, Habit
from datetime import *
import calendar

def index(request):
    context = {}
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            context = {"message": "Login Successful"}
            print("success")
            return redirect('habits')
        else:
            context = {"form": form, "message": "Invalid username or password"}
            print(form.errors)  # Print the form errors for debugging

    else:  # Handle GET request
        form = UserLoginForm()

    context['form'] = form  # Add form to context to render in template
    return render(request, 'index.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = UserRegistrationForm()
    return render(request, 'sign-up.html', {'form': form})

def habits(request):
    habits = Habit.objects.all().values()
    return render(request, 'habits.html', {'habits': habits})

def habit(request,id):
    today = datetime.today()
    habit = Habit.objects.get(habit_id=id)
    start = today - timedelta(days=today.weekday())
    print("dekjhk ",habit)
    days_week = [(start + timedelta(days=i), ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][i]) for i in range(7)]
    return render(request, "smoking.html",{"habit":habit, "days_week":[(start + timedelta(days=i)) for i in range(7)] ,"today":today,'days_week':days_week})