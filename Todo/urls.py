from django.urls import path
from . import views

app_name = "Todo"

urlpatterns = [
    path('', views.task_list, name='home'),
    path('create/', views.task_create, name='task_create'),
]
