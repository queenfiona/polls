"""pollsapp views."""
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import authenticate, login
from .models import Question, Choice


class IndexView(generic.TemplateView):
    """docstring for IndexView."""

    template_name = 'polls/index.html'


class LatestQuestionView(generic.ListView):
    """docstring for IndexView."""

    template_name = 'polls/question.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions (not those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """docstring for DetailView."""

    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    """docstring for ResultsView."""

    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    """Handle voting for a particular question."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('pollsapp:results',
                                            args=(question.id,)))


def login_view(request):
    """Authenticate users and attach them to current session."""
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('pollsapp:index'))
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
