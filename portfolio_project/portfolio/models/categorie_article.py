from django.db import models


class CategorieNiv1 (models.Model):
    """defining the table to declare level 1 categorie"""
    id_categorie_niv_1 = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, default="category name", null=False)

    class Meta:
        verbose_name = "categorie level 1"

    def __str__(self):
        return str(self.id_categorie_niv_1)


class CategorieNiv2(models.Model):
    """defining the table to declare level 2 categorie"""
    id_categorie_niv_1 = models.ForeignKey(CategorieNiv1,
                                           null=False,
                                           unique=False,
                                           default=None,
                                           on_delete=models.SET_DEFAULT)

    nom = models.CharField(max_length=100, default="category name", null=False)
    id_categorie_niv_2 = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "categorie level 2"

    def __str__(self):
        return str(self.id_categorie_niv_2)


class CategorieNiv3 (models.Model):
    """defining the table to declare level 3 categorie"""
    nom = models.CharField(max_length=100, default="category name", null=False)
    id_categorie_niv_2 = models.ForeignKey(CategorieNiv2,
                                           null=False,
                                           unique=False,
                                           default=None,
                                           on_delete=models.SET_DEFAULT)

    id_categorie_niv_3 = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "categorie level 3"

    def __str__(self):
        return str(self.id_categorie_niv_3)
