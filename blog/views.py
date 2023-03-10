from django.shortcuts import render, get_object_or_404
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.core.mail import send_mail

from environs import Env

from .models import Post
from .forms import EmailPostForm


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


def post_share(request, post_id):
    
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    env = Env()
    env.read_env()
    sent = False
    form = EmailPostForm()

    if request.method == "POST":

        form = EmailPostForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url)
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n {cd['name']}\'s comments: " \
                        f"{cd['comments']}"
            send_mail(subject, message, env("DJANGO_EMAIL_HOST_USER"), [cd['to']])
            sent = True

        else:
            form = EmailPostForm()    
        
    return render(request, "blog/post_share.html", {
        "post": post,
        "form": form,
        "sent": sent,
    })
