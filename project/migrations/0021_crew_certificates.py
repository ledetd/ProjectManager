# Generated by Django 5.1.3 on 2024-11-22 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_remove_certificate_certificate_complete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crew',
            name='certificates',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project.certificate'),
            preserve_default=False,
        ),
    ]