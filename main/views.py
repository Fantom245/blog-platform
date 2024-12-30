from django.shortcuts import render, redirect

from .models import UsersPost
from .forms import UsersPostForm
from .form_regiter import CustomUserCreationForm

from django.contrib.auth.views import LoginView

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):
        template_name = 'main/login_page.html'


def index(request):
    posts = UsersPost.objects.all()
    return render(request, "main/index.html", {"posts": posts, "user": request.user})


def post_page(request):
    return render(request, "main/create_post.html")


def create_post(request):
    error = ""
    if request.method == "POST":
        form = UsersPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return redirect("/")
        else:
            error = "Форма була невірною"


    form = UsersPostForm()

    data = {
        "form": form,
        "error": error,
        "post": post if request.method == "POST" and form.is_valid() else None
    }

    return render(request, "main/create_post.html", data)


def edit_post(request):
    return render(request, "main/edit_post.html")


@login_required
def delete_post(request, pk):
    post = get_object_or_404(UsersPost, pk=pk)
    
    if request.method == 'POST':
        if request.user == post.user:
            post.delete()
            return redirect('index')
    return render(request, 'confirm_delete.html', {'post': post})


def register_page(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
    else:
        form = CustomUserCreationForm()

    return render(request, "main/register_page.html", {'form': form})


# def login_page(request):
#     return render(request, "main/login_page.html")


def user_profile(request):
    return render(request, "main/user_profile.html")


def category_page(request):
    return render(request, "main/category_page.html")
