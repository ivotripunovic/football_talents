# Generated by Django 5.1.7 on 2025-03-30 18:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("GK", "Goalkeeper"),
                            ("DEF", "Defender"),
                            ("MID", "Midfielder"),
                            ("FWD", "Forward"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "height",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Height in centimeters",
                        max_digits=5,
                    ),
                ),
                (
                    "weight",
                    models.DecimalField(
                        decimal_places=2, help_text="Weight in kilograms", max_digits=5
                    ),
                ),
                ("date_of_birth", models.DateField()),
                ("nationality", models.CharField(max_length=100)),
                (
                    "preferred_foot",
                    models.CharField(
                        choices=[("L", "Left"), ("R", "Right"), ("B", "Both")],
                        max_length=10,
                    ),
                ),
                ("jersey_number", models.IntegerField(blank=True, null=True)),
                (
                    "speed",
                    models.IntegerField(
                        blank=True, help_text="Speed rating (1-100)", null=True
                    ),
                ),
                (
                    "strength",
                    models.IntegerField(
                        blank=True, help_text="Strength rating (1-100)", null=True
                    ),
                ),
                (
                    "stamina",
                    models.IntegerField(
                        blank=True, help_text="Stamina rating (1-100)", null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["user__last_name", "user__first_name"],
            },
        ),
    ]
