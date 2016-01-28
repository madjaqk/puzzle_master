from django.db import models

class Puzzle(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20)
    url = models.CharField(max_length=255)
    answer = models.CharField(max_length=32) # Maybe something else, if hashed
    meta_order = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "puzzles"

class AnswerAttempt(models.Model):
    answer = models.CharField(max_length=255)
    user = models.ForeignKey("accounts.User")
    puzzle = models.ForeignKey("Puzzle")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.answer
    class Meta:
        db_table = "answers"
