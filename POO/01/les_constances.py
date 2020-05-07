import os # parce qu'on travaille avec des chemins

CUR_DIR = os.path.dirname(os.path.abspath(__file__)) # file retourne le chemin actuelle les_constance.py, abspath permet de récuperer un chemin absolu, dirname qui permet de 
                                                    # récuperer le dossier actuelle 01 cur_dir pour current dir, dossier actuelle
DATA_DIR = os.path.join(CUR_DIR, "data")
print(DATA_DIR)