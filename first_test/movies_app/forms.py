from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['vote'].widget.attrs.update(
            {'class': 'form-control'})

    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Movie name'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control narrow-select',
                'placeholder': 'Enter some description',
                'style': 'height:50px'}),
            'release_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD format'}),
            'duration': forms.TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'HH:MM format'}),
        }


