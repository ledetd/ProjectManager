# Generated by Django 5.1.3 on 2024-11-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0030_alter_crew_date_bst_alter_crew_date_h2s_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crew',
            name='bst_expires',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='crew',
            name='h2s_expires',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='crew',
            name='iwcf_expires',
            field=models.DateField(auto_now=True),
        ),
    ]