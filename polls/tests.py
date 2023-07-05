import datetime
import string

from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.core.management import BaseCommand
from polls.utils import created_question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class UtilsTest(TestCase):
    def test_created_question(self):
        parameter = 3.5
        created_question(parameter)
        self.assertEquals(3, Question.objects.all().count())

    def test_created_question_raise_error_with_wrong_parameter_type(self):
        wrong_parameter = "kfkf"
        with self.assertRaises(ValueError):
            created_question(wrong_parameter)

    def test_created_question_raise_error_with_negative_value(self):
        negative_parameter = -2
        with self.assertRaises(ValueError):
            created_question(negative_parameter)







