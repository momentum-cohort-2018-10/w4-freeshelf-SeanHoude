from django.contrib import admin

# Register your models here.
from books.models import Book

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'author', 'description', 'slug', 'date', 'creator', 'cover', 'favorited', 'fantasy', 'scifi', 'horror', )
    prepopulated_fields = {'slug': ('title',)}

# class SocialAdmin(admin.ModelAdmin):
#     model = Social
#     list_display = ('network', 'username',)

admin.site.register(Book, BookAdmin)
# admin.site.register(Social, SocialAdmin)