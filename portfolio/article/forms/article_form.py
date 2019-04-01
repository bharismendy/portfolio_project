from django import forms
from markdownx.fields import MarkdownxFormField
from article.models import Article
from categorie.models import CategorieNiv1, CategorieNiv2, CategorieNiv3


class EditArticle(forms.Form):
    """Form to write or edit an article"""
    def __init__(self, article=None, *args, **kwargs):
        try:
            self.article = article
        except Exception as error:
            self.article=None
            print(error)
        super(EditArticle, self).__init__(*args, **kwargs)
        titre_value = None
        resume_value = None
        content_value = None
        categorie_niv1_value = None
        categorie_niv2_value = None
        categorie_niv3_value = None
        image_value = None

        if hasattr(self.article, 'titre'):
            titre_value = self.article.titre

        if hasattr(self.article, 'resume'):
            resume_value = self.article.resume

        if hasattr(self.article, 'content'):
            content_value = self.article.content

        if hasattr(self.article, 'categorie_niv1'):
            categorie_niv1_value = self.article.categorie_niv1

        if hasattr(self.article, 'categorie_niv2'):
            categorie_niv2_value = self.article.categorie_niv2

        if hasattr(self.article, 'categorie_niv3'):
            categorie_niv3_value = self.article.categorie_niv3

        if hasattr(self.article, 'image'):
            image_value = self.article.image

        self.fields['image'] = forms.ImageField()

        self.fields['categorie_niv1'] = forms.ModelChoiceField(initial=categorie_niv1_value,
                                                               queryset=CategorieNiv1.objects.all())

        self.fields['categorie_niv2'] = forms.ModelChoiceField(initial=categorie_niv2_value,
                                                               queryset=CategorieNiv2.objects.all())

        self.fields['categorie_niv3'] = forms.ModelChoiceField(initial=categorie_niv3_value,
                                                               queryset=CategorieNiv3.objects.all())

        self.fields['titre'] = forms.CharField(label="Titre",
                                               required=True,
                                               initial=titre_value)

        self.fields['resume'] = forms.CharField(widget=(forms.Textarea()),
                                                initial=resume_value,
                                                label="Résumé",
                                                required=True)

        self.fields['content'] = MarkdownxFormField(initial=content_value)

    def save(self, commit=True, user=None):
        """
        function to save the article
        with save it and then and then add the category according to thee documentation
        https://docs.djangoproject.com/fr/2.1/topics/db/examples/many_to_many/
        :param commit: do we register the article ?
        :param user: user to associate to the article
        :return: nothing
        """
        print(self.cleaned_data['image'])
        art = super(EditArticle, self).save(commit=False)
        art.content = self.cleaned_data['content']
        art.resume = self.cleaned_data['resume']
        art.categorie_niv1 = self.cleaned_data['categorie_niv1'] or None
        art.categorie_niv2 = self.cleaned_data['categorie_niv2'] or None
        art.categorie_niv3 = self.cleaned_data['categorie_niv3'] or None
        art.image = self.cleaned_data['image'] or None
        art.personne = user
        art.titre = self.cleaned_data['titre']
        if commit and user:
            art.save()
