from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    priority = models.CharField(max_length=200, default=None)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_in = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True)
    completed_in = models.DateTimeField(auto_now=False, auto_now_add=False,default=None, null=True)
    #sub_project_of = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, default=None, null=True)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    priority = models.CharField(max_length=200, default=None)
    description = models.TextField(blank=True, null=True)
    created_in = models.DateTimeField(auto_now_add=True)
    task_of_project = models.ForeignKey(Project, on_delete=models.CASCADE, to_field="name")
    complete = models.BooleanField(default=False)
    completed_by = models.CharField(max_length=200, blank=True, default=None, null=True)
    completed_in = models.DateTimeField(auto_now=False, auto_now_add=False,default=None, null=True)
    
    def __str__(self):
        if self.description == None:
            return self.title
        return f"{self.title}: {self.description}" 