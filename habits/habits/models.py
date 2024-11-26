from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Language(models.Model):
    language_code = models.CharField(max_length=2, primary_key=True)
    language_name = models.CharField(max_length=50)

    def __str__(self):
        return self.language_name
    
class Habit(models.Model):
    habit_id = models.AutoField(primary_key=True)
    language_code = models.ForeignKey(Language, on_delete=models.RESTRICT)
    habit_name = models.CharField(max_length=100)
    habit_type = models.CharField(max_length=4, choices=[('good', 'Good'), ('bad', 'Bad')])
    description = models.TextField(blank=True)
    gradient_color_start = models.CharField(max_length=7, blank=True, help_text="Hex code for the gradient start color")
    gradient_color_end = models.CharField(max_length=7, blank=True, help_text="Hex code for the gradient end color")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('habit_id', 'language_code')

    def __str__(self):
        return self.habit_name

    def save(self, *args, **kwargs):
        if self.habit_type == 'good' and not self.gradient_color_start and not self.gradient_color_end:
            self.gradient_color_start = '#FEC6EE'  # Pink gradient start
            self.gradient_color_end = '#F076CD'    # Pink gradient end
        elif self.habit_type == 'bad' and not self.gradient_color_start and not self.gradient_color_end:
            self.gradient_color_start = '#C22165'  # Red gradient start
            self.gradient_color_end = '#19274A'    # Blue gradient end
        super(Habit, self).save(*args, **kwargs)

class Step(models.Model):
    step_id = models.AutoField(primary_key=True)
    language_code = models.ForeignKey(Language, on_delete=models.RESTRICT)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('step_id', 'language_code')

    def __str__(self):
        return self.description

class HabStep(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    step_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('habit', 'step', 'step_order')

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    current_day = models.IntegerField(default=1) 
    completed_tasks_today = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def reset_tasks_for_next_day(self):
        
        self.current_day += 1
        self.completed_tasks_today = 0
        self.save()

    def check_all_tasks_completed(self):
   
        steps_for_today = HabStep.objects.filter(habit=self.habit, step_order=self.current_day)
        completed_steps = UserTask.objects.filter(
            user_progress=self,
            task_description__in=[step.step.description for step in steps_for_today],
            task_completed=True
        ).count()

        if completed_steps == steps_for_today.count():
            self.reset_tasks_for_next_day()


    def __str__(self):
        return f"{self.user.username} - {self.habit.habit_name} - Day {self.current_day}"
    
    def get_days_active(self):
        """Returns the number of unique days where tasks were completed"""
        from django.db.models import Count
        from django.db.models.functions import TruncDate
    
        return UserTask.objects.filter(
          user_progress=self,
         task_completed=True
     ).annotate(
            date=TruncDate('created_at')
     ).values('date').distinct().count()

    def get_total_steps_completed(self):
        """Returns the total number of completed tasks"""
        return UserTask.objects.filter(
            user_progress=self,
            task_completed=True
        ).count()

    def get_completion_history(self):
        """Returns a dictionary of dates and number of tasks completed"""
        history = {}
        completed_tasks = UserTask.objects.filter(
            user_progress=self,
            task_completed=True
        ).order_by('created_at')
        
        for task in completed_tasks:
            date = task.created_at.date()
            if date in history:
                history[date] += 1
            else:
                history[date] = 1
        
        return history

    class Meta:
        unique_together = ('user', 'habit')

class UserTask(models.Model):
    user_progress = models.ForeignKey(UserProgress, on_delete=models.CASCADE)
    task_completed = models.BooleanField(default=False)
    task_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Task for {self.user_progress.user.username} - Day {self.user_progress.current_day}"
    
    
    
    
    
    
    

