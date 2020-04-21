from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

from django.contrib.auth import (
    authenticate,
    login,
    logout,
    models,
)
from .forms import UserLoginForm, UserRegisterForm

#User = get_user_model()

def login_view(request):
    form1 = UserLoginForm(request.POST or None)

    if form1.is_valid():
        username = form1.cleaned_data.get("username")
        password = form1.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        user1 = User.objects.get(username=username)
        if not request.user.is_staff:
            if user1.is_staff:
                login(request, user)
                return redirect("/adminhome/")
            login(request, user)
            return redirect("/car/newcar/")
    return render(request, "form.html", {"form": form1, "title": "Login"})

def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()

        return redirect("/login/")
    context = {
        "title" : "Registration",
        "form": form,
    }
    return render(request, "form.html", context)

def logout_view(request):
    logout(request)
    return render(request, "home.html", {})

