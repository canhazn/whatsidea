from django.urls import path
from user import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name="user-login-page"),
    path('logout/', auth_views.LogoutView.as_view(next_page="home-page"), name="user-logout"),
    path('profile-setting/', views.profileSetting, name="profile-setting-page")
]
