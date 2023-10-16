from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from tags.models import TaggedItem


class PublishStatusOptions(models.TextChoices):
    PUBLISHED = "PU", "Published"
    DRAFT = "DR", "Draft"


class Video(models.Model):
    VideoStatusOptions = PublishStatusOptions
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    status = models.CharField(
        max_length=2,
        choices=VideoStatusOptions.choices,
        default=VideoStatusOptions.DRAFT,
    )
    published_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    tags = GenericRelation(TaggedItem, related_query_name="videos")

    def __str__(self):
        return self.title


class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "All Video"
        verbose_name_plural = "All Videos"

    def __str__(self):
        return self.title


class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "Published Video"
        verbose_name_plural = "Published Videos"

    def __str__(self):
        return self.title


