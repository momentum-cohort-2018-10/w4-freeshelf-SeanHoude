from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from books.models import Book
from django.core.files import File

def get_path(file):
    return os.path.join(settings.BASE_DIR, 'initial_data', file)

class Command(BaseCommand):
    help = "Load books from book_data/books.csv"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        print('Deleting books!')
        # Book.objects.all().delete()
        with open(get_path('books.csv'), 'r') as file:
            reader = csv.DictReader(file)
            i = 0
            for row in reader:
                i += 1
                book = Book(
                    title=row['title'],
                    description=row['description'],
                    language=row['language'],
                    author=row['author'],
                )
                book.cover.save(row['image'],
                    File(open(get_path(row['image']), 'rb')))
                book.save()
        print(f'{i} books imported!')
