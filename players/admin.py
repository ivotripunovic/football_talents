from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'height', 'weight', 'nationality', 'country', 'city', 'club', 'jersey_number')
    list_filter = ('position', 'nationality', 'country', 'club', 'preferred_foot')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'nationality', 'country', 'city', 'club')
    ordering = ('user__last_name', 'user__first_name')
