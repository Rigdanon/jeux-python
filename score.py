#Pour utiliser le RANDOM il faut importer la librairie random
import random
#On utilise la fonction randint pour générer un nombre aléatoire entre 1 et 50
#A = random.randint(2, 10)
#B = random.randint(2, 10)

score = 0
for i in range(10):
    A = random.randint(2, 10)
    B = random.randint(2, 10)
    C = A * B
#print(f" {C}")
    i = i + 1
    choix = int(input(f"Question {i} : {A} x {B} = "))

    if C == choix:
        print(f" C'est juste!")
    else:
        print(f"Perdu !")

    if C == choix:
        score = score + 1
        #print(f"Score : {score}/10")
print(f"Score : {score}/10")

    #if coups ==  7 and choix != RD:
        #print(f"Vous avez dépassé plus de 7 essais le nb était {RD}.")