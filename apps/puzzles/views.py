from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View

class Home(View):
    def get(self, request):
        return render(request, "puzzles/puzzle_home.html")

class WhenInRome(View):
    def get(self, request):
        return render(request, "puzzles/when-in-rome.html")

class ShowPuzzle(View):
    def get(self, request, puzzle_name):
        if puzzle_name=="rome":
            puzz_url = "puzzles/when-in-rome.html"
            return render(request, puzz_url)
        else:
            return HttpResponse("Puzzle not found")
