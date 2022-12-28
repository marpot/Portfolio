from tempfile import template

from django.shortcuts import render
from jedi.api import project
from django.http import HttpResponse
from django.template import loader, context




# Every view function you create needs to have a context dictionary.

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return HttpResponse(template.render(context, request))


def project_detail(request, pk=None):
    projects = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html')


def home(request):
    return HttpResponse(template.render(context, request))