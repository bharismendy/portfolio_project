from django import forms


class RechercheArt(forms.Form):
    search_field = forms.CharField(label="",
                                   widget=(forms.TextInput(attrs={'class': 'form-control col-lg-9'})))
    choice_field = forms.ChoiceField(choices=(('tout', 'Tout'),
                                              ('titre', 'Titre'),
                                              ('contenu', 'Contenu'),
                                              ('resume', 'Resume')),
                                     widget=forms.Select(attrs={'class': 'custom-select mb-2 mr-sm-2 mb-sm-0  col-lg-2'}))
