# Generated by Django 4.2.6 on 2023-10-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_delete_videoproxy_videoallproxy_videopublishedproxy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
