from django.contrib import admin
from .models import Artist, Singer, SoloArtist, GroupArtist, Actor

# Register your models here.

admin.site.register(Artist)
admin.site.register(Singer)
admin.site.register(SoloArtist)
admin.site.register(GroupArtist)
admin.site.register(Actor)



