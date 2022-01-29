from django.shortcuts import render, get_object_or_404

from .models import Project

# Create your views here.

def starting_page(request):
    latest_projects = Project.objects.all().order_by("-date")[:3]
    return render(request, "portfolio/index.html", {
        "projects": latest_projects
    })

def projects(request):
    all_projects = Project.objects.all().order_by("-date")
    return render(request, "portfolio/all-projects.html", {
        "all_projects": all_projects
    })

def project_detail(request, slug):
    identified_project = get_object_or_404(Project, slug=slug)
    return render(request, "portfolio/project-detail.html", {
        "project": identified_project,
        "project_tags": identified_project.tags.all()
    })