# Generated by Django 5.1.3 on 2025-02-22 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0067_rename_manifold_rate_manifold_operational_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.rate'),
        ),
    ]
