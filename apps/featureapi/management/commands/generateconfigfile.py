from django.core.management.base import BaseCommand
from create_conf import *


class Command(BaseCommand):

     def handle(self, *args, **options):
         load_feature_conf()