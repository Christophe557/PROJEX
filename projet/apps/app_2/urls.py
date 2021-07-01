from django.urls import path, re_path, include
from . import views

app_name = 'app_2'

urlpatterns = [
        re_path(r'^$', views.listing, name='listing'), 
        ]
