# Generated by Django 5.1.3 on 2025-02-19 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0064_tool_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.project'),
        ),
    ]
