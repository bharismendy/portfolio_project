from django import forms
from markdownx.fields import MarkdownxFormField
from article.models import Article


class EditArticle(forms.ModelForm):
    titre = forms.CharField(label="Titre", required=True)
    content = MarkdownxFormField()

    class Meta:
        model = Article
        fields = {'image'}

    def save(self, commit=True, user=None):
        art = super(EditArticle, self).save(commit=False)
        art.content = self.cleaned_data['content']
        art.personne = user
        art.titre = self.cleaned_data['titre']
        if commit and user:
            art.save()
