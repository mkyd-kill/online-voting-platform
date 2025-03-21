from django.urls import path
from .views import register, profile, index
from django.contrib.auth import views as auth

urlpatterns = [
    path("", index, name="home"),
    path('register/', register, name='register'),
    path('accounts/login/', auth.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('logout/', auth.LogoutView.as_view(next_page='login'), name='logout')
]