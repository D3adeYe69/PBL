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
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('habit_id', 'language_code')

    def __str__(self):
        return self.habit_name

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
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    progress_status = models.CharField(max_length=15, default='not started', choices=[
        ('not started', 'Not Started'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed')
    ])
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'habit', 'step')