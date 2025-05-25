from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'task': forms.TextInput(attrs={
                'placeholder': 'Add the task',
                'class': 'form-control',
            }),
            'due_date': forms.DateInput(attrs={
                'placeholder': 'Enter the due date',
                'type': 'date',
                'class': 'form-control',
            }),
        }
