# Generated by Django 5.1.3 on 2024-11-28 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0035_crew_today'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crew',
            name='today',
        ),
    ]