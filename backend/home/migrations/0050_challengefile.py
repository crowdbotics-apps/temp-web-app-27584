# Generated by Django 2.2.18 on 2021-03-12 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_auto_20210312_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='1', max_length=225)),
                ('title', models.CharField(max_length=244)),
                ('file', models.FileField(blank=True, null=True, upload_to='challenge-download/')),
                ('challenge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='challenge_download', to='home.Challenge')),
            ],
        ),
    ]
