from django.urls import path
from .views import TaskListView, AddTaskView, CompleteTaskView, SignUpView, EditTaskView, DeleteTaskView, logout_view
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from todo_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('add/', AddTaskView.as_view(), name='add_task'),
    path('complete/<int:task_id>/', CompleteTaskView.as_view(), name='complete_task'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit/<int:task_id>/', views.EditTaskView.as_view(), name='edit_task'),
    path('delete/<int:task_id>/', views.DeleteTaskView.as_view(), name='delete_task'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]