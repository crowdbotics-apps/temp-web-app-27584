# Generated by Django 2.2.16 on 2020-11-04 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201008_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='competition',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sport',
        ),
    ]
