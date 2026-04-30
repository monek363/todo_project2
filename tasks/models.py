from django.db import models

class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(
        max_length=200
    )
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    color = models.CharField(max_length=20, default='white')

    def __str__(self):
        return self.title
    
# Create your models here.
"""
password = adminlinuxoid957
python manage.py createsuperuser
python manage.py runserver
python manage.py startapp tasks ! 'tasks' conflicts with the name
django-admin startproject config
"""
