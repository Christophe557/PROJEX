from django.test import RequestFactory
from django.urls import reverse
from apps.app_1 import views
from mixer.backend.django import mixer
import pytest


class TestViews:

    def test_index(self):
        path = reverse('index')
        request = RequestFactory().get(path)
        response = views.index(request)
        assert response.status_code == 200


    def test_listing(self):
        path = reverse('app_1:listing')
        request = RequestFactory().get(path)
        response = views.listing(request)
        assert response.status_code == 200


