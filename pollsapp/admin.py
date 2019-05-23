"""Pollsapp admin file."""
from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    """docstring for QuestionAdmin."""

    fields = ['pub_date', 'question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
