#Pour utiliser le RANDOM il faut importer la librairie random
import random
#On utilise la fonction randint pour générer un nombre aléatoire entre 1 et 50
#score = 0
for ordi in range(1, 4):
    A = random.randint(1, 3)
    #B = random.randint(2, 10)
    #C = A * B
#print(f" {C}")
    if A == 1:
        A = "pierre"
    elif A == 2:
        A = "feuille"
    else:
        A = "ciseaux"

    for joueur in range(1, 4):
        B = random.randint(1, 3)
    #print(f" {C}")
    if B == 1:
        B = "pierre"
    elif B == 2:
        B = "feuille"
    else:
        B = "ciseaux"

    elif (joueur == "pierre" and ordi == "ciseaux") or \
(joueur == "feuille" and ordi == "pierre") or \
(joueur == "ciseaux" and ordi == "feuille"):
    break

    i = i + 1
    choix = int(input(f"Question {i} : {A} x {B} = "))

    if C == choix:
        print(f" C'est juste!")
    else:
        print(f"Perdu, c'était {C}")

    if C == choix:
        score = score + 1
        #print(f"Score : {score}/10")
print(f"Score : {score}/10")
if score == 10:
    print(f"Parfait")
elif score >= 7:
    print(f"Très bien")
elif score >= 5:
    print(f"Pas mal")
else:
    print(f"Révisez vos tables")
#choix = int(input("Votre proposition : "))

#while choix != RD and coups < 7:
    #coups = coups + 1
    #print(f"Essai {coups} sur 7")

    #choix = int(input("Votre proposition : "))
    #print(f"Nombre magique {RD} ")
    
    #if choix < RD:
        #print(" C'est plus.")        
    #elif choix > RD:
        #print(" C'est moins.")
    #else:
        #print(f"Bravo, trouvé en {coups} coups !")    
    #if coups ==  7 and choix != RD:
        #print(f"Vous avez dépassé plus de 7 essais le nb était {RD}.")