from django.contrib import admin
from .models import User, Language, Habit, Step, HabStep, UserProgress

# Register your models here.
admin.site.register(User)
admin.site.register(Language)
admin.site.register(Habit)
admin.site.register(Step)
admin.site.register(HabStep)
admin.site.register(UserProgress)