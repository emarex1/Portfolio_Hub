# Generated by Django 4.2.5 on 2023-12-13 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_recentposts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='title',
            new_name='my_title',
        ),
    ]
