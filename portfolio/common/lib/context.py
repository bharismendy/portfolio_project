from categorie.models import CategorieNiv1
from categorie.models import CategorieNiv2
from categorie.models import CategorieNiv3


def context_general():
    list_cat_1 = CategorieNiv1.objects.all().order_by('nom_categorie')
    list_cat_2 = CategorieNiv2.objects.all().order_by('nom_categorie')
    list_cat_3 = CategorieNiv3.objects.all().order_by('nom_categorie')
    return {"cat_niv_1": list_cat_1, "cat_niv_2": list_cat_2, "cat_niv_3": list_cat_3}
