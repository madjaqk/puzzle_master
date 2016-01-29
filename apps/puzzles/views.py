from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.views.generic import View
from .models import Puzzle, AnswerAttempt
from apps.accounts.models import User
from hashlib import md5
import re

class Home(View):
    def get(self, request):
        try:
            request.session["id"]
        except:
            return redirect("accounts-login")

        context = {
            "puzzles": sorted(Puzzle.objects.all(), key=lambda x: x.meta_order),
            }
        
        return render(request, "puzzles/puzzle_home.html", context)

class ShowPuzzle(View):
    def get(self, request, puzzle_name):
        try:
            user = User.objects.get(id=request.session["id"])
        except:
            return redirect("accounts-login")
        
        try:
            puzzle = Puzzle.objects.get(short_name = puzzle_name)
        except:
            raise Http404("Puzzle does not exist")

        context = {
            "puzz_id": puzzle.id,
            "name": puzzle.name,
            }

        answers = AnswerAttempt.objects.filter(user=user).filter(puzzle=puzzle)
        answer_list = []

        unsolved = True
        
        if len(answers) > 0:
            for answer in answers:
                is_right = check_answer(answer.answer, puzzle.answer)
                answer_list.append( {"answer": answer.answer, "correct": is_right })
                if is_right:
                    messages.success(request, "{} is correct!".format(answer.answer))
                    unsolved = False
            context["answers"] = answer_list
            
        context["unsolved"] = unsolved

        return render(request, puzzle.url, context)

class Check(View):
    def post(self, request):
        puzzle = Puzzle.objects.get(id=request.POST["id"])
        user = User.objects.get(id=request.session["id"])
        attempt = request.POST["attempt"]

        AnswerAttempt.objects.create(answer=attempt, user=user, puzzle=puzzle)

        if not check_answer(attempt, puzzle.answer):
            messages.error(request, "Sorry, {} is not correct.".format(attempt))
            
        return redirect("/puzzles/" + puzzle.short_name)

def check_answer(attempt, answer_hash):
    only_letters=re.compile(r"[^a-zA-Z]")
    attempt = only_letters.sub("", attempt).lower()
    if md5(bytes(attempt, "utf-8")).hexdigest() == answer_hash:
        return True
    else:
        return False
