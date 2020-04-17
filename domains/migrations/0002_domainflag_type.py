# Generated by Django 3.0.5 on 2020-04-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='domainflag',
            name='type',
            field=models.CharField(choices=[('EXP', 'Expired'), ('OUT', 'Outzone'), ('DEL', 'Delete Candidate')], default='Expired', max_length=3),
        ),
    ]