# Generated by Django 2.1 on 2018-12-07 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_remove_avitem_formatduration'),
    ]

    operations = [
        migrations.AddField(
            model_name='avitem',
            name='formatduration',
            field=models.TimeField(default='00:00:00'),
        ),
    ]