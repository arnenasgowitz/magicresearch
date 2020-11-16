# Generated by Django 2.2.12 on 2020-11-12 14:31

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0026_player_religion_int'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='pilot_eff',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='pilot_inv',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='pilot_overall',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='pilot_redis',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
