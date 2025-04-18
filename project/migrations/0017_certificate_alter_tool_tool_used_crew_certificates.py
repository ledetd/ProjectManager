# Generated by Django 5.1.3 on 2024-11-22 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_well_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(max_length=500)),
                ('certificate_complete', models.BooleanField(default=False)),
                ('certificate_date', models.DateField()),
                ('certificate_expires', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='tool',
            name='tool_used',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='crew',
            name='certificates',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.certificate'),
        ),
    ]
