from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # affichage des articles

    # définition d'une barre de recherche et de filtre sur les champs
    search_fields = ['titre']
    list_filter = []

    # champs à afficher
    fieldsets = [
            (None, {'fields': [('titre', ), ]})
            ]
 
    # déclarer les champs non modifiables pour pouvoir les afficher:
    readonly_fields = []
    



