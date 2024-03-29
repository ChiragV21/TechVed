# Generated by Django 5.0.3 on 2024-03-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewExperienceApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewexperience',
            name='experience',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interviewexperience',
            name='role',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interviewexperience',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
