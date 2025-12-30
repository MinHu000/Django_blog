

# blog/admin.py
from django.contrib import admin
from .models import Post
from django.conf import settings


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")

    class Media:
        css = {
            "all": ("admin/minhu_admin.css",)
        }


admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE