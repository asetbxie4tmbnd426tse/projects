from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project, Task
from .forms import CreateProjectForm, CreateTaskForm
#from projectManagementApp import forms
#from datetime import datetime

# Create your views here.

def index(request, name):
    
    if Project.objects.get(name=name).created_by_id == request.user.id:
        tasks = Task.objects.filter(task_of_project_id=name)
        if request.method == "POST":
            if request.POST.get("save"):
                for task in tasks:
                    if request.POST.get(f"t{str(task.title)}") == "clicked":
                        task.complete = True
                    else:
                        task.complete = False
                    
                    task.save()
                return HttpResponseRedirect(f"/{name}") 

            elif request.POST.get("newTask"):
                return HttpResponseRedirect("/createTask/")
            
            else:
                for t in tasks:
                    if request.POST.get(f"delete{t.title}"):
                        t.delete()
                        return HttpResponseRedirect(f"/{name}")


    else:
        return HttpResponseRedirect("/view_projects/")

    context = {
            "project":name,
            "tasks":tasks
           }
    return render(request, "projectManagementApp/project.html", context)

def viewProjects(request):
    projects = request.user.project_set.filter()
    context = {"projects":projects}
    return render(request, "projectManagementApp/viewProjects.html", context)


def home(request):
    context = {}
    return render(request, "projectManagementApp/home.html", context)

def createProjectView(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            name = form.cleaned_data["name"]
            project = Project.objects.get(name=name)
            return HttpResponseRedirect(f"/{project.name}") 
    else:
        form = CreateProjectForm()
    
    context = {"form": form}
    return render(request, "projectManagementApp/createProject.html", context)

def createTaskView(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            project_name = Project.objects.get(name=form.cleaned_data["task_of_project"]).name
            return HttpResponseRedirect(f"/{project_name}") 
    else:
        form = CreateTaskForm()
    
    context = {"form": form}
    return render(request, "projectManagementApp/createProject.html", context)