from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from .forms import UserRegistrationForm, UserLoginForm
from .models import User, Habit, Step, UserProgress
from datetime import *
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Habit, Step, HabStep,UserTask,UserProgress
from datetime import *
from django.utils import timezone

def index(request):
    context = {}
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username).first()
            if user and check_password(password, user.password):
                request.session['user_id'] = user.user_id
                return redirect('habits')
            else:
                context = {"form": form, "message": "Invalid username or password"}
        else:
            context = {"form": form, "message": "Invalid username or password"}
    else:
        form = UserLoginForm()
    context['form'] = form
    return render(request, 'index.html', context)

def sign_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            for habit in Habit.objects.all():
                for day in range(1, 2):
                    for task in Step.objects.filter(...):
                        UserProgress.objects.create(user=user, habit=habit, step=task, curent_day=day)
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'sign-up.html', {'form': form})

def habits(request):
    habits = Habit.objects.all().values()
    return render(request, 'habits.html', {'habits': habits})


def habit(request, id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    user = get_object_or_404(User, user_id=user_id)
    habit = get_object_or_404(Habit, habit_id=id)

    user_progress = UserProgress.objects.filter(user=user, habit=habit).first()
    if not user_progress:
        user_progress = UserProgress.objects.create(
            user=user,
            habit=habit,
            current_day=1,
            completed_tasks_today=0
        )

    steps_for_today = HabStep.objects.filter(habit=habit, step_order=user_progress.current_day)

   
    current_time = timezone.now()
    print(current_time.hour+2)
    if current_time.hour+2 == 24 and current_time.minute == 0:
        user_progress.check_all_tasks_completed() 

    if request.method == 'POST':

        for step in steps_for_today:
            step_id = request.POST.get(f'step_{step.id}')

            user_task, created = UserTask.objects.get_or_create(
                user_progress=user_progress,
                task_description=step.step.description
            )

            if step_id == 'on':  
                user_task.task_completed = True
            elif step_id == 'off':  
                user_task.task_completed = False

            user_task.save()


            print(f"task description: {user_task.task_description} task completed: {user_task.task_completed}")

       

    steps_for_today = HabStep.objects.filter(habit=habit, step_order=user_progress.current_day)
    today = timezone.now()
    start = today - timedelta(days=today.weekday())
    days_week = [(start + timedelta(days=i), ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][i]) for i in range(7)]
   
    return render(request, "smoking.html", {
        "habit": habit,
        "days_week": days_week,
        "today": today,
        "user_progress": user_progress,
        "steps_for_today": steps_for_today
    })



def assign_steps_to_habit(request):
    habit_id = 25
    start_step_id = 1
    end_step_id = 5
    habit = get_object_or_404(Habit, habit_id=habit_id)
    for step_id in range(start_step_id, end_step_id + 1):
        step = get_object_or_404(Step, step_id=step_id)
        HabStep.objects.create(habit=habit, step=step, step_order=step_id)
    return HttpResponse(f'Successfully assigned steps {start_step_id} to {end_step_id} to habit "{habit.habit_name}".')

def settings(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    return render(request, 'settings.html',{"user_id": user_id})

def problem(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    return render(request, 'problem.html',{"user_id": user_id})

def notifications(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    return render(request, 'notifications.html',{"user_id": user_id})

def account(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    return render(request, 'account.html',{"user_id": user_id})

def support(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    return render(request, 'support.html',{"user_id": user_id})