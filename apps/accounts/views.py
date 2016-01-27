from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.views.generic import View

class Register(View):
    form = forms.UserCreationForm
    def get(self, request):
        context = {"form": self.form()}
        return render(request, "accounts/register.html", context)
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/success")
        else:
            context = {"form": form}
            return render(request, "accounts/register.html", context)

class Success(View):
    def get(self, request):
        return render(request, "accounts/success.html")

class LogIn(View):
    form = forms.AuthenticationForm
    def get(self, request):
        context = {"form": self.form()}
        return render(request, "accounts/login.html", context)
    def post(self, request):
        form = self.form(None, request.POST)
        context = {"form": form}
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/accounts/success")
            else:
                return render(request, "accounts/login.html")
        else:
            return render(request, "accounts/login.html", context)
