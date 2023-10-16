from django.contrib import admin
from .models import VideoAllProxy, VideoPublishedProxy, PublishStatusOptions
from tags.admin import TaggedItemInline

class VideoAllAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline]
    list_display = ['title', "slug"]
    search_fields = ['title']
    list_filter = ['active']

    class Meta:
        model = VideoAllProxy


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline]
    list_display = ['title', "slug"]
    search_fields = ['title']

    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return self.model.objects.filter(status=PublishStatusOptions.PUBLISHED)


admin.site.register(VideoAllProxy, VideoAllAdmin)
admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)
