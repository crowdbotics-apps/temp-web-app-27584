# Generated by Django 2.2.19 on 2021-04-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_challengefile_is_bulk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='type',
            field=models.CharField(choices=[('CODE', 'CODE'), ('LICENCE', 'LICENCE'), ('TEAM', 'TEAM'), ('CUSTOM_CODE', 'CUSTOM_CODE')], default='CODE', max_length=225),
        ),
    ]
