#Pour utiliser le RANDOM il faut importer la librairie random
import random
#On utilise la fonction randint pour générer un nombre aléatoire entre 1 et 50
RD = random.randint(1, 100)
#secret = 42
choix = 0
coups = 0
while choix != RD:
    choix = int(input("Votre proposition : "))
    coups = coups + 1
    #print(f"Nombre magique {RD} ")
    if choix < RD:
        print(" C'est plus.")
        
    elif choix > RD:
        print(" C'est moins.")
    else:
        print(f"Bravo, trouvé en {coups} coups !")