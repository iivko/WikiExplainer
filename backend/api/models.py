from django.db import models


class Explanation(models.Model):
    topic = models.CharField(
        max_length=256,
        blank=False,
        null=False
    )

    text = models.JSONField(
        blank=False,
        null=False
    )

    image_url = models.URLField(
        blank=False,
        null=False
    )


    def __str__(self):
        return self.topic
