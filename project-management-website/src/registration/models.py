from django.db import models
from django.contrib.auth.models import Group
# Create your models here.

#this is a function that creates a group for every created user
def createGroup(user_name: str):
    new_group, created = Group.objects.get_or_create(name =f'{user_name}')