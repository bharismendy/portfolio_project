from django import forms
from categorie.models import CategorieNiv4


class NewCategorieNiv4(forms.ModelForm):
    """used to create form from model"""
    class Meta:
        model = CategorieNiv4
        fields = {'nom_categorie', 'cat_sup'}

    def save(self, commit=True):
        """used to save the model in DB"""
        cat = super(NewCategorieNiv4, self).save(commit=False)
        if commit:
            cat.save()
            cat.cat_sup.has_sub = True
            cat.cat_sup.save()
