from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login as loginMethod, update_session_auth_hash
from django.contrib import messages


def login(request):

    if request.user.is_authenticated:
        return redirect("home-page")

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                loginMethod(request, user)
                return redirect("home-page")
        return render(request, 'user/user-login.html', {
            'form': form
        })
    else:
        return render(request, 'user/user-login.html', {
            'form': AuthenticationForm()
        })


def register(request):

    if request.user.is_authenticated:
        return redirect("home-page")

    if request.method == "POST":
        form = forms.UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            loginMethod(request, user,
                        backend='django.contrib.auth.backends.ModelBackend')
            return redirect("home-page")

        return render(request, 'user/user-register.html', {
            'form': form
        })
    else:
        return render(request, 'user/user-register.html', {
            'form': forms.UserRegisterForm()
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


@login_required()
def user_edit(request, username):

    if request.method == "POST":
        user_form = forms.UserEditForm(request.POST, instance=request.user)
        profile_form = forms.ProfileForm(
            request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            return redirect("user-detail-page", user.username)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = forms.UserEditForm(instance=request.user)
        profile_form = forms.ProfileForm(instance=request.user.profile)

    return render(request, 'user/user-edit.html', {
        'user_form': user_form,
        "profile_form": profile_form
    })
