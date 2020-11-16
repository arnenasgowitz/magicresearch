# Generated by Django 2.2.12 on 2020-11-04 12:34

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0008_auto_20201104_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='income',
            field=otree.db.models.IntegerField(choices=[[1, 'Below 2.000'], [2, '2.000 - 4.000'], [3, '4.000 - 8.000'], [4, '8.000 - 12.000'], [5, '12.000 - 20.000'], [6, 'More than 20.000']], null=True, verbose_name='In which range is your monthly household income?'),
        ),
    ]
