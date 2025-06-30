from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list_tasks, name='list_tasks'),
    path('create/', views.create_task, name='create_task'),
]