from django.db import models


class Categorie(models.Model):
    """this class is use to categorise every article"""
    NIV_CAT = {(1, 1),
               (2, 2),
               (3, 3),
               (4, 4)}
    nom_categorie = models.CharField(max_length=100, default=None, null=False, unique=True)
    has_sub = models.BooleanField(default=False)
    cat_sup = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True)
    niv_cat = models.IntegerField(default=None, null=True, choices=NIV_CAT)

    def __str__(self):
        return self.nom_categorie
