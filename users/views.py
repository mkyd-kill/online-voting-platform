from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UpdateProfileForm
from .models import CustomUser

@login_required
def profile(request):
    user = CustomUser.objects.filter(id=request.user.id).first()
    if request.method == 'POST':
        pass
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