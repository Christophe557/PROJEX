# les settings par défaut sont dans developpement.py :
from .developpement import *

# ensuite, si le fichier production.py existe (normalement uniquement
# sur le serveur de produciton, les variables de production viendront écraser
# celles de développement :
try:
    from .production import *
except ModuleNotFoundError:
    pass
