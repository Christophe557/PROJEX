from app_2.models import Contenu
from mixer.backend.django import mixer
import pytest



@pytest.mark.django_db
class TestModels:

    def test_contenu_has_title(self):
        contenu = mixer.blend(Contenu, titre="CONTENT")
        assert contenu.titre == "CONTENT"


        

