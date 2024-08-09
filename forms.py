from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'Done': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'content': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task content'
            }),
        }

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Update task content'
            }),
        }
