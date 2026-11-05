#Pour utiliser le RANDOM il faut importer la librairie random
#import random
#On utilise la fonction randint pour générer un nombre aléatoire entre 1 et 50
#RD = random.randint(1, 50)
choix = int(input("Votre proposition : "))
secret = 42

if choix < secret:
    print(" C'est plus.")
elif choix > secret:
    print(" C'est moins.")
else:
    print("Bravo, c'est gagné !")
