# Generated by Django 2.2.17 on 2021-01-26 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_auto_20210119_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='small_thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='thumbnail/'),
        ),
    ]
