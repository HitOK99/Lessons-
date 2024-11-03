from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Task, Subtask
from .forms import TaskForm, SubtaskForm 

def add_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_task')
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

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    tasks = Task.objects.all()
    form = SubtaskForm()
    subtasks = Subtask.objects.filter(task=task)

    data = {
        'task': task,
        'tasks': tasks,
        'form': form,
        'subtasks': subtasks,
    }
    return render(request, 'main_work_window/task_detail.html', data)

def add_subtask_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    tasks = Task.objects.all()
    form = SubtaskForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            subtask.save()
            return redirect('task_detail', task_id=task.id)

    return render(request, 'main_work_window/add_subtask.html', {'form': form, 'tasks': tasks, 'task': task})

@require_POST
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('add_task')
    except Task.DoesNotExist:
        return redirect('add_task')

def delete_subtask(request, subtask_id):
    subtask = get_object_or_404(Subtask, id=subtask_id)
    task_id = subtask.task.id
    if request.method == 'POST':
        subtask.delete()
    return redirect('task_detail', task_id=task_id)
