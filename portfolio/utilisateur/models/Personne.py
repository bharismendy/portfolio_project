from django.db import models
from django.contrib.auth.models import User


class Personne(models.Model):
    """class to define the model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    age = models.IntegerField(null=False, default=0)
    site_web = models.URLField(blank=True)
    avatar = models.ImageField(null=True, upload_to='avatars/')
    signature = models.TextField(blank=True)
    inscrit_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)
