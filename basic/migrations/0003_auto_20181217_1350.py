# Generated by Django 2.1 on 2018-12-17 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20181217_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avitem',
            name='format_duration',
            field=models.TimeField(blank=True, default='00:00:00'),
        ),
    ]
