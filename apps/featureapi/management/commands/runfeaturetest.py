from django.core.management.base import BaseCommand
from all_test_handle import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        test(data)
