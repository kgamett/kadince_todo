from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TaskForm,self).__init__(*args, **kwargs)

    def save(self, commit=True):
        task = super(TaskForm, self).save(commit=False)
        task.user = self.user  # Assign the user to the task
        if commit:
            task.save()
        return task

class SignUpForm(UserCreationForm):
    class meta:
        model = User
        fields = ('username', 'password1', 'password2')