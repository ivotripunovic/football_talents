from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator

class Position(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3, unique=True)
    description = models.TextField(blank=True)
    x_coordinate = models.FloatField(help_text="X coordinate on the football field (0-100)")
    y_coordinate = models.FloatField(help_text="Y coordinate on the football field (0-100)")
    is_primary = models.BooleanField(default=False, help_text="Is this a primary position?")

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        ordering = ['name']

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    positions = models.ManyToManyField(Position, related_name='players')
    height = models.DecimalField(max_digits=5, decimal_places=2, help_text="Height in centimeters")
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight in kilograms")
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    country = models.CharField(max_length=100, help_text="Current country of residence", blank=True, null=True)
    state = models.CharField(max_length=100, help_text="State/Province of residence", blank=True, null=True)
    city = models.CharField(max_length=100, help_text="City of residence", blank=True, null=True)
    club = models.CharField(max_length=100, help_text="Current football club", blank=True, null=True)
    fifa_profile_url = models.URLField(max_length=255, help_text="Link to official FIFA profile", blank=True, null=True, validators=[URLValidator()])
    preferred_foot = models.CharField(max_length=10, choices=[('L', 'Left'), ('R', 'Right'), ('B', 'Both')])
    jersey_number = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(help_text="Speed rating (1-100)", null=True, blank=True)
    strength = models.IntegerField(help_text="Strength rating (1-100)", null=True, blank=True)
    stamina = models.IntegerField(help_text="Stamina rating (1-100)", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        positions = ", ".join([pos.name for pos in self.positions.all()])
        return f"{self.user.get_full_name()} - {positions}"

    class Meta:
        ordering = ['user__last_name', 'user__first_name']
