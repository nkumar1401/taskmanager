from django.urls import path
from .views import *

urlpatterns = [
    path('list/', list_tasks, name='list_tasks'),
    path('create/', create_task, name='create_task'),
]