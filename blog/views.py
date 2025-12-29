
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