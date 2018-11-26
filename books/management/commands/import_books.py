from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from books.models import Book
from django.core.files import File
from django.template.defaultfilters import slugify


def get_path(file):
    return os.path.join(settings.BASE_DIR, 'books/management/commands/imports/', file)

class Command(BaseCommand):
    help = "Import books from books.csv"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        print('Deleting books!')
        Book.objects.all().delete()
        with open(get_path('books.csv'), 'r') as file:
            reader = csv.DictReader(file)
            i = 0
            for row in reader:
                i += 1
                book = Book(
                    title=row['title'],
                    author=row['author'],
                    series=row['series'],
                    date=row['date'],
                    slug=slugify(row['title']),
                    fantasy=row['fantasy'],
                    scifi=row['scifi'],
                    horror=row['horror'],
                    description=row['description'],
                )
                book.cover.save(row['cover'], File(open(get_path(row['cover']), 'rb')))
                book.save()
        print(f'{i} books imported!')
