"""Pollsapp models."""
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Question model."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """String method for question model."""
        return self.question_text

    def was_published_recently(self):
        """Recently published questions."""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """Choice model."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """String method for choice model."""
        return self.choice_text
