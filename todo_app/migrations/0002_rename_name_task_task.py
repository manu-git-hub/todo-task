# Generated by Django 4.1.5 on 2023-01-17 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="name",
            new_name="task",
        ),
    ]
