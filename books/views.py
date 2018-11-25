from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.core.mail import EmailMessage
from django.template.loader import get_template
from books.models import Book
from books.forms import BookForm, ContactForm


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {
        'books': books
    })

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {
        'book': book,
    })

@login_required
def edit_book(request, slug):
    book = Book.objects.get(slug=slug)
    if book.creator != request.user:
        raise Http404
    form_class = BookForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', slug=book.slug)
    else:
        form = form_class(instance=book)

    return render(request, 'books/edit_book.html', {
        'book': book,
        'form': form,
    })

def create_book(request):
    form_class = BookForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.creator = request.user
            book.slug = slugify(book.title)
            book.save()
            return redirect('book_detail', slug=book.slug)
    else:
        form = form_class()

    return render(request, 'books/create_book.html', {
        'form': form,
    })

def browse_by_title(request, initial=None):
    if initial:
        books = Book.objects.filter(title__istartswith=initial).order_by('title')
    else:
        books = Book.objects.all().order_by('title')

    return render(request, 'search.html', {
        'books': books,
        'initial': initial,
    })

def browse_by_category(request, category):
    if category:
        books = Book.objects.filter(category=True)
    else:
        books = Book.objects.all().order_by('title')

    categories = ('is_fantasy', 'is_scifi', 'is_horror')

    return render(request, 'search.html', {
        'books': books,
        'category': category,
        'categories': categories
    })

def contact(request):
    form_class = ContactForm

    if request.method == "POST":
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            template = get_template('contact_template.txt')

            content = template.render({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })

            email = EmailMessage(
                'New contact form submission',
                content,
                'Your website <h1@example.com>',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })
