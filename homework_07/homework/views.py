from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from homework.models import Post


# Create your views here.
def index_page(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="homework/index.html",
        context={},
    )


def posts_view(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    print(posts)
    return render(
        request=request,
        template_name="homework/post.html",
        context={
            "posts": posts,
        },
    )
