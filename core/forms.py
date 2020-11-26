from core import models
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class UserEditForm(UserChangeForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['bio', 'phone']


class IdeaCreateForm(forms.ModelForm):
    class Meta:
        model = models.Idea
        fields = ["title", "problem", "solution", "description"]


class IdeaEditForm(forms.ModelForm):
    class Meta:
        model = models.Idea
        fields = ["title", "slug", "problem", "solution", "description",
                  "is_publish", "address", "phone", "website"]


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["idea", "user", "content"]
