from django import forms
from people.models import UserProfile, DISTANCE_CHOICES


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
    distance_pref = forms.ChoiceField(
        required=False,
        choices=DISTANCE_CHOICES,
        label="Display distances as")
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
        fields = [
            'first_name', 'last_name', 'distance_pref',
            'twitter', 'facebook', 'instagram',
            'about', 'hide_real_name']
