import django.contrib.auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from library.settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
from vault.forms import RegisterForm
from .models import User


# Create your views here.
@login_required
def account(request):
    return render(request, 'account.html', {'user': request.user})


def login(request):
    next = request.GET.get('next') or request.POST.get(
        'next') or LOGIN_REDIRECT_URL
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = django.contrib.auth.authenticate(username=username,
                                                    password=password)
            if user:
                django.contrib.auth.login(request, user)
                return redirect(next)
            else:
                # Username or password wrong
                messages.error(request, "Login information is incorrect.")
                return render(request, 'login.html')
        else:
            # Username or password not given
            messages.error(request, "Login information is incomplete.")
            return render(request, 'login.html')
    else:
        # First time
        return render(request, 'login.html')


def logout(request):
    next = request.GET.get('next') or request.POST.get(
        'next') or LOGOUT_REDIRECT_URL
    django.contrib.auth.logout(request)
    return redirect(next)


def register(request):
    if request.method == 'POST':
        # Data has been submitted
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'],
                                            cd['email'],
                                            cd['password'])
            user = django.contrib.auth.authenticate(username=cd['username'],
                                                    password=cd['password'])
            if user:
                django.contrib.auth.login(request, user)
                return redirect(reverse('home'))
            else:
                # Should never happen!
                assert False
    else:
        # First time
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
