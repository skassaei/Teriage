from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from . import forms
from .forms import ChangeEmailForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied

#from django.contrib.auth.forms import UserChangeForm
# Create your views here.

#checks if user is not in a station
def not_station_check(user):
    return not user.groups.filter(name__in=['stations']).exists()

def login_user(request):
    form = forms.LoginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('triage/')

        else:
            messages.success(request,("Error"))
            return redirect('login')
    else:
        return render(request, 'authentication/login.html',context={'form': form})

def logout_user(request):
    logout(request)
    messages.success(request,("Successfully logged out"))
    return redirect('login')

@login_required()
def changeEmail(request):
    if not_station_check(request.user):
        if request.method == "POST":
            form = ChangeEmailForm(request.POST,user=request.user)

            if form.is_valid():
                form.save()
                messages.success(request, 'ایمیل شما با موفقیت تغییر داده شد')
                return redirect("home")
        else:
            form = ChangeEmailForm(instance=request.user)
            args = {'form':form}
            return render(request, 'authentication/edit-email.html', args)
    else:
        raise PermissionDenied

@login_required()
def changePassword(request):
    if not_station_check(request.user):
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()

                return render(request, 'authentication/successfully_changed.html')
            else:
                return render(request, 'authentication/error_change_pass.html')
        else:
            form = PasswordChangeForm(user=request.user)
            args = {'form': form}
            return render(request, 'authentication/change-password.html', args)
    else:
        raise PermissionDenied
