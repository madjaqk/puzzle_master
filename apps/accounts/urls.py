from django.conf.urls import url
from apps.accounts.views import Register, Success, LogIn

urlpatterns = [
    url(r'^login/?$', LogIn.as_view(), name="accounts-login"),
    url(r'^register/$', Register.as_view(), name="accounts-register"),
    url(r'^success[/]?', Success.as_view(), name="accounts-success"),
    ]
