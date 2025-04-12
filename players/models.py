from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    height = models.DecimalField(max_digits=5, decimal_places=2, help_text="Height in centimeters")
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight in kilograms")
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    country = models.CharField(max_length=100, help_text="Current country of residence", blank=True, null=True)
    state = models.CharField(max_length=100, help_text="State/Province of residence", blank=True, null=True)
    city = models.CharField(max_length=100, help_text="City of residence", blank=True, null=True)
    club = models.CharField(max_length=100, help_text="Current football club", blank=True, null=True)
    preferred_foot = models.CharField(max_length=10, choices=[('L', 'Left'), ('R', 'Right'), ('B', 'Both')])
    jersey_number = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(help_text="Speed rating (1-100)", null=True, blank=True)
    strength = models.IntegerField(help_text="Strength rating (1-100)", null=True, blank=True)
    stamina = models.IntegerField(help_text="Stamina rating (1-100)", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"

    class Meta:
        ordering = ['user__last_name', 'user__first_name']
