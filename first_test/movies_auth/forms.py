from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Enter Your Username', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Enter Your Password', 'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username', 'password')


class SignUpUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Enter Your Password', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Confirm Your Password', 'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        widgets = {
            'username': forms.TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter Your Username'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email'})}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'This email address is already '
                                        u'registered')
        return email


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dob']
        widgets = {
            'dob': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD format'}),
        }

