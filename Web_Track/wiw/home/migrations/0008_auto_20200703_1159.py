# Generated by Django 3.0.3 on 2020-07-03 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200703_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video_link',
            new_name='url',
        ),
    ]
