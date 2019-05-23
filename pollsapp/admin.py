"""Pollsapp admin file."""
from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """docstring for ChoiceInline."""

    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    """docstring for QuestionAdmin."""

    # The first element of each tuple in fieldsets is the title of the fieldset
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),

    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
