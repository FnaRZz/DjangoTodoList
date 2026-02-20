from gc import get_objects

from .models import Task
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {
        'tasks': tasks,
    })

def task_create(request):
    if request.method == 'POST':
        task_name = request.POST['task_name']
        task_description = request.POST.get('task_description','')
        task_completed = request.POST.get('task_completed') == 'on'
        task_date = request.POST['task_date']
        Task.objects.create(
            title=task_name,
            description=task_description,
            completed=task_completed,
            date=task_date
        )
        return redirect('Todo:home')
    return render(request, 'create_task.html')

def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('Todo:home')
    return render(request,'task_list.html')

def task_edit(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = request.POST.get('completed') == 'on'
        task.save()
        return redirect('Todo:home')
    return render(request, 'task_edit.html', {'task': task})

def task_more(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        return redirect('Todo:home')
    return render(request,'task_more.html', {'task': task})