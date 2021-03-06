# Generated by Django 2.2.16 on 2020-10-19 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_quicklink'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='history_transaction', to='home.HistoryRecord')),
            ],
            options={
                'verbose_name_plural': 'History Transactions',
                'ordering': ('-created',),
            },
        ),
    ]
