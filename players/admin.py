from django.contrib import admin
from .models import Player, Position

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_primary', 'x_coordinate', 'y_coordinate')
    list_filter = ('is_primary',)
    search_fields = ('name', 'code', 'description')
    ordering = ('name',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_positions', 'height', 'weight', 'nationality', 'country', 'city', 'club', 'jersey_number', 'has_fifa_profile')
    list_filter = ('positions', 'nationality', 'country', 'club', 'preferred_foot')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'nationality', 'country', 'city', 'club')
    ordering = ('user__last_name', 'user__first_name')
    filter_horizontal = ('positions',)

    def get_positions(self, obj):
        return ", ".join([pos.name for pos in obj.positions.all()])
    get_positions.short_description = 'Positions'

    def has_fifa_profile(self, obj):
        return bool(obj.fifa_profile_url)
    has_fifa_profile.boolean = True
    has_fifa_profile.short_description = 'FIFA Profile'
