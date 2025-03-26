from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length= 200, blank=False)
    completed = models.BooleanField(default=False, blank=False)
    deadline_day = models.DateTimeField(auto_now_add=True)
    