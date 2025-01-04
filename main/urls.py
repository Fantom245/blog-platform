from django.urls import path
from . import views
from .views import CustomLoginView, PostUpdateViews


urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.post_page, name="post"),
    path("posts/create/", views.create_post, name="create_post"),
    path("posts/<int:pk>/edit/", PostUpdateViews.as_view(), name="edit_post"),
    path("posts/<int:pk>/delete/", views.delete_post, name="delete_post"),
    path("register/", views.register_page, name="register"),
    path('login/', CustomLoginView.as_view(), name="login")
]
