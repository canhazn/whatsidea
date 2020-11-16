from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as loginMethod


def login(request):

    if request.user.is_authenticated:
        return redirect("home-page")

    form = AuthenticationForm(data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                loginMethod(request, user)
                return redirect("home-page")

    return render(request, 'user/user-login.html', {
        'form': form
    })


def register(request):

    if request.user.is_authenticated:
        return redirect("home-page")

    form = forms.UserRegisterForm(data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            loginMethod(request, user,
                        backend='django.contrib.auth.backends.ModelBackend')
            return redirect("home-page")

    return render(request, 'user/user-register.html', {
        'form': form
    })


@login_required()
def profileSetting(request):
    context = {
        # 'user': user
    }
    return render(request, 'user/user-profile-setting.html', context)


def user_detail(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user
    }
    return render(request, 'user/user-detail.html', context)


def user_edit(request, username):

    if request.method == "POST":
        form = forms.UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect("user-detail-page", user.username)
        return render(request, 'user/user-edit.html', {
            'form': form
        })
    else:
        form = forms.UserEditForm(instance=request.user)
        return render(request, 'user/user-edit.html', {
            'form': form
        })
