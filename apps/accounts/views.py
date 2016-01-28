from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from random import randint
from .models import LoginForm, RegisterForm, User
from django.http import HttpResponse

class Register(View):
    def get(self, request):
        return redirect("accounts-login")
    def post(self, request):
        username = request.POST["username"].lower()
        if len(username) < 1:
            messages.error(request, "Please enter a user name", extra_tags="register")
            return redirect("accounts-login")
        already_taken = User.objects.filter(username=username)
        if len(already_taken) > 0:
            messages.error(request, "This user name is already taken", extra_tags="register")
            return redirect("accounts-login")
        else:
            pin = randint(1000,9999)
            new_user = User.objects.create(username=username, pin=pin)
            context = {"username": username, "pin": pin}
            return render(request, "accounts/success.html", context)

class Success(View):
    def get(self, request):
        return render(request, "accounts/success.html")

class LogIn(View):
    login_form = LoginForm
    register_form = RegisterForm
    def get(self, request):
        context = {
            "login_form": self.login_form(),
            "register_form": self.register_form(),
            }
        return render(request, "accounts/login.html", context)
    def post(self, request):
        username, pin = request.POST["username"].lower(), request.POST["pin"]
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User name not found", extra_tags="login")
            return redirect("accounts-login")

        if str(user.pin) != pin:
            print("user.pin: {}".format(user.pin))
            print("pin: {}".format(pin))
            messages.error(request, "Incorrect PIN", extra_tags="login")
            return redirect("accounts-login")
        else:
            request.session["id"] = user.id
            return HttpResponse("Logged in")
 
