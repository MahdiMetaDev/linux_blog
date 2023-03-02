from django.shortcuts import render, get_object_or_404

from .models import Post


def posts_list_view(request):
    posts = Post.published.all()

    return render(request,
                 "blog/posts_list.html",
                 {"posts": posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    
    return render(request,
                 "blog/post_detail.html",
                 {"post": post})
