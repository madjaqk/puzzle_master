from django.db import models
from django.forms import ModelForm

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    pin = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
    class Meta:
        db_table = "users"

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "pin"]

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ["username"]
