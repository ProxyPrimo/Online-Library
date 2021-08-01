from django.shortcuts import render, redirect

from app.common.profile import get_profile
from app.forms.book import BookForm
from app.models import Book


def create_book(request):
    # GET
    if request.method == 'GET':
        ctx = {
            'form': BookForm(),
        }

        return render(request, 'add-book-page.html', ctx)

    # POST
    elif request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.profile = get_profile()
            book.save()
            return redirect('index')

        ctx = {
            'form': form
        }

        return render(request, 'add-book-page.html', ctx)


def details_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'GET':
        ctx = {
            'book': book,
            'form': BookForm(instance=book),
        }

        return render(request, 'book-details-page.html', ctx)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'GET':
        ctx = {
            'book': book,
            'form': BookForm(instance=book)
        }

        return render(request, 'edit-book-page.html', ctx)

    elif request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('index')

        ctx = {
            'book': book,
            'form': form
        }

        return render(request, 'edit-book-page.html', ctx)
