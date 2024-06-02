from django.contrib import admin

# Register your models here.
from games.models import Games
from games.models import Engine
from games.models import Profile

admin.site.register(Games)
admin.site.register(Engine)
admin.site.register(Profile)
