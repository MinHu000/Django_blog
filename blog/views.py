from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


def debug_list(request):
    posts = Post.objects.filter(category="debug").order_by("-created_at")
    return render(request, "blog/debug_list.html", {"posts": posts})


def debug_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, category="debug")
    return render(request, "blog/debug_detail.html", {"post": post})


from django.shortcuts import get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()

    # 삭제 후 돌아갈 위치
    return redirect("debug_list")


def study_list(request):
    posts = Post.objects.filter(category="study").order_by("-created_at")
    return render(request, "blog/study_list.html", {
        "posts": posts
    })


def study_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, category="study")
    return render(request, "blog/study_detail.html", {
        "post": post
    })


def debug_list(request):
    posts = Post.objects.filter(category="debug").order_by("-created_at")
    sandcastle_count = posts.count()

    return render(request, "blog/debug_list.html", {
        "posts": posts,
        "sandcastle_count": sandcastle_count,
    })


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


from django.shortcuts import render
from blog.models import Post
from projects.models import Project


def home(request):
    debug_count = Post.objects.filter(category="debug").count()
    study_count = Post.objects.filter(category="study").count()
    project_count = Project.objects.count()

    posts = Post.objects.order_by("-created_at")[:3]  # ✅ 추가된 부분 (이거 하나)

    return render(request, "blog/home.html", {
        "debug_count": debug_count,
        "study_count": study_count,
        "project_count": project_count,
        "posts": posts,  # ✅ 추가된 부분 (이거 하나)
    })
