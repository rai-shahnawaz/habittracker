from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    available = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Habit(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='habit_profile')
    name = models.CharField(max_length=100)
    description = models.TextField()
    available = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Goal(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='goal_habit')
    name = models.CharField(max_length=100)
    description = models.TextField()
    target_date = models.DateField()
    status = models.CharField(
        max_length=20, 
        choices=[('completed', 'Completed'), ('inprogress', 'In Progress'), ('onhold', 'On Hold')]
    )
    available = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Milestone(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='milestone_goal')
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=20, 
        choices=[('completed', 'Completed'), ('inprogress', 'In Progress'), ('onhold', 'On Hold')]
    )
    available = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Reminder(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reminder_profile')
    message = models.CharField(max_length=255)
    reminder_date = models.DateTimeField()
    frequency = models.CharField(
        max_length=20, 
        choices=[('daily', 'Daily'), ('monthly', 'Monthly'), ('annually', 'Annually'), ('5years', 'Every 5 Years')]
    )
    available = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
