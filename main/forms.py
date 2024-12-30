from .models import UsersPost
from django.forms import ModelForm, TextInput, Textarea

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UsersPostForm(ModelForm):
    class Meta:
        model = UsersPost
        fields = ["title", "content", "category"]

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Заголовок"
            }),
            "content": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Змітс"
            }),
            "category": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Категорія"
            })
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
