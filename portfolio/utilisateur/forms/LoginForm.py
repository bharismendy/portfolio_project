from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """formulaire that allow to log the user"""
    identifiant = forms.CharField(label="identifiant", max_length=100)
    mot_de_passe = forms.CharField(label='mot de passe', widget=forms.PasswordInput)
    captcha = CaptchaField()
