import json

from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest

from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView, RedirectView
import requests
from homework.models import Post


POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


# Create your views here.
class IndexView(TemplateView):
    template_name = "homework/index.html"


class PostsListView(ListView):
    template_name = "homework/post.html"
    context_object_name = "posts"
    queryset = Post.objects.all()


def create_posts(request: HttpRequest) -> HttpResponse:
    data = fetch_posts_data()
    user = get_user(request)
    for post in data[:11]:
        new_post = Post(
            title=post["title"],
            body=post["body"],
            user=user,
        )
        new_post.save()
    return redirect("homework:posts")


class PostDetailsView(DetailView):
    model = Post


def fetch_posts_data(url: str = POSTS_DATA_URL):
    data = json.loads(requests.get(url).text)
    return data
