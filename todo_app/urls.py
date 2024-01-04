from django.urls import path
from .views import TaskListView, AddTaskView, CompleteTaskView, SignUpView
from todo_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('add/', AddTaskView.as_view(), name='add_task'),
    path('complete/<int:task_id>/', CompleteTaskView.as_view(), name='complete_task'),
    path('signup/', SignUpView.as_view(), name='signup'),
]