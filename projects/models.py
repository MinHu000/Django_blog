from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()

    slug = models.SlugField(unique=True, blank=True)
    # ✅ 썸네일 추가
    thumbnail = models.ImageField(
        upload_to="project_thumbnails/",
        blank=True,
        null=True
    )
    # 🔥 여기 수정
    dashboard_url = models.CharField(
        max_length=200,
        blank=True,
        help_text="내부 대시보드 경로 (/dashboard/ 등)"
    )

    github_url = models.URLField(
        blank=True,
        help_text="GitHub 저장소 URL"
    )

    created_at = models.DateField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
