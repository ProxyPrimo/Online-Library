from django.shortcuts import render, redirect

from app.forms.profile import ProfileForm


def create_profile(request):
    if request.method == 'GET':
        ctx = {
            'form': ProfileForm()
        }

        return render(request, 'home-no-profile.html', ctx)
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

    ctx = {
        'form': form
    }

    return render(request, 'home-no-profile.html', ctx)
