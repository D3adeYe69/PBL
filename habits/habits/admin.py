from django.contrib import admin
from .models import User, Language, Habit, Step, HabStep, UserProgress,UserTask

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email')  # Customize as needed

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language_code', 'language_name')  # Customize as needed

class HabitAdmin(admin.ModelAdmin):
    list_display = ('habit_id', 'habit_name', 'habit_type', 'language_code', 'gradient_color_start', 'gradient_color_end')

class StepAdmin(admin.ModelAdmin):
    list_display = ('step_id', 'language_code', 'description')  # Show the ID

class HabStepAdmin(admin.ModelAdmin):
    list_display = ('get_habit_id', 'get_step_id', 'step_order')
    ordering = ('step__step_id', 'habit__habit_id')  # Order by step_id and habit_id

    def get_habit_id(self, obj):
        return obj.habit.habit_id
    get_habit_id.admin_order_field = 'habit'  # Allows sorting by habit_id
    get_habit_id.short_description = 'Habit ID'  # Column title in admin

    def get_step_id(self, obj):
        return obj.step.step_id
    get_step_id.admin_order_field = 'step'  # Allows sorting by step_id
    get_step_id.short_description = 'Step ID'  # Column title in admin

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('habit', 'step')  # Join with Habit and Step tables


# Register your models here with their custom admin classes
admin.site.register(User, UserAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Habit, HabitAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(HabStep, HabStepAdmin)
admin.site.register(UserProgress)
admin.site.register(UserTask)
