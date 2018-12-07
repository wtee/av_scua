# Generated by Django 2.1 on 2018-12-07 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0005_avitem_copies'),
    ]

    operations = [
        migrations.AddField(
            model_name='avitem',
            name='digital_preservation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avitem',
            name='lto_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='avitem',
            name='other_notes',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='avitem',
            name='status',
            field=models.CharField(choices=[('on shelf', 'ON SHELF'), ('conservation', 'CONSERVATION'), ('vendor', 'VENDOR'), ('loan', 'LOAN')], default='', max_length=15),
        ),
    ]
