from django import forms

class ShortenURLForm(forms.Form):
    url = forms.URLField(label='Your website', required=True,
                        widget=forms.TextInput(attrs={'placeholder': 'Your website'}))
