# Generated by Django 2.2.17 on 2020-12-31 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0028_track_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244)),
            ],
            options={
                'verbose_name_plural': 'Challenges',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244)),
                ('code', models.CharField(max_length=244, unique=True)),
                ('grant_premium', models.BooleanField(default=False)),
                ('grant_premium_for_months', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('18', '18'), ('24', '24'), ('36', '36'), ('48', '48'), ('50', '50')], default='0', max_length=225)),
                ('grant_premium_users_limit', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Member', 'Member'), ('Admin', 'Admin'), ('Owner', 'Owner')], default='Member', max_length=225)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team_of_user', to='home.Team')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_team', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Team Members',
            },
        ),
        migrations.CreateModel(
            name='TeamChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team_message', to='home.Team')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_message', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Team Chat Messages',
            },
        ),
        migrations.CreateModel(
            name='SelectedChallenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('challenge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='selected_challenge', to='home.Challenge')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='selected_challenge_team', to='home.Team')),
            ],
            options={
                'verbose_name_plural': 'Selected Challenge',
            },
        ),
        migrations.CreateModel(
            name='LastSeen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='message_last_seen', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_last_seen', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Last Seen Message',
            },
        ),
        migrations.CreateModel(
            name='ChallengeTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], default='1', max_length=225)),
                ('task_title', models.CharField(max_length=244)),
                ('task', models.TextField(blank=True, null=True)),
                ('challenge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='challenge_tasks', to='home.Challenge')),
                ('task_track', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='task_track', to='home.Track')),
            ],
            options={
                'verbose_name_plural': 'Challenge Tasks',
            },
        ),
    ]
