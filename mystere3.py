secret = 42
choix = 0
coups = 0
while choix != secret:
    choix = int(input("Votre proposition : "))
    coups = coups + 1
    if choix < secret:
        print(" C'est plus.")        
    elif choix > secret:
        print(" C'est moins.")
    else:
        print(f"Bravo, trouvé en {coups} coups !")