"""docstring for pollsapp tests."""
import datetime
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from .models import Question

client = Client()


def create_question(question_text, days):
    """Create a question and add no. of days to now."""
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    """docstring for QuestionModelTests."""

    def test_was_published_recently_with_future_question(self):
        """Should return false."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """Func returns False for questions whose pub-date is older than 1 day."""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """Func returns True for questions whose pub-date is within the last day."""
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):
    """docstring for QuestionIndexViewTests."""

    def test_no_questions(self):
        """Display appropriate msg if no questions exist."""
        response = self.client.get(reverse('pollsapp:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """Display questions with a pub_date in the past on the index page."""
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('pollsapp:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_future_question(self):
        """Don't display questions with a pub_date in the future on the index page."""
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('pollsapp:index'))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """Display past questions even if both past and future questions exist."""
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('pollsapp:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """The questions index page may display multiple questions."""
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('pollsapp:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
