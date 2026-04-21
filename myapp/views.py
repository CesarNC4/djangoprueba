from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from myapp.form import CreateNewTask
from .models import Project, Task
from django.shortcuts import get_object_or_404, render


def index(request):
    title = "Welcome to the Project Management App"
    return render(request, 'index.html', {'title': title})


def hello(request, name):
    return HttpResponse(f"<h2>Hello, {name}!</h2>")


def about(request):
    username = 'Cesar Negrete'
    return render(request, 'about.html', {'username': username})


def project(request, project_id):
    # projects = get_object_or_404(Project, id=project_id)
    projects = Project.objects.all()
    return render(request, 'project.html', {'project': projects})


def task(request, task_id):
    # task = get_object_or_404(Task, id=task_id)
    tasks = Task.objects.all()
    return render(request, 'task.html', {'task': tasks})


def create_task(request):
    if request.method == 'GET':
        # show interface to create a new task
        return render(request, 'create_task.html', {'form': CreateNewTask()})
    else:
        # create a new task
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=request.POST['project']
        )
        return redirect('/task/1')
