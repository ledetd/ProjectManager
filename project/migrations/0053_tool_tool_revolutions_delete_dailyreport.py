# Generated by Django 5.1.3 on 2025-02-17 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0052_alter_day_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='tool_revolutions',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='DailyReport',
        ),
    ]
