from django import forms
from trails.models import Trail


class TrailEditForm(forms.ModelForm):
    '''
    User edits one of their trails.
    '''

    class Meta:
        model = Trail
        fields = [
            'title', 'region', 'country', 'description', 'trackfile', 'distance', 'ascent',
            'calories', 'duration', 'geocaches', 'public', 'trail_type', 'activity_type',
            'difficulty', 'season', 'directions',
            ]


class TrailDeleteForm(forms.Form):
    '''
    User deletes own trail.
    '''

    confirm = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
