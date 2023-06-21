# authentication/forms.py
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,widget=forms.TextInput(attrs={'class':'input-text'}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'class':'input-text'}))

    class Media:
        css = {
            'all': ('login-form-layout.css',)
        }
        js = (
            'https://some-cdn.com/some-framework.js'
            'login-form-script.js',
        )



class ChangeEmailForm(ModelForm):

    class Meta:
        model = User
        fields = ['email']
