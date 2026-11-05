secret = 42
choix = 0
while choix != secret:
    choix = int(input("Votre proposition : "))

    if choix < secret:
        print(" C'est plus.")        
    elif choix > secret:
        print(" C'est moins.")
    else:
        print("Bravo, c'est gagné !")
        
