from django.contrib import admin
from .models import Game, Genre, LibraryEntry

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(LibraryEntry)
