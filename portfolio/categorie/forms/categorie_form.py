from django import forms
from categorie.models import Categorie


class CategorieForm(forms.ModelForm):
    """create a form from the model"""

    class Meta:
        model = Categorie
        exclude = ['niv_cat', 'has_sub']

    def save(self, commit=True):
        """used to save the object in DB"""
        cat = super(CategorieForm, self).save(commit=False)
        cat.niv_cat = 1
        if commit:
            cat.save()
            if self.cleaned_data['cat_sup']:
                cat.cat_sup.has_sub = True
                cat.niv_cat = cat.cat_sup.niv_cat + 1
                cat.save()
                cat.cat_sup.save()

