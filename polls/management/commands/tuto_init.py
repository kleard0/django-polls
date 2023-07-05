from django.core.management import BaseCommand
from polls.utils import created_question


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # print(get_quantity_vote(6))
        created_question(-2)
