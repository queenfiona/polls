"""Pollsapp admin file."""
from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    """docstring for ChoiceInline."""

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """docstring for QuestionAdmin."""

    # The first element of each tuple in fieldsets is the title of the fieldset
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),

    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
