# Generated by Django 5.1.3 on 2025-02-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0056_alter_note_day_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='day_due',
            field=models.DateField(),
        ),
    ]
