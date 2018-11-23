from django.contrib import admin

# Register your models here.
from books.models import Book

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Book, BookAdmin)