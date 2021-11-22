from .forms import SignupForm
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import UniUser as User


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        username = request.POST["email"]
        password = request.POST["password"]
        # url = request.POST["url"]

        user = authenticate(request, username=username, password=password)
        # user = User.objects.get(username=username)
        if user is not None:
            # if user.check_password(raw_password=password):
            login(request, user)
            try:
                # next_url = url.split('=')[1]
                # return HttpResponseRedirect(next_url)
                return HttpResponseRedirect('/')
            except Exception as e:
                return redirect('home')
        else:
            messages.error(
                request,
                "Please use correct credential to login.",
            )
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')


@login_required
def logout(request):
    # logout(request)
    request.session.flush()
    return redirect('home')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            if not User.objects.filter(username=request.POST.get('email')).exists():
                form = SignupForm(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.is_active = True
                    user.set_password(form.cleaned_data["password"])
                    user.username = form.cleaned_data["email"]
                    user.save()
                    messages.success(request, "Registation successfully completed! Please login.", )
                    return redirect('login')
                else:
                    errors = ''
                    for field in form:
                        for error in field.errors:
                            errors += '| '+field.name.replace('_', ' ').title() + ' | '
                    messages.error(
                        request, 'Required Fields: ' + errors)
                    return render(request, 'users/registration.html')
            else:
                messages.error(
                    request, "Please use correct email. This user already exsit!", )
                return render(request, 'users/registration.html')
        else:
            return render(request, 'users/registration.html')
