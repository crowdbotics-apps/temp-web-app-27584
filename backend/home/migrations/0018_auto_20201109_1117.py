# Generated by Django 2.2.16 on 2020-11-09 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20201104_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpreference',
            name='competition',
        ),
        migrations.DeleteModel(
            name='Competition',
        ),
    ]
