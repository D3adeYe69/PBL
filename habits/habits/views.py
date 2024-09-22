from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from .forms import UserRegistrationForm, UserLoginForm
from .models import User

def index(request):
    context = {}
    if request.method == 'GET':
        form = UserLoginForm(request.GET)
        if form.is_valid():
            context = {"message": "Login Successful"}
            print("success")
            return render(request, 'habits.html', context)
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
    return render(request, "habits.html")

def smoking(request):
    return render(request, "smoking.html")