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
from django.http import JsonResponse
from django.views.decorators.http import require_POST

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
            # Create initial progress for each habit
            for habit in Habit.objects.all():
                # Just create progress for day 1 initially
                UserProgress.objects.create(
                    user=user,
                    habit=habit,
                    current_day=1,
                    completed_tasks_today=0
                )
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
    
    # Add the deletion handling
    if request.method == 'POST':
        try:
            user = get_object_or_404(User, user_id=user_id)
            user.delete()
            # Clear session
            request.session.flush()
            return redirect('/')
        except Exception as e:
            return render(request, 'account.html', {
                "user_id": user_id,
                "error_message": "Failed to delete account. Please try again."
            })
            
    return render(request, 'account.html', {"user_id": user_id})

def support(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    return render(request, 'support.html',{"user_id": user_id})

def help_center(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    return render(request, 'help_center.html',{"user_id": user_id})

def profile_setup(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    return render(request, 'profile_setup.html',{"user_id": user_id})

def edit_password(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    return render(request, 'edit_password.html',{"user_id": user_id})

def troubleshooting(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    return render(request, 'troubleshooting.html',{"user_id": user_id})



def delete_account(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if not user_id:
            return JsonResponse({'error': 'Not logged in'}, status=401)
        
        try:
            user = User.objects.get(user_id=user_id)
            # Delete all related data (Django will handle this automatically due to on_delete=CASCADE)
            user.delete()
            # Clear the session
            request.session.flush()
            return JsonResponse({'message': 'Account deleted successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def habit_info(request, id):
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
    
    # Get all completed tasks for this habit
    completed_tasks = UserTask.objects.filter(
        user_progress=user_progress,
        task_completed=True
    ).order_by('-created_at')  # Most recent first
    
    # Debug prints
    print("Completed tasks:", completed_tasks.count())
    print("Task dates:", [task.created_at.date() for task in completed_tasks])
    
    days_active = completed_tasks.dates('created_at', 'day').distinct().count()
    print("Days active:", days_active)
    
    context = {
        'habit': habit,
        'habit_info': habit.habit_name,
        'days_active': days_active,
        'total_steps': completed_tasks.count(),
        'user_progress': user_progress,
        'completed_tasks': completed_tasks,
    }
    
    return render(request, 'habit_info.html', context)


@require_POST
def complete_step(request, habit_id, step_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'success': False, 'error': 'Not logged in'}, status=401)
    
    try:
        user = User.objects.get(user_id=user_id)
        habit = Habit.objects.get(habit_id=habit_id)
        step = HabStep.objects.get(step=step_id, habit=habit)
        
        user_progress = UserProgress.objects.get(user=user, habit=habit)
        
        # Debug print
        print(f"Creating/updating task for user {user.username}, habit {habit.habit_name}, step {step.step.description}")
        
        user_task, created = UserTask.objects.get_or_create(
            user_progress=user_progress,
            task_description=step.step.description,
            defaults={
                'task_completed': True,
                'created_at': timezone.now()  # Make sure we're setting the date
            }
        )
        
        if not created:
            user_task.task_completed = not user_task.task_completed
            user_task.save()
            
        print(f"Task {'created' if created else 'updated'} - completed: {user_task.task_completed}")
        
        return JsonResponse({'success': True})
    except Exception as e:
        print(f"Error in complete_step: {str(e)}")
        return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
    
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from .models import User
from .tokens import password_reset_token
from django.views import View

class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'reset_password.html')
    
    def post(self, request):
        email = request.POST.get('email')
        if not email:
            return render(request, 'reset_pass.html', {'error': 'Please provide an email'})
            
        user = User.objects.filter(email=email).first()
        if user:
            current_site = get_current_site(request)
            subject = 'Password Reset Request'
            
            # Create reset token
            uid = urlsafe_base64_encode(force_bytes(user.user_id))
            token = password_reset_token.make_token(user)
            
            # Create email content
            email_context = {
                'user': user,
                'domain': current_site.domain,
                'uid': uid,
                'token': token,
                'protocol': 'https' if request.is_secure() else 'http'
            }
            
            email_body = render_to_string('password_reset_email.html', email_context)
            
            # Send email
            try:
                send_mail(
                    subject,
                    email_body,
                    'h4bitquest@gmail.com',
                    [user.email],
                    fail_silently=False,
                )
                print(f"Password reset email sent to {email}")
                return redirect('password_reset_sent')
            except Exception as e:
                print(f"Error sending email: {str(e)}")
                return render(request, 'reset_pass.html', {'error': 'Error sending email'})
        
        return redirect('password_reset_sent')  # Redirect even if email not found for security

class ResetPasswordConfirmView(View):
    def get(self, request, uidb64, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(user_id=user_id)
            
            if password_reset_token.check_token(user, token):
                return render(request, 'password_reset_form.html', {
                    'uidb64': uidb64,
                    'token': token
                })
            else:
                return render(request, 'password_reset_form.html', {'error': 'Invalid token'})
                
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return render(request, 'password_reset_form.html', {'error': 'Invalid reset link'})
    
    def post(self, request, uidb64, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(user_id=user_id)
            
            if password_reset_token.check_token(user, token):
                password = request.POST.get('new_password1')
                confirm_password = request.POST.get('new_password2')
                
                if password == confirm_password:
                    from django.contrib.auth.hashers import make_password
                    user.password = make_password(password)
                    user.save()
                    return redirect('password_reset_complete')
                else:
                    return render(request, 'password_reset_form.html', {
                        'error': 'Passwords do not match',
                        'uidb64': uidb64,
                        'token': token
                    })
            
            return render(request, 'password_reset_form.html', {'error': 'Invalid token'})
            
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return render(request, 'password_reset_form.html', {'error': 'Invalid reset link'})

def password_reset_sent(request):
    return render(request, 'password_reset_sent.html')

def password_reset_complete(request):
    return render(request, 'password_reset_done.html') 

    
    
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO
from datetime import datetime
from .models import User, UserProgress, UserTask, Habit

def download_history_pdf(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('index')
    
    try:
        # Get user and their habits
        user = User.objects.get(user_id=user_id)
        user_progress_list = UserProgress.objects.filter(user=user)
        
        # Create PDF buffer
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            title="Your Habits History"
        )
        
        # PDF Styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.HexColor('#c22165'),
            alignment=1  # Center alignment
        )
        
        habit_style = ParagraphStyle(
            'HabitTitle',
            parent=styles['Heading2'],
            fontSize=18,
            textColor=colors.HexColor('#333333'),
            spaceBefore=20,
            spaceAfter=10
        )

        # Create custom style for wrapped text
        cell_style = ParagraphStyle(
            'CellStyle',
            parent=styles['Normal'],
            fontSize=10,
            leading=12,  # Line spacing
            spaceBefore=6,
            spaceAfter=6,
            wordWrap='CJK'  # Enable word wrapping
        )
        
        # PDF Elements
        elements = []
        
        # Add main title
        elements.append(Paragraph("Your Habits History", title_style))
        elements.append(Spacer(1, 30))
        
        # For each habit
        for progress in user_progress_list:
            # Add habit title
            elements.append(Paragraph(progress.habit.habit_name, habit_style))
            
            # Get completed tasks for this habit
            completed_tasks = UserTask.objects.filter(
                user_progress=progress,
                task_completed=True
            ).order_by('-created_at')
            
            if completed_tasks.exists():
                # Create table data
                data = [['Step Completed', 'Date']]  # Header row
                for task in completed_tasks:
                    # Create paragraph objects for both columns
                    wrapped_description = Paragraph(task.task_description, cell_style)
                    date_text = Paragraph(task.created_at.strftime('%B %d, %Y'), cell_style)
                    data.append([wrapped_description, date_text])
                
                # Create and style table with adjusted dimensions
                table = Table(data, colWidths=[350, 150], rowHeights=None)
                table.setStyle(TableStyle([
                    # Header style
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FEC6EE')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#333333')),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 12),
                    
                    # Content style
                    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 10),
                    
                    # Alignment and spacing
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),  # Important for text wrapping
                    ('LEFTPADDING', (0, 0), (-1, -1), 12),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 12),
                    ('TOPPADDING', (0, 0), (-1, -1), 8),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                    
                    # Grid style
                    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#FEC6EE')),
                ]))
                
                elements.append(table)
            else:
                elements.append(
                    Paragraph("No steps completed yet for this habit", styles['Normal'])
                )
            
            elements.append(Spacer(1, 20))
        
        # Build PDF
        doc.build(elements)
        
        # Create response
        buffer.seek(0)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="habits_history_{datetime.now().strftime("%Y%m%d")}.pdf"'
        response.write(buffer.getvalue())
        
        return response
        
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return redirect('index')
    
    
    
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import NotificationSettings, User
import json

def notifications(request):
    # Get the user from your User model
    try:
        user = User.objects.get(user_id=request.session.get('user_id'))
        settings, created = NotificationSettings.objects.get_or_create(user=user)
        
        context = {
            'show_notifications': settings.show_notifications,
            'weekly_summary': settings.weekly_summary,
        }
    except User.DoesNotExist:
        context = {
            'show_notifications': False,
            'weekly_summary': False,
        }
    
    return render(request, 'notifications.html', context)

@csrf_exempt
def update_notification_settings(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            setting_type = data.get('type')
            enabled = data.get('enabled')
            
            # Get the user from your User model
            user = User.objects.get(user_id=request.session.get('user_id'))
            settings, created = NotificationSettings.objects.get_or_create(user=user)
            
            if setting_type == 'show_notifications':
                settings.show_notifications = enabled
            elif setting_type == 'weekly_summary':
                settings.weekly_summary = enabled
            
            settings.save()
            
            # Send test notification if enabling notifications
            if setting_type == 'show_notifications' and enabled:
                return JsonResponse({
                    'status': 'success',
                    'showTestNotification': True,
                    'notificationTitle': 'Habit Tracker',
                    'notificationBody': f'Hi {user.username}! Notifications are now enabled for your habits.'
                })
            
            return JsonResponse({'status': 'success'})
            
        except User.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'User not found'
            }, status=404)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

from django.utils import timezone
from .models import NotificationLog

def log_notification(user, title, message):
    return NotificationLog.objects.create(
        user=user,
        title=title,
        message=message
    )

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def update_notification_settings(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            setting_type = data.get('type')
            enabled = data.get('enabled')
            
            # Get user settings
            if setting_type == 'show_notifications':
                return JsonResponse({
                    'status': 'success',
                    'showTestNotification': True,
                    'notificationTitle': 'HabitQuest',
                    'notificationBody': 'Welcome to HabitQuest! You will receive reminders every 4 hours to check your habits.'
                })
            
            return JsonResponse({'status': 'success'})
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def get_notification_history(request):
    try:
        user = User.objects.get(user_id=request.session.get('user_id'))
        logs = NotificationLog.objects.filter(user=user).order_by('-sent_at')
        
        return JsonResponse({
            'status': 'success',
            'notifications': [
                {
                    'title': log.title,
                    'message': log.message,
                    'sent_at': log.sent_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'was_clicked': log.was_clicked
                }
                for log in logs
            ]
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)