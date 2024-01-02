from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Preferences
from .forms import ProfileForm, PreferenceForm


def profile_list(request):
    profile = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profile})


def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profile_detail.html', {'profile': profile})


def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {'form': form})


def profile_update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_form.html', {'form': form})


def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.delete()
    return redirect('profile_list')


def prefences_list(request):
    prefences = Preferences.objects.all()
    return render(request, 'preferences_list.html', {'preferencess': prefences})


def preferences_detail(request, pk):
    preferences_detail = get_object_or_404(Preferences, pk=pk)
    return render(request, 'preferences_detail.html', {'preferences': preferences_detail})


def preferences_create(request):
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('preferences_list')
    else:
        form = PreferenceForm()
    return render(request, 'preferences_form.html', {'form': form})


def preferences_edit(request, pk):
    preferences_edit = get_object_or_404(Preferences, pk=pk)
    if request.method == 'POST':
        form = PreferenceForm(request.POST, instance=preferences_edit)
        if form.is_valid():
            form.save()
            return redirect('preferences_list')
    else:
        form = PreferenceForm(instance=preferences_edit)
    return render(request, 'preferences_form.html', {'form': form})


def preferences_delete(request, pk):
    preferences = get_object_or_404(Preferences, pk=pk)

    preferences.delete()
    return redirect('preferences_list')
