from select import select

from myapp.models import Project
from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task Title", max_length=100)
    description = forms.CharField(
        label="Task Description", widget=forms.Textarea)
    project = forms.ModelChoiceField(queryset=Project.objects.all())
