from .models import Task
from django.shortcuts import render, redirect

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

