from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    # path("", views.posts_list_view, name="posts_list"),
    path("", views.PostListView.as_view(), name="posts_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail_view,
        name="post_detail"),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
]
