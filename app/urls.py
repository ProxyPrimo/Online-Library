from django.urls import path

from app.views.index import index
from app.views.profiles import create_profile

urlpatterns = (
    path('', index, name='index'),
    path('profile/create/', create_profile, name='create profile')
)
