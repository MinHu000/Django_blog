from django.urls import path
from . import views

urlpatterns = [
    # 🛠 Debug
    path("debug/", views.debug_list, name="debug_list"),
    path("debug/<int:pk>/", views.debug_detail, name="debug_detail"),

    # 📘 Study
    path("study/", views.study_list, name="study_list"),
    path("study/<int:pk>/", views.study_detail, name="study_detail"),

    # 🗑 Delete
    path("post/<int:pk>/delete/", views.post_delete, name="post_delete"),
]
