# Generated by Django 2.2.16 on 2020-11-18 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20201118_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quicklink',
            name='track',
            field=models.FileField(upload_to='quicklinks/track/'),
        ),
    ]
