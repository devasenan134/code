# Generated by Django 3.0.3 on 2020-08-05 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_scores_source_file'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scores',
            new_name='Score',
        ),
    ]
