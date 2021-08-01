from django.shortcuts import render, redirect

from app.common.profile import get_profile
from app.forms.profile import ProfileForm, ProfileDeleteForm
from app.models import Profile


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


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileForm(instance=profile)
        ctx = {
            'form': form,
            'profile': profile
        }

        return render(request, 'edit-profile-page.html', ctx)

    elif request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

        ctx = {
            'form': form,
            'profile': profile
        }

        return render(request, 'edit-profile-page.html', ctx)

def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)

        ctx = {
            'form': form
        }

        return render(request, 'delete-profile-page.html', ctx)

    if request.method == 'POST':
        Profile.delete(profile)
        return redirect('index')
