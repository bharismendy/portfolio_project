from django import forms
from categorie.models import CategorieNiv2


class NewCategorieNiv2(forms.ModelForm):
    """create a form from the model"""
    class Meta:
        model = CategorieNiv2
        fields = {'nom_categorie', 'cat_sup'}

    def save(self, commit=True):
        """used to save the model in DB"""
        cat = super(NewCategorieNiv2, self).save(commit=False)
        cat.has_sub = False
        if commit:
            cat.save()
            cat.cat_sup.has_sub = True
            cat.cat_sup.save()
