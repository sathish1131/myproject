# Generated by Django 3.2.12 on 2024-09-08 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_rename_task_todolist_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='priority',
            field=models.CharField(default='Low', max_length=50),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
