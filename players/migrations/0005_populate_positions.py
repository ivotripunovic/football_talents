from django.db import migrations

def populate_positions(apps, schema_editor):
    Position = apps.get_model('players', 'Position')
    
    positions = [
        {'name': 'Goalkeeper', 'code': 'GK', 'x_coordinate': 50, 'y_coordinate': 5, 'is_primary': True},
        {'name': 'Right Back', 'code': 'RB', 'x_coordinate': 80, 'y_coordinate': 30, 'is_primary': True},
        {'name': 'Left Back', 'code': 'LB', 'x_coordinate': 20, 'y_coordinate': 30, 'is_primary': True},
        {'name': 'Center Back', 'code': 'CB', 'x_coordinate': 50, 'y_coordinate': 25, 'is_primary': True},
        {'name': 'Defensive Midfielder', 'code': 'DM', 'x_coordinate': 50, 'y_coordinate': 40, 'is_primary': True},
        {'name': 'Central Midfielder', 'code': 'CM', 'x_coordinate': 50, 'y_coordinate': 50, 'is_primary': True},
        {'name': 'Right Midfielder', 'code': 'RM', 'x_coordinate': 80, 'y_coordinate': 50, 'is_primary': True},
        {'name': 'Left Midfielder', 'code': 'LM', 'x_coordinate': 20, 'y_coordinate': 50, 'is_primary': True},
        {'name': 'Attacking Midfielder', 'code': 'AM', 'x_coordinate': 50, 'y_coordinate': 60, 'is_primary': True},
        {'name': 'Right Winger', 'code': 'RW', 'x_coordinate': 80, 'y_coordinate': 70, 'is_primary': True},
        {'name': 'Left Winger', 'code': 'LW', 'x_coordinate': 20, 'y_coordinate': 70, 'is_primary': True},
        {'name': 'Striker', 'code': 'ST', 'x_coordinate': 50, 'y_coordinate': 80, 'is_primary': True},
        {'name': 'Second Striker', 'code': 'SS', 'x_coordinate': 50, 'y_coordinate': 75, 'is_primary': True},
    ]
    
    for position_data in positions:
        Position.objects.create(**position_data)

def reverse_positions(apps, schema_editor):
    Position = apps.get_model('players', 'Position')
    Position.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('players', '0004_position_remove_player_position_player_positions'),
    ]

    operations = [
        migrations.RunPython(populate_positions, reverse_positions),
    ] 