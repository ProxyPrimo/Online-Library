from django.urls import path

from app.views.books import create_book, edit_book, details_book
from app.views.index import index
from app.views.profiles import create_profile, details_profile

urlpatterns = (
    # Index
    path('', index, name='index'),

    # User
    path('profile/create/', create_profile, name='create profile'),
    path('profile/', details_profile, name='details profile'),


    # Book
    path('book/create/', create_book, name='create book'),
    path('book/edit/<int:pk>/', edit_book, name='edit book'),
    path('book/details/<int:pk>/', details_book, name='details book'),
)
