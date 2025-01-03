# Generated by Django 5.1.3 on 2024-12-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0046_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='average_flow_line_temp',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='max_connection_surface_back_pressure',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='max_drilling_surface_back_pressure',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='max_flow_line_temp',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='max_rpm',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='max_stripping_surface_back_pressure',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='mud_system',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='mud_weight',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='total_installed_time',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='total_rotating_time',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='total_stripped_length',
        ),
        migrations.AddField(
            model_name='tracker',
            name='bearingTemp',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='drilledLengthRotating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='drilledLengthSliding',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='drilledLengthTotal',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='flowlineTemp',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='holeDepth',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='pressureConnections',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='pressureDrilling',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='pressureStripping',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='rotatingDepth',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='rpm',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='strippedLengthDown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='strippedLengthTotal',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='strippedLengthUp',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='totalRotationTime',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='totalRotations',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='trippingSpeed',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='hole_section',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='run_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
