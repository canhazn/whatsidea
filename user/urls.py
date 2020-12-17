from django.urls import path, include
from user import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name="user-login-page"),
    path('register/', views.register, name="user-register-page"),
    path('logout/', auth_views.LogoutView.as_view(next_page="home-page"),
         name="user-logout"),
    path('profile-setting/', views.profileSetting, name="profile-setting-page"),
    path('user/<slug:username>/', views.user_detail, name="user-detail-page"),
    path('user/edit/<slug:username>/', views.user_edit, name="user-edit-page"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('read-notify/', views.read_notify, name="api-read-notify"),
    path('list-notify/', views.list_notify, name="api-list-notify"),
]
