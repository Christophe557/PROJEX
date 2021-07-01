from django.shortcuts import render
from .models import Article

def index(request):
    context = {}
    return render(request, 'app_1/index.html', context)


def listing(request):
    articles = Article.objects.all()
    titre_page = "TOUS LES ARTICLES"

    context = {
            'articles': articles,
            'titre_page': titre_page
            }

    return render(request, 'app_1/listing.html', context)
