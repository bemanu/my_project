from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.isValid():
            form.save()
            messages.success(request,f'Your account has been created ! You are now able to log in')
            return redirect('/homepage')
    else:
        form = RegisterForm()

    return render(request, 'register/register.html', {'form': form})
