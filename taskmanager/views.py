from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from .models import Task
import json

@login_required
def list_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(user=request.user).values('title', 'created_at')
        return JsonResponse(list(tasks), safe=False)
    return HttpResponseBadRequest("Invalid request method. Use GET to retrieve tasks.")

@login_required
def create_task(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            description = data.get('description')
            if not title:
                return HttpResponseBadRequest("Title is required.")
            task = Task.objects.create(user=request.user, title=title, description=description)
            return JsonResponse({
                'title': task.title,
                'description': task.description,
            }, status=201)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data.")
    return HttpResponseBadRequest("Invalid request method. Use POST to create a task.")