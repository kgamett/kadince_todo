from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse, reverse_lazy

from .models import Task
from .forms import TaskForm, SignUpForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('/')

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        filter_option = self.request.GET.get('filter')
        if filter_option == 'completed':
            return Task.objects.filter(user=self.request.user, completed=True)
        elif filter_option == 'incomplete':
            return Task.objects.filter(user=self.request.user, completed=False)
        else:
            return Task.objects.filter(user=self.request.user)
    

class AddTaskView(LoginRequiredMixin, View):
    def get(self, request):
        form = TaskForm(user=request.user)
        return render(request, 'add_task.html', {'form': form})
    
    def post(self, request):
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'add_task.html', {'form': form})


class CompleteTaskView(LoginRequiredMixin, View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.completed = True
        task.save()
        return HttpResponseRedirect(reverse('task_list'))
    
class EditTaskView(LoginRequiredMixin, View):
    def get(self, request, task_id):
        task = Task.objects.get(pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'edit_task.html', {'form': form, 'task': task})
    
    def post(self, request, task_id):
        task = Task.objects.get(pk=task_id, user=request.user)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            edited_task = form.save(commit=False)
            edited_task.user = request.user
            edited_task.save()
            return HttpResponseRedirect(reverse('task_list'))  # Redirect after editing
        return render(request, 'edit_task.html', {'form': form, 'task': task})
    
class DeleteTaskView(LoginRequiredMixin, View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        task.delete()
        return HttpResponseRedirect(reverse('task_list')) 
    
class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration