from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:name>", views.index, name="index"),
    path("view_projects/", views.viewProjects, name="viewProjects"),
    path("createProject/", views.createProjectView, name="createProject"),
    path("createTask/", views.createTaskView, name="createTask"),
]
