from django.contrib import admin
from .models import Playlist, PlaylistVideo
from tags.admin import TaggedItemInline
class PlaylistVideoInline(admin.TabularInline):
    model = PlaylistVideo
    extra = 1
    
    
class PlaylistAdmin(admin.ModelAdmin):
    inlines = [PlaylistVideoInline, TaggedItemInline]
    list_display = ['title', 'active', 'status']
    list_editable = ['active', 'status']
    list_filter = ['active', 'status']
    search_fields = ['title']
    class Meta:
        model = Playlist


admin.site.register(Playlist, PlaylistAdmin)