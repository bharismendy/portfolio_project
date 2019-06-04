from django.test import TestCase
import pytest

from article.models import Article

pytestmark = pytest.mark.django_db

class TestProductModel:

    def test_save(self):
        product = Article.objects.create(

        )
        assert product.name == Sample product
        assert product.price == 500
