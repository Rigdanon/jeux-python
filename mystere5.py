#Pour utiliser le RANDOM il faut importer la librairie random
import random
#On utilise la fonction randint pour générer un nombre aléatoire entre 1 et 50
RD = random.randint(1, 50)
#secret = 42
choix = 0
coups = 0
while choix != RD and coups < 7:
    coups = coups + 1
    print(f"Essai {coups} sur 7")

    choix = int(input("Votre proposition : "))
    #print(f"Nombre magique {RD} ")
    
    if choix < RD:
        print(" C'est plus.")        
    elif choix > RD:
        print(" C'est moins.")
    else:
        print(f"Bravo, trouvé en {coups} coups !")
    
    if coups ==  7 and choix != RD:
        print(f"Vous avez dépassé plus de 7 essais le nb était {RD}.")

