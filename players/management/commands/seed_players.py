from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from players.models import Player, Position
from datetime import date, timedelta
import random
from faker import Faker
from players.models import Player
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seeds the database with realistic player data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write("Deleting old players")
        # Delete all players and their associated users
        for player in Player.objects.all():
            player.user.delete()
            player.delete()
        self.stdout.write("Finished deleting existing players")
        
        # Create positions if they don't exist
        positions_data = [
            {'name': 'Goalkeeper', 'code': 'GK', 'x': 50, 'y': 5, 'is_primary': True},
            {'name': 'Right Back', 'code': 'RB', 'x': 85, 'y': 30, 'is_primary': True},
            {'name': 'Center Back', 'code': 'CB', 'x': 50, 'y': 25, 'is_primary': True},
            {'name': 'Left Back', 'code': 'LB', 'x': 15, 'y': 30, 'is_primary': True},
            {'name': 'Defensive Midfielder', 'code': 'CM', 'x': 50, 'y': 45, 'is_primary': True},
            {'name': 'Right Midfielder', 'code': 'RM', 'x': 85, 'y': 50, 'is_primary': True},
            {'name': 'Central Midfielder', 'code': 'CM', 'x': 50, 'y': 50, 'is_primary': True},
            {'name': 'Left Midfielder', 'code': 'LM', 'x': 15, 'y': 50, 'is_primary': True},
            {'name': 'Attacking Midfielder', 'code': 'CM', 'x': 50, 'y': 65, 'is_primary': True},
            {'name': 'Right Winger', 'code': 'RW', 'x': 85, 'y': 70, 'is_primary': True},
            {'name': 'Striker', 'code': 'ST', 'x': 50, 'y': 80, 'is_primary': True},
            {'name': 'Left Winger', 'code': 'LW', 'x': 15, 'y': 70, 'is_primary': True},
        ]

        positions = {}
        for pos_data in positions_data:
            pos = Position.objects.get(
                code=pos_data['code']
            )
            positions[pos_data['code']] = pos

        # Sample player data
        players_data = [
            {
                'first_name': 'Lionel', 'last_name': 'Messi', 'email': 'messi@example.com',
                'positions': ['RW', 'ST', 'CM'], 'height': 170, 'weight': 72,
                'date_of_birth': date(1987, 6, 24), 'nationality': 'Argentina',
                'country': 'United States', 'city': 'Miami', 'club': 'Inter Miami',
                'preferred_foot': 'L', 'jersey_number': 10,
                'speed': 90, 'strength': 70, 'stamina': 85
            },
            {
                'first_name': 'Cristiano', 'last_name': 'Ronaldo', 'email': 'ronaldo@example.com',
                'positions': ['ST', 'LW'], 'height': 187, 'weight': 85,
                'date_of_birth': date(1985, 2, 5), 'nationality': 'Portugal',
                'country': 'Saudi Arabia', 'city': 'Riyadh', 'club': 'Al Nassr',
                'preferred_foot': 'R', 'jersey_number': 7,
                'speed': 88, 'strength': 85, 'stamina': 90
            },
            {
                'first_name': 'Kevin', 'last_name': 'De Bruyne', 'email': 'debruyne@example.com',
                'positions': ['CM', 'CM'], 'height': 181, 'weight': 76,
                'date_of_birth': date(1991, 6, 28), 'nationality': 'Belgium',
                'country': 'England', 'city': 'Manchester', 'club': 'Manchester City',
                'preferred_foot': 'R', 'jersey_number': 17,
                'speed': 80, 'strength': 75, 'stamina': 85
            },
            {
                'first_name': 'Virgil', 'last_name': 'van Dijk', 'email': 'vandijk@example.com',
                'positions': ['CB'], 'height': 193, 'weight': 92,
                'date_of_birth': date(1991, 7, 8), 'nationality': 'Netherlands',
                'country': 'England', 'city': 'Liverpool', 'club': 'Liverpool',
                'preferred_foot': 'R', 'jersey_number': 4,
                'speed': 75, 'strength': 90, 'stamina': 80
            },
            {
                'first_name': 'Kylian', 'last_name': 'Mbappé', 'email': 'mbappe@example.com',
                'positions': ['ST', 'LW'], 'height': 178, 'weight': 73,
                'date_of_birth': date(1998, 12, 20), 'nationality': 'France',
                'country': 'France', 'city': 'Paris', 'club': 'Paris Saint-Germain',
                'preferred_foot': 'R', 'jersey_number': 7,
                'speed': 95, 'strength': 75, 'stamina': 85
            }
        ]

        # Create players
        for player_data in players_data:
            # Create user
            username = f"{player_data['first_name'].lower()}.{player_data['last_name'].lower()}"
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': player_data['first_name'],
                    'last_name': player_data['last_name'],
                    'email': player_data['email'],
                    'password': 'pbkdf2_sha256$600000$dummy$dummy='  # Dummy password
                }
            )

            if created:
                # Create player profile
                player = Player.objects.create(
                    user=user,
                    height=player_data['height'],
                    weight=player_data['weight'],
                    date_of_birth=player_data['date_of_birth'],
                    nationality=player_data['nationality'],
                    country=player_data['country'],
                    city=player_data['city'],
                    club=player_data['club'],
                    preferred_foot=player_data['preferred_foot'],
                    jersey_number=player_data['jersey_number'],
                    speed=player_data['speed'],
                    strength=player_data['strength'],
                    stamina=player_data['stamina']
                )

                # Add positions
                for pos_code in player_data['positions']:
                    player.positions.add(positions[pos_code])

                self.stdout.write(self.style.SUCCESS(f'Created player: {player}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded player data')) 