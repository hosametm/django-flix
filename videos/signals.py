from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import VideoAllProxy


@receiver(pre_save, sender=VideoAllProxy)
def update_published_date(sender, instance, **kwargs):
    if (
        instance.status == "PU"
        and sender.VideoStatusOptions.PUBLISHED
        and instance.published_date is None
    ):
        instance.published_date = timezone.now()
