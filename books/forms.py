from django import forms
from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description')

class ModelFormWithFileField(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.ImageField()
