# Generated by Django 5.1.3 on 2024-11-21 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_alter_day_lift_frame_alter_day_mpd_manifold_building_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='name',
        ),
        migrations.AddField(
            model_name='day',
            name='well_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.well'),
        ),
    ]