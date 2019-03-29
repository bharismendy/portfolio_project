from django import forms
from categorie.models import CategorieNiv1


class NewCategorieNiv1(forms.ModelForm):
    class Meta:
        model = CategorieNiv1
        fields = {'nom_categorie'}

    def save(self, commit=True):
        cat = super(NewCategorieNiv1, self).save(commit=False)
        cat.has_sub = False
        if commit:
            cat.save()

