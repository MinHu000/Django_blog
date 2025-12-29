from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("debug/", views.debug_list, name="debug_list"),
    path("debug/<int:pk>/", views.debug_detail, name="debug_detail"),
    path("post/<int:pk>/delete/", views.post_delete, name="post_delete"),
    path("study/", views.study_list, name="study_list"),
    path("study/<int:pk>/", views.study_detail, name="study_detail"),

]
