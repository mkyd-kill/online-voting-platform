from django.urls import path
from .views import register
from django.contrib.auth import views as auth

urlpatterns = [
    path('register/', register, name='register'),
    path('accounts/login/', auth.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout')
]