from django.db.models import fields
from django.forms import ModelForm
from .models import Project, Task
from django.contrib.auth.models import User


class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'priority']
        exclude = ('created_by',)

    def save(self, commit=True, user=None):
        self.instance.created_by = user
        return super().save(commit=commit)


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','task_of_project','priority']


#name = forms.CharField(label="Project's Name:", max_length=200)
#priority = forms.CharField(label="Project's Priority (the greater the number, the prior it is compared to other projects.):", max_length=200, required=False)
