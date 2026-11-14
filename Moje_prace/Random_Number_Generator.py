import random

#zepta se na hodnoty od a do kterych se ma henerovat
od = int(input("Zadejte od ktereho čísla se má generovat: "))
do = int(input("Zadejte do ktereho čísla se má generovat: "))

#vygeneruje nahodne číslo
random_n = random.randint(od, do)

#vypise vygenerovane číslo
print(f"Vygenerovane číslo je: {random_n}")