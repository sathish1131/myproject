# Generated by Django 3.2.12 on 2024-09-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20240908_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='priority',
            field=models.CharField(default='low', max_length=50),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
