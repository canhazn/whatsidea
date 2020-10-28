from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user import forms, models


# Create your views here.
def login(request):

    return render(request, 'user_login.html', {
        'form': forms.UserRegisterForm()
    })

@login_required()
def profileSetting(request):
    context = {
        # 'user': user
    }
    return render(request, 'user_profile_setting.html', context)
