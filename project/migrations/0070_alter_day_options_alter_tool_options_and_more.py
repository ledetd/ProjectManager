# Generated by Django 5.1.3 on 2025-02-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0069_tool_well_section'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='day',
            options={'ordering': ('current_operations',)},
        ),
        migrations.AlterModelOptions(
            name='tool',
            options={'ordering': ('tool_used', '-tool_location')},
        ),
        migrations.AlterField(
            model_name='day',
            name='total_rotating_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
