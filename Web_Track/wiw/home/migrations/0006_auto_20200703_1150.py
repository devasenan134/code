# Generated by Django 3.0.3 on 2020-07-03 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200703_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(upload_to='wiw/media/home/videos/'),
        ),
    ]
