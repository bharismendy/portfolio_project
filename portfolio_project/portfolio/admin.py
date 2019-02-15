from django.contrib import admin
from portfolio.models.categorie_article import CategorieNiv1,CategorieNiv2,CategorieNiv3
from portfolio.models.UserModel import Utilisateur

admin.site.register(Utilisateur)
admin.site.register(CategorieNiv1)
admin.site.register(CategorieNiv2)
admin.site.register(CategorieNiv3)
