from django import forms
from categorie.models import CategorieNiv3


class NewCategorieNiv3(forms.ModelForm):
    """used to create form from model"""
    class Meta:
        model = CategorieNiv3
        fields = {'nom_categorie', 'cat_sup'}

    def save(self, commit=True):
        """used to save the model in DB"""
        cat = super(NewCategorieNiv3, self).save(commit=False)
        cat.has_sub = False
        if commit:
            cat.save()
            cat.cat_sup.has_sub = True
            cat.cat_sup.save()
