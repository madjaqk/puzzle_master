from django.conf.urls import url
from apps.puzzles.views import Home, ShowPuzzle, Check, About

urlpatterns = [
    url(r'^$', Home.as_view(), name="puzzles-home"),
    url(r'^about$', About.as_view(), name="puzzles-about"),
    url(r'^check$', Check.as_view(), name="puzzle-check"),
    url(r'^(?P<puzzle_name>.+)$', ShowPuzzle.as_view(), name="show_puzz"),
    ]
