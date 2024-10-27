from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateInput, ClearableFileInput

class TaskForm(ModelForm):
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