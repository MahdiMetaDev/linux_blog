# config urls for the project

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # django
    path("admin/", admin.site.urls),

    # local
    path("blog/", include("blog.urls")),
]
