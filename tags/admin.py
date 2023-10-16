from django.contrib import admin
from .models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline

class TaggedItemInline(GenericTabularInline):
    model = TaggedItem
    extra = 1

class TagggedItemAdmin(admin.ModelAdmin):
    fields = ['tag', 'content_object', 'content_type', 'object_id']
    readonly_fields = ['content_object']
    class Meta:
        model = TaggedItem
      
admin.site.register(TaggedItem, TagggedItemAdmin)
