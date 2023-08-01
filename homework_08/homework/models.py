from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
