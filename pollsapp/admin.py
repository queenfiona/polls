"""Pollsapp admin file."""
from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    """docstring for QuestionAdmin."""

    # The first element of each tuple in fieldsets is the title of the fieldset
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),

    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
