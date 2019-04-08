from django import forms


class RechercheArt(forms.Form):
    """simple form to get 2 value to search an article"""
    search_field = forms.CharField(label="",
                                   widget=(forms.TextInput(attrs={'class': 'form-control col-lg-9'})))
    choice_field = forms.ChoiceField(choices=(('Tout', 'Tout'),
                                              ('Titre', 'Titre'),
                                              ('contenu', 'Contenu'),
                                              ('Resume', 'Resume')),
                                     widget=forms.Select(
                                         attrs={'class': 'custom-select mb-2 mr-sm-2 mb-sm-0  col-lg-2'}))
