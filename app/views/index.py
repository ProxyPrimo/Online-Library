from django.shortcuts import render

from app.common.profile import get_profile
from app.models import Profile, Book
from app.views.profiles import create_profile


def index(request):
    if Profile.objects.exists():
        profile = get_profile()
        books = Book.objects.all()

        ctx = {
            'profile': profile,
            'books': books
        }

        return render(request, 'home-with-profile.html', ctx)
    return create_profile(request)
