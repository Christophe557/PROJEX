from django.test import RequestFactory
from django.urls import reverse
from app_2 import views
from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestViews:



    def test_listing(self):
        path = reverse('app_2:listing')
        request = RequestFactory().get(path)
        response = views.listing(request)
        assert response.status_code == 200


