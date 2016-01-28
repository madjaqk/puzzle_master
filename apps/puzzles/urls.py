from django.conf.urls import url
from apps.puzzles.views import Home, WhenInRome, ShowPuzzle

urlpatterns = [
    url(r'^$', Home.as_view(), name="puzzles-home"),
    url(r'^(?P<puzzle_name>\w+)$', ShowPuzzle.as_view(), name="show_puzz"),
    url(r'^rooooooome$', WhenInRome.as_view(), name="rome"),
    ]
