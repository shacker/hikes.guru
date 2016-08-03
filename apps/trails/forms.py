from django import forms
from trails.models import Trail


class TrailEditForm(forms.ModelForm):
    '''
    User edits one of their trails.
    '''

    class Meta:
        model = Trail
        fields = [
            'title', 'region', 'description', 'trackfile', 'distance', 'ascent', 'calories', 'duration', 'geocaches',
            'public', 'trail_type'
            ]
