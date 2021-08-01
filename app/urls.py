from django.urls import path

from app.views.books import create_book
from app.views.index import index
from app.views.profiles import create_profile

urlpatterns = (
    # Index
    path('', index, name='index'),

    # User
    path('profile/create/', create_profile, name='create profile'),


    # Book
    path('book/create/', create_book, name='create book'),
)
