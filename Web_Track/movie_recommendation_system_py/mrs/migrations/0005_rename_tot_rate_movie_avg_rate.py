# Generated by Django 3.2.7 on 2021-09-24 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrs', '0004_auto_20210924_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='tot_rate',
            new_name='avg_rate',
        ),
    ]
