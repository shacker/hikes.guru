from django import forms
from people.models import UserProfile


class ProfileEditForm(forms.ModelForm):
    '''
    User edits own profile.
    '''

    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    twitter = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    facebook = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    instagram = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'twitter', 'facebook', 'instagram', 'about']