from django.db import models
from django.contrib.auth.models import User


class UsersPost(models.Model):
    """База данних з користувачами та постами"""
    title = models.CharField(max_length=30)
    content = models.TextField()
    time_of_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
