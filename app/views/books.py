from django.shortcuts import render, redirect

from app.common.profile import get_profile
from app.forms.book import BookForm


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
