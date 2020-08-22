from django.contrib import admin

from .models import TeamStructure, TeamPlayerStructure, Matches, playerHistory
admin.site.register(TeamStructure)
admin.site.register(TeamPlayerStructure)
admin.site.register(Matches)
admin.site.register(playerHistory)

# Register your models here.
