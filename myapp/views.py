from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from myapp import form
from myapp.form import CreateNewProject, CreateNewTask
from .models import Project, Task


def index(request):
    title = "Welcome to the Project Management App"
    return render(request, 'index.html', {'title': title})


def hello(request, name):
    return HttpResponse(f"<h2>Hello, {name}!</h2>")


def about(request):
    username = 'Cesar Negrete'
    return render(request, 'about.html', {'username': username})


def project(request):
    # projects = get_object_or_404(Project, id=project_id)
    projects = Project.objects.all()
    return render(request, 'projects/project.html', {'project': projects})


def task(request):
    # task = get_object_or_404(Task, id=task_id)
    tasks = Task.objects.all()
    return render(request, 'tasks/task.html', {'task': tasks})


def create_task(request):
    # print(request.GET['title'])
    # print(request.GET['description'])

    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('tasks')


def create_projects(request):
    if request.method == 'GET':
        return render(request, 'projects/create_projects.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('project')
