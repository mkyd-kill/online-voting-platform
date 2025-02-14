from django.shortcuts import render, redirect
from .forms import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            if user:
                return redirect("login")
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})