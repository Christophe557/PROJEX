from django.shortcuts import render
from .models import Article



def listing(request):
    articles = Article.objects.all()
    titre_page = "TOUS LES ARTICLES"

    context = {
            'articles': articles,
            'titre_page': titre_page
            }

    return render(request, 'app_2/listing.html', context)
