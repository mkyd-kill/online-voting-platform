from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            