from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Player

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['position', 'height', 'weight', 'date_of_birth', 'nationality', 
                 'country', 'state', 'city', 'club', 'fifa_profile_url',
                 'preferred_foot', 'jersey_number', 'speed', 'strength', 'stamina']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'fifa_profile_url': forms.URLInput(attrs={'placeholder': 'https://www.fifa.com/player/...'}),
        } 