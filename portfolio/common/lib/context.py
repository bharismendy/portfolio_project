from categorie.models import Categorie


def context_general():
    """
    method to get the menu to be displayed
    :return: different menu in a dict
    """
    list_cat_1 = Categorie.objects.filter(niv_cat=1).order_by('nom_categorie')
    list_cat_2 = Categorie.objects.filter(niv_cat=2).order_by('nom_categorie')
    list_cat_3 = Categorie.objects.filter(niv_cat=3).order_by('nom_categorie')
    list_cat_4 = Categorie.objects.filter(niv_cat=4).order_by('nom_categorie')

    return {"cat_niv_1": list_cat_1,
            "cat_niv_2": list_cat_2,
            "cat_niv_3": list_cat_3,
            "cat_niv_4": list_cat_4}
