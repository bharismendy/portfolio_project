from django import forms
from categorie.models import CategorieNiv3


class NewCategorieNiv3(forms.ModelForm):
    class Meta:
        model = CategorieNiv3
        fields = {'nom_categorie', 'cat_sup'}

    def save(self, commit=True):
        cat = super(NewCategorieNiv3, self).save(commit=False)
        if commit:
            cat.save()
            cat.cat_sup.has_sub = True
            cat.cat_sup.save()
