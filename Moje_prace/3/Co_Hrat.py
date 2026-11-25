import random

hry = ["Euro Truck Simulator 2", "Minecraft", "GTA V", "GTA VI", "Farming Simulator 25", "DiRT Rally 2.0", "American Truck Simulator", "Counter Strike 2"]

vyber = random.choice(hry)

print(f"Dnes si zahrajes: {vyber}")

hry.append("Farming Simulator 22")
hry.insert(4, "Euro Truck Simulator 2 MapCombo")
print("priddana hra: FS22, ETS2 MapCombo")

vyber2 = random.choice(hry)
print(f"Nebo si zahraj: {vyber2}")