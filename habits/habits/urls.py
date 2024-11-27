"""
URL configuration for habits project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import assign_steps_to_habit
from django.contrib.auth import views as auth_views
from .views import (
    ResetPasswordView, 
    ResetPasswordConfirmView,
    password_reset_sent,
    password_reset_complete
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'log-in'),
    path('sign-up', views.sign_up, name = 'sign-up'),
    path('habits', views.habits, name = 'habits'),
    path('habit/<int:id>/', views.habit, name='habit'),
    path('habit/<int:id>/info', views.habit_info, name='habit_info'),
    path('assign-steps/', assign_steps_to_habit, name='assign_steps'),
    path('settings', views.settings, name="settings"),
    path('problem', views.problem, name="problem"),
    path('notifications', views.notifications, name="notifications"),
    path('account', views.account, name="account"),
    path('support', views.support, name="support"),
    path('help_center', views.help_center, name="help_center"),
    path('profile_setup', views.profile_setup, name='profile_setup'),
    path('edit_password', views.edit_password, name='edit_password'),
    path('troubleshooting', views.troubleshooting, name='troubleshooting'),
    # path('report/problem', views.report_problem, name='report_problem'),
    path('api/delete-account', views.delete_account, name='delete_account'),
    
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('password_reset_sent/', password_reset_sent, name='password_reset_sent'),
    path('reset/<str:uidb64>/<str:token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', password_reset_complete, name='password_reset_complete'),
    path('download-history/', views.download_history_pdf, name='download_history'),
    path('habit/<int:habit_id>/info/', views.habit_info, name='habit_info'),
    path('habit/<int:habit_id>/step/<int:step_id>/complete/', views.complete_step, name='complete_step'),
    
  path('notifications/', views.notifications, name='notifications'),
path('update-notification-settings/', views.update_notification_settings, name='update_notification_settings'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)