# Nakupni seznam

print("=============== Nakupni seznam ===============")
seznam = []                                                    #prazdny nakupni seznam
while True:                                                    #opakuje furt dokad nezadas "end"
    seznam.append(input("Zadej co chces nakoupit: (když sem zadas vse napis end)"))

    if seznam[-1] == "end":
        break

seznam.remove("end")                                           #odstarni polozku "end" ze seznamu
print(f"Potrebujes koupit: {seznam}")




# verze 2

# Nakupni seznam

print("=============== Nakupni seznam V2 ===============")
seznam = []                                                    #prazdny nakupni seznam
while True:                                                    #opakuje furt dokad nezadas "end"
    polozka = input("Zadej co chces koupit: (Pro konec napis end)")
    seznam.append(polozka)

    if polozka == "end":
        break

seznam.remove("end")                                           #odstarni polozku "end" ze seznamu
print(f"Potrebujes koupit: {seznam}")