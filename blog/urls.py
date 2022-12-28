from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.views.generic import TemplateView

from jobs.views import (home)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view (template_name="home_page/home.html"))
]
