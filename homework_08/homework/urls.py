from django.urls import path

from .views import IndexView, PostsListView, PostDetailsView, create_posts

app_name = "homework"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/", PostsListView.as_view(), name="posts"),
    path("posts/createposts/", create_posts, name="create-posts"),
    path("posts/<int:pk>/", PostDetailsView.as_view(), name="post"),
]
