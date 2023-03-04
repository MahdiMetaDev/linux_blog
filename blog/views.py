from django.shortcuts import render, get_object_or_404
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic

from .models import Post


# def posts_list_view(request):
    
#     posts_list = Post.published.all()

#     # Pagination with 3 posts per page
#     paginator = Paginator(posts_list, 3)
#     page_number = request.GET.get("page", 1)

#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         # If page_number is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page_number is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
    
#     return render(request,
#                  "blog/posts_list.html",
#                  {"posts": posts})


class PostListView(generic.ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/posts_list.html"


def post_detail_view(request, year, month, day, post):

    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    
    return render(request,
                 "blog/post_detail.html",
                 {"post": post})
