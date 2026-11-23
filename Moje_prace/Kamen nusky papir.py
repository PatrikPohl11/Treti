import random 

moznost = ["kamen", "nuzky", "papir"]

bot = random.choice(moznost).lower()
while True:
    clovek = input("Zadej co chces pouzit (Kamen, Nuzky, Papir): ").lower()

    if clovek in moznost:
        break
    print("Zadal si gupotu, pis poradne!")

print("bot zvolil: ",bot)
print("clovek zvolil: ", clovek)


if bot == clovek:
    print("Remiza!")

# vsechny prohry
elif bot == "kamen" and clovek == "nuzky":
    print("Prohra")
elif bot == "papir" and clovek == "kamen":
    print("Prohra")
elif bot == "nuzky" and clovek == "papir":
    print("Prohra")
    
else:
    print("Vyhra")