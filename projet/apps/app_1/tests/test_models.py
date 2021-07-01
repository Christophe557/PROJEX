from app_1.models import Article
from mixer.backend.django import mixer
import pytest



@pytest.mark.django_db
class TestModels:

    def test_article_has_title(self):
        article = mixer.blend(Article, titre="TITRE")
        assert article.titre == "TITRE"


        

