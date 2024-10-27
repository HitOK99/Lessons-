from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def main_work_window(request):
    tasks = Task.objects.all()
    return render(request, 'main_work_window/main_work_window.html', {'tasks': tasks})

def add_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_work_window')
        else:
            error = 'Неправильно заповнено!'
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    
    data = {
        'form': form,
        'tasks': tasks,
        'error': error
    }
    return render(request, 'main_work_window/add_task.html', data)
