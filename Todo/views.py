from .models import Tasks
from django.shortcuts import render

# Create your views here.


def index(request):
    task = Tasks.objects.all()
    return render(request, 'index.html', {
        task: 'task',
    })
