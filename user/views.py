from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginMethod


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

    return render(request, 'user-login.html', {
        'loginForm': AuthenticationForm()
    })


def register(request):

    if request.user.is_authenticated:
        return redirect("home-page")

    if request.method == "POST":
        form = forms.UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            loginMethod(request, user)
            return redirect("home-page")

    return render(request, 'user-register.html', {
        'registerForm': forms.UserRegisterForm(),
    })


@login_required()
def profileSetting(request):
    context = {
        # 'user': user
    }
    return render(request, 'user-profile-setting.html', context)
