#zepta se na osobni udaje
Jmeno = input("Zadejte svoje jmeno: ")
Prijmeni = input("zadejte svoje prijmeni: ")
Vek = int(input("Zadejte svuj vek: "))

#pokad je vek mezi 15 a 65 tak se zepta i napovolani
if Vek >= 15 and Vek < 65:
    Povolani = input("Zadejte svoju robotu: ")
elif Vek >= 65:
    Povolani = ("Jsi senior, takže si nejspis v duchodu a nerobiš")
else:
    Povolani = "Bud si nezamestnany nebo robis na cerno"


#vypise zadane udaje
print("Jmenuješ se", Jmeno, Prijmeni, "a je ti", Vek, "let.")
print("Robiš ve: ", Povolani)
if Vek < 15:
    print("Jsi decko")
elif Vek >= 15 and Vek < 18:
    print("Jsi teenager")
elif Vek >= 18 and Vek < 65:
    print("je ti dsot")
else:
    print("Jsi senior")