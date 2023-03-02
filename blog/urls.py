from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.posts_list_view, name="posts_list"),
    path("post/<int:pk>/", views.post_detail_view, name="post_detail"),
]
