# Generated by Django 5.1.7 on 2025-03-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='deadline_day',
            field=models.DateTimeField(null=True),
        ),
    ]
