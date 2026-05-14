from django.db import models

class Task(models.Model):
    COMPLEXITY_CHOICES = [
        ('easy', 'Просте'),
        ('medium', 'Середнє'),
        ('hard', 'Важке'),
    ]

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(
        max_length=200
    )
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    color = models.CharField(max_length=20, default='white')
    complexity = models.CharField(
        max_length=10,
        choices=COMPLEXITY_CHOICES,
        default='medium'
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']