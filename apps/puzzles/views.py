from django.shortcuts import render, redirect
from django.views.generic import View

class Home(View):
    def get(self, request):
        return render(request, "puzzles/puzzle_home.html")