from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post


def posts_list_view(request):
    
    posts_list = Post.published.all()

    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get("page", 1)
    posts = paginator.page(page_number)
    
    return render(request,
                 "blog/posts_list.html",
                 {"posts": posts})


def post_detail_view(request, year, month, day, post):

    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    
    return render(request,
                 "blog/post_detail.html",
                 {"post": post})
