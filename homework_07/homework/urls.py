from django.urls import path

from .views import index_page, posts_view

app_name = "homework"

urlpatterns = [
    path("", index_page, name="index"),
    path("posts/", posts_view, name="posts"),
]
