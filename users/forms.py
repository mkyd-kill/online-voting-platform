from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'password']