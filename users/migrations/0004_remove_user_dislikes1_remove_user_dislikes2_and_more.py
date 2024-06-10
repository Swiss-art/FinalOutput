# Generated by Django 5.0.1 on 2024-05-06 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_dislikes1_alter_user_dislikes2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dislikes1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dislikes2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dislikes3',
        ),
        migrations.RemoveField(
            model_name='user',
            name='likes1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='likes2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='likes3',
        ),
        migrations.AddField(
            model_name='user',
            name='dislikes',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='reason',
            field=models.TextField(blank=True),
        ),
    ]