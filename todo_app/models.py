from django.db import models
from django.urls import reverse
from django.conf import settings

class ToDoItem(models.Model):
    '''
    This is the ToDoItem Model.
    ToDoId      fk      connects the item to the status
    ToDoStatus  string  marks item as 'pending' or 'complete'
    title       string  name of the item in the list 
    '''
    todo_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    todo_status = models.ForeignKey(ToDoStatus, on_delete=models.CASCADE)

class ToDoStatus(models.Model):
    '''
    This is the Status Model
    ToDoId      fk      connects the item with the status
    status      string  either pending or complete
    '''
    todo_status = (
        ('p', 'Pending'),
        ('c', 'Complete'),
    )
    status = models.CharField(
        max_length=1,
        choices=todo_status,
        blank=true,
        default='p'
        help_text='Task Status'
    )

class ToDoList(models.Model):
    '''
    ToDoID      fk      connects the item to the overall list
    '''
