# Generated by Django 2.2.12 on 2020-11-11 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0017_auto_20201111_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='performance_tr',
        ),
    ]