from .models import Task
from django.shortcuts import render

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {
        'tasks': tasks,
    })
