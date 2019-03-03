from django import forms
from utilisateur.models import Personne


class EditUserProfile(forms.Form):
    """form to allow the user to edit himself is data"""
    def __init__(self, user=None, *args, **kwargs):
        try:
            self.user = user
        except Exception as error:
            self.user=None
            print(error)
        super(EditUserProfile, self).__init__(*args, **kwargs)
        first_name = None
        last_name = None
        email = None
        age = None
        site_web = None
        avatar = None
        signature = None

        if hasattr(self.user, 'first_name'):
            first_name = self.user.first_name

        if hasattr(self.user, 'last_name'):
            last_name = self.user.last_name

        if hasattr(self.user, 'email'):
            email = self.user.email
        try:
            if hasattr(self.user.personne, 'age'):
                age = self.user.personne.age

            if hasattr(self.user.personne, 'site_web'):
                site_web = self.user.personne.site_web

            if hasattr(self.user.personne, 'avatar'):
                avatar = self.user.personne.avatar

            if hasattr(self.user.personne, 'signature'):
                signature = self.user.personne.signature
        except():
            self.user.personne = Personne(user=self.user)
            self.user.personne.save()

        self.fields['first_name'] = forms.CharField(label="first name", required=False, widget=(forms.TextInput(
                                                    attrs={'value': first_name or None})))
        self.fields['last_name'] = forms.CharField(label="last name", required=False, widget=(forms.TextInput(
                                                   attrs={'value': last_name or None})))
        self.fields['email'] = forms.CharField(label="email", required=False, widget=(forms.TextInput(
                                               attrs={'value': email or None})))
        self.fields['age'] = forms.IntegerField(label="Age", required=False, widget=(forms.TextInput(
                                               attrs={'value': age or 0})))
        self.fields['site_web'] = forms.CharField(label="site web", required=False, widget=(forms.TextInput(
                                                     attrs={'value': site_web or None})))
        self.fields['avatar'] = forms.ImageField(label="avatar", required=False)
        self.fields['signature'] = forms.CharField(label="signature", required=False, widget=(forms.TextInput(
                                                     attrs={'value': signature or None})))

    def save(self):
        data = self.cleaned_data
        utilisateur = self.user
        utilisateur.first_name = data['first_name']
        utilisateur.last_name = data['last_name']
        utilisateur.email = data['email']
        utilisateur.personne.age = data['age']
        utilisateur.personne.site_web = data['site_web']
        utilisateur.personne.avatar = data['avatar']
        utilisateur.personne.signature = data['signature']
        utilisateur.save()
        utilisateur.personne.save()
