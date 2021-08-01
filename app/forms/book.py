from django import forms

from app.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('profile',)

