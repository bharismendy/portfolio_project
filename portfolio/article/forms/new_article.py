from django import forms
from markdownx.fields import MarkdownxFormField
from article.models import Article
from categorie.models import CategorieNiv1, CategorieNiv3, CategorieNiv2


class EditArticle(forms.ModelForm):
    """Form to write an article"""
    titre = forms.CharField(label="Titre", required=True)
    resume = forms.CharField(widget=forms.Textarea(), label="Résumé", required=True)
    content = MarkdownxFormField()
    field_order = titre, resume, content

    class Meta:
        model = Article
        fields = {'image', 'categorie_niv1', 'categorie_niv2', 'categorie_niv3'}

    def save(self, commit=True, user=None):
        """
        function to save the article
        with save it and then and then add the category according to thee documentation
        https://docs.djangoproject.com/fr/2.1/topics/db/examples/many_to_many/
        :param commit: do we register the article ?
        :param user: user to associate to the article
        :return: nothing
        """
        art = super(EditArticle, self).save(commit=False)
        art.content = self.cleaned_data['content']
        art.resume = self.cleaned_data['resume']
        art.categorie_niv1 = self.cleaned_data['categorie_niv1'] or None
        art.categorie_niv2 = self.cleaned_data['categorie_niv2'] or None
        art.categorie_niv3 = self.cleaned_data['categorie_niv3'] or None
        art.personne = user
        art.titre = self.cleaned_data['titre']
        if commit and user:
            art.save()
