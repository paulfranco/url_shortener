from django.core.management.base import BaseCommand, CommandError
from shorterner.models inport LftURL

class Command(BaseCommand):
    help = 'Refreshes att LftURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)
        parser.add_argument('number2', type=int)
        parser.add_argument('number3', type=int)



    def handle(self, *args, **options):
        return UlfURL.objects.refresh_shortcodes(items=options['items'])
