def vypocet_obvodu_obdelniku(delka, sirka):
    return 2 * (delka + sirka)

def vypocet_obsahu_obdelniku(delka, sirka):
    return delka * sirka

delka = float(input("Zadej delku Tvaru: "))
sirka = float(input("Zadej sirku Tvaru: "))

print(f"Obvod obdelniku s delkou {delka} a sirkou {sirka} je: {vypocet_obvodu_obdelniku(delka, sirka)}")
print(f"Obsah obdelniku s delkou {delka} a sirkou {sirka} je: {vypocet_obsahu_obdelniku(delka, sirka)}")



def vypocet_obvodu_obsahu_obdelniku(delka, sirka):
    return 2 * (delka + sirka), (delka * sirka)

delka = float(input("Zadej delku: "))
sirka = float(input("Zadej sirku: "))

obvod, obsah = vypocet_obvodu_obsahu_obdelniku(delka, sirka)
print(f"Obvod je: {obvod}")
print(f"Obsah je: {obsah}")
print(f"Rozmery tvaru jsou: delka = {delka}, sirka = {sirka}")