# Generated by Django 2.2.17 on 2020-12-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_track_is_premium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='track_duration',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
