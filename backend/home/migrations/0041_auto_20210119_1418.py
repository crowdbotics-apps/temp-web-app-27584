# Generated by Django 2.2.17 on 2021-01-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_auto_20210119_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='artist',
            field=models.CharField(blank=True, default='Restoic', max_length=250, null=True),
        ),
    ]
