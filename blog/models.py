from django.db import models
from django.utils import timezone

class Post(models.Model):
    CATEGORY_CHOICES = [
        ("debug", "삽질 로그"),
        ("study", "Study"),
        ("project", "Projects"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="study"
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
