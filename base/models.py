from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """String representation of a model."""
        return self.title

    class Meta:
        ordering = ['is_completed'] # push every done task to the bottom
