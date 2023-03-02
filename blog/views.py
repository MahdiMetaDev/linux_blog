from django.shortcuts import render
from django.http import Http404

from .models import Post


def posts_list_view(request):
    posts = Post.published.all()

    return render(request,
                 "blog/post/list.html",
                 {"posts": posts})


def post_detail_view(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    
    return render(request,
                 "blog/post/detail.html",
                 {"post": post})
