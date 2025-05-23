# Generated by Django 5.2 on 2025-04-12 21:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("players", "0002_player_city_player_club_player_country_player_state"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="fifa_profile_url",
            field=models.URLField(
                blank=True,
                help_text="Link to official FIFA profile",
                max_length=255,
                null=True,
                validators=[django.core.validators.URLValidator()],
            ),
        ),
    ]
