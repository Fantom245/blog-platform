from django.contrib import admin
from django.urls import path
from . import views
from .views import CustomLoginView


urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.post_page),
    path("posts/create/", views.create_post),
    path("posts/edit/", views.edit_post), # Добавить id
    path("posts/delete/<int:pk>/", views.delete_post, name="delete_post"), # Добавить id
    path("register/", views.register_page),
    path('login/', CustomLoginView.as_view()),
    path("profile/", views.user_profile),
    path("category/", views.category_page)
]