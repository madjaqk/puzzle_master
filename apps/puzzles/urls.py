from django.conf.urls import url
from apps.puzzles.views import Home

urlpatterns = [
    url(r'^$', Home.as_view(), name="puzzles-home"),
    ]
