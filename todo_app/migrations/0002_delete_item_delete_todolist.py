# Generated by Django 5.0.1 on 2024-01-03 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]
