#Pour utiliser le RANDOM il faut importer la librairie random
import random
#On utilise la fonction randint pour générer un nombre aléatoire entre 1 et 50
A = random.randint(2, 10)
B = random.randint(2, 10)

#print(f"{A} x {B} = {A * B}")
C = A * B
#print(f" {C}")
choix = int(input(f"{A} x {B} = "))

if C == choix:
    print(f" C'est juste!")
else:
    print(f"Perdu !")



    
   