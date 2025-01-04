from django.contrib import admin
from .models import UsersPost


@admin.register(UsersPost)
class UserPostAdmin(admin.ModelAdmin):
    table = ["title", "time_of_creation", "user", "category"]
