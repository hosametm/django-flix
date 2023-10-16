from django.db import models
from categories.models import Category
from videos.models import Video, PublishStatusOptions
from django.contrib.contenttypes.fields import GenericRelation
from tags.models import TaggedItem

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    active = models.BooleanField(default=True)
    videos = models.ManyToManyField(Video, blank=True, through="PlaylistVideo")
    status = models.CharField(
        max_length=2,
        choices=PublishStatusOptions.choices,
        default=PublishStatusOptions.DRAFT,
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    tags = GenericRelation(TaggedItem, related_query_name="playlists")

    def __str__(self):
        return self.title


class PlaylistVideo(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    order = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.playlist.title} - {self.video.title}"
