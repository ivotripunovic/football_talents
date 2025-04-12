from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, PlayerProfileForm
from .models import Player, Position

# Create your views here.

def home(request):
    # Get recent players to display on homepage
    recent_players = Player.objects.all().order_by('-id')[:5]
    return render(request, 'players/home.html', {
        'recent_players': recent_players
    })

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        player_form = PlayerProfileForm(request.POST)
        
        if user_form.is_valid() and player_form.is_valid():
            user = user_form.save()
            player = player_form.save(commit=False)
            player.user = user
            player.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        player_form = PlayerProfileForm()
    
    return render(request, 'players/register.html', {
        'user_form': user_form,
        'player_form': player_form,
        'positions': Position.objects.all()
    })

@login_required
def profile(request, player_id):
    try:
        player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        player = None
    
    return render(request, 'players/profile.html', {'player': player})

@login_required
def edit_profile(request):
    try:
        player = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        player = None
    
    if request.method == 'POST':
        form = PlayerProfileForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save(commit=False)
            player.user = request.user
            player.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = PlayerProfileForm(instance=player)
    
    return render(request, 'players/edit_profile.html', {'form': form})
