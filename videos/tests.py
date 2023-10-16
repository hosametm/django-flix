from django.test import TestCase
from .models import Video


# Create your tests here.

class VideoModelTestCase(TestCase):
    def setUp(self):
        Video.objects.create(title="This is my title", description="This is my description", slug="this-is-my-title",
                             video_id="123456789")

    def test_valid_title(self):
        qs = Video.objects.filter(title="This is my title")
        self.assertTrue(qs.exists())

    def test_created_count(self):
        qs = Video.objects.all()
        self.assertEqual(qs.count(), 1)
