from django.db import models
from utilisateur.models import Personne
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from categorie.models import Categorie
import datetime


class Article (models.Model):
    """model of the article """
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=None, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="image_article/")
    date = models.DateField(null=False, default=datetime.date.today)
    publish = models.BooleanField(default=False)
    titre = models.CharField(max_length=100, null=False, default=None)
    resume = models.CharField(max_length=200, null=False, default=None)
    content = MarkdownxField()

    @property
    def formatted_resume_markdown(self):
        return markdownify(self.resume)

    @property
    def formatted_content_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return "article de " + self.personne.user.username

