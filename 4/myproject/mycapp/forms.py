from django import forms
from .models import Profile, Preferences


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'date_of_birth', 'hobby', 'previous_workplace']


class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preferences
        fields = '__all__'
