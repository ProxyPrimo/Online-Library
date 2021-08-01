from django.shortcuts import render, redirect

from app.common.profile import get_profile
from app.forms.profile import ProfileForm


def create_profile(request):
    if request.method == 'GET':
        ctx = {
            'form': ProfileForm(),
            'user': None
        }

        return render(request, 'home-no-profile.html', ctx)

    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

    ctx = {
        'form': form,
        'user': None
    }

    return render(request, 'home-no-profile.html', ctx)


def details_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        ctx = {
            'profile': profile
        }

        return render(request, 'profile.html', ctx)
