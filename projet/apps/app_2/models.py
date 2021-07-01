from django.db import models


class Contenu(models.Model):

    titre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "contenu"
    def __str__(self):
        return self.titre



