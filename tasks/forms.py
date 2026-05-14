from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'description', 'priority', 'complexity', 'color']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву задачі',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть опис задачі (опціонально)',
                'rows': 4
            
            }),
            'priority': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пріорітет (0-10)',
                'min': 0,
                'max': 10
            }),
            'complexity': forms.Select(attrs={
                'class': 'form-control'
            }),
            'color': forms.Select(attrs={
                'class': 'form-control'
            })

        }