# Generated by Django 2.2.16 on 2020-11-04 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20201104_0913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competition',
            options={'verbose_name_plural': 'Competitions'},
        ),
        migrations.AlterModelOptions(
            name='sport',
            options={'verbose_name_plural': 'Sports'},
        ),
    ]
