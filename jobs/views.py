from django.shortcuts import render
from jedi.api import project

from projects.models import Project


# Every view function you create needs to have a context dictionary.

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk=None):
    projects = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
