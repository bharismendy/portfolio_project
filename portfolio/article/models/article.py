from django.db import models
from utilisateur.models import Personne
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from categorie.models import Categorie


class Article (models.Model):
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    content = MarkdownxField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="image_projet/")

    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return "article de " + self.personne.user.username

