from django.urls import path
from . import views

app_name = "Todo"

urlpatterns = [
    path('', views.task_list, name='home'),
    path('create/', views.task_create, name='task_create'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
]
