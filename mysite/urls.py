from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🔐 Auth
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # 🏠 Home (메인)
    path("", blog_views.home, name="home"),

    # 🛠 Debug / 📘 Study
    path("", include("blog.urls")),

    # 🚀 Projects
    path("projects/", include("projects.urls")),

    # 📄 Pages
    path("", include("pages.urls")),

    # 🔧 Admin
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
