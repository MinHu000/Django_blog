from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

from .models import Post
from projects.models import Project


# 🏠 HOME
def home(request):
    debug_count = Post.objects.filter(category="debug").count()
    study_count = Post.objects.filter(category="study").count()
    project_count = Project.objects.count()

    posts = Post.objects.order_by("-created_at")[:3]

    return render(request, "blog/home.html", {
        "debug_count": debug_count,
        "study_count": study_count,
        "project_count": project_count,
        "posts": posts,
    })


# 🧾 전체 글 (필요하면 유지)
def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


def debug_list(request):
    posts = Post.objects.filter(category="debug").order_by("-created_at")
    sandcastle_count = posts.count()

    return render(
        request,
        "blog/debug_list.html",
        {
            "posts": posts,
            "sandcastle_count": sandcastle_count,
        }
    )

def debug_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, category="debug")
    return render(request, "blog/debug_detail.html", {"post": post})


# 📘 STUDY
def study_list(request):
    posts = Post.objects.filter(category="study").order_by("-created_at")
    study_count = posts.count()

    return render(
        request,
        "blog/study_list.html",
        {
            "posts": posts,
            "study_count": study_count,
        }
    )


def study_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, category="study")
    return render(request, "blog/study_detail.html", {"post": post})


# 🗑 DELETE
@staff_member_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("debug_list")
