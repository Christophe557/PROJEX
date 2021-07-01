from django.shortcuts import render
from .models import Contenu



def listing(request):
    contenus = Contenu.objects.all()
    titre_page = "TOUS LES CONTENUS"

    context = {
            'contenus': contenus,
            'titre_page': titre_page
            }

    return render(request, 'app_2/listing.html', context)
