from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    ACTIVITY_TYPES = [
        ('workout', 'Workout'),
        ('meal', 'Meal'),
        ('steps', 'Steps'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    steps = models.PositiveIntegerField(default=0)  # ✅ For step-tracking support
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')

    def __str__(self):
        return f"{self.title} ({self.status})"
