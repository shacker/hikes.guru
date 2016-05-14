from django import forms
from feedback.models import Feedback, FEEDBACK_TYPE_CHOICES


class FeedbackForm(forms.ModelForm):
    '''
    Simple user feedback form.
    '''

    feedback_type = forms.ChoiceField(choices=FEEDBACK_TYPE_CHOICES, required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
    subject = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(required=True,
        widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Feedback
        fields = ['feedback_type', 'subject', 'body']
