# Generated by Django 5.1.3 on 2024-11-28 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0037_crew_today'),
    ]

    operations = [
        migrations.AddField(
            model_name='crew',
            name='on_location',
            field=models.BooleanField(default=False),
        ),
    ]
