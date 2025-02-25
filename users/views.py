from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UpdateProfileForm

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = UpdateProfileForm(instance=user)
    return render(request, 'users/profile.html', {'form': form})

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