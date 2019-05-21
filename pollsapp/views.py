"""pollsapp views."""
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question


def index(request):
    """Index function."""
    latest_question_list = Question.objects.order_by('-pub_date')[0:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """Display question text with a form to vote."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    """Display results for a particular question."""
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    """Handle voting for a particular question."""
    return HttpResponse("You're voting on question %s." % question_id)
