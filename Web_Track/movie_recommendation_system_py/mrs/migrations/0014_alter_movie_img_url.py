# Generated by Django 3.2.7 on 2021-09-25 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrs', '0013_auto_20210925_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img_url',
            field=models.URLField(null=True),
        ),
    ]
