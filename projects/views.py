from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project


def project_list(request):
    projects = Project.objects.all().order_by("-created_at")
    return render(request, "projects/project_list.html", {
        "projects": projects
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "projects/project_detail.html", {
        "project": project
    })


# ✅ 프로젝트 삭제 (Admin만 가능)
@login_required
def project_delete(request, slug):
    project = get_object_or_404(Project, slug=slug)

    # 관리자만 삭제 허용
    if not request.user.is_staff:
        return redirect("project_list")

    if request.method == "POST":
        project.delete()
        return redirect("project_list")

    return render(request, "projects/project_confirm_delete.html", {
        "project": project
    })

def project_list(request):
    projects = Project.objects.all().order_by("-created_at")
    project_count = projects.count()

    return render(
        request,
        "projects/project_list.html",
        {
            "projects": projects,
            "project_count": project_count,
        }
    )
