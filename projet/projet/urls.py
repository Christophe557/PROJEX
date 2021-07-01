"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings					
from app_1 import views as views_1
from app_2 import views as views_2

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^app_1/', include('app_1.urls', namespace='app_1')),
    re_path(r'^app_2/', include('app_2.urls', namespace='app_2')),
    re_path(r'^$', views_1.index, name='index'),
]

if settings.DEBUG:
    import debug_toolbar
             
    urlpatterns = [
            re_path(r'^__debug__/', include(debug_toolbar.urls)),
            ] + urlpatterns
