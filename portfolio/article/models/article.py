from django.db import models
from utilisateur.models import Personne
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from categorie.models import CategorieNiv1, CategorieNiv2, CategorieNiv3


class Article (models.Model):
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    resume = models.CharField(max_length=200, null=False, default=None)
    titre = models.CharField(max_length=100, null=False, default=None)
    content = MarkdownxField()
    categorie_niv1 = models.ForeignKey(CategorieNiv1, on_delete=models.CASCADE, default=None, null=True)
    categorie_niv2 = models.ForeignKey(CategorieNiv2, on_delete=models.CASCADE, default=None, null=True)
    categorie_niv3 = models.ForeignKey(CategorieNiv3, on_delete=models.CASCADE, default=None, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="image_projet/")

    @property
    def formatted_resume_markdown(self):
        return markdownify(self.resume)
    @property
    def formatted_content_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return "article de " + self.personne.user.username

