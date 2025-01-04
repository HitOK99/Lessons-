from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateInput, ClearableFileInput
from .models import Task, Subtask, Comment

class TaskForm(ModelForm):
    attachments = forms.FileField(required=False)
    
    class Meta:
        model = Task
        fields = ['title', 'task_description', 'collaborators', 'status', 'priority', 'budget', 'attachments', 'dead_line']

        widgets = {
            'title': TextInput(attrs={'placeholder': 'Назва'}),
            'task_description': Textarea(attrs={'placeholder': 'Опис'}),
            'collaborators': TextInput(attrs={'placeholder': 'Працівники'}),
            'status': TextInput(attrs={'placeholder': 'Статус'}),
            'priority': TextInput(attrs={'placeholder': 'Пріорітет'}),
            'budget': TextInput(attrs={'placeholder': 'Бюджет'}),
            'attachments': ClearableFileInput(attrs={'placeholder': 'Файл', 'accept': '*/*'}),
            'dead_line': DateInput(attrs={'placeholder': 'Дедлайн'}),
        }

class SubtaskForm(ModelForm):
    class Meta:
        model = Subtask
        fields = ['title', 'task_description', 'collaborators', 'status', 'priority', 'budget', 'attachments', 'dead_line']
        
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Назва підзавдання'}),
            'task_description': Textarea(attrs={'placeholder': 'Опис підзавдання'}),
            'collaborators': TextInput(attrs={'placeholder': 'Працівники'}),
            'status': TextInput(attrs={'placeholder': 'Статус'}),
            'priority': TextInput(attrs={'placeholder': 'Пріорітет'}),
            'budget': TextInput(attrs={'placeholder': 'Бюджет'}),
            'attachments': ClearableFileInput(attrs={'placeholder': 'Файл', 'accept': '*/*'}),
            'dead_line': DateInput(attrs={'placeholder': 'Дедлайн'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    widgets = {
        'text': forms.Textarea(attrs={'placeholder': 'Напишіть свій коментар...', 'rows': 4}),
    }