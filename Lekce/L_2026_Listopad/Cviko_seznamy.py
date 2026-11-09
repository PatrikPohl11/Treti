import math
#promena a retezce
jmeno = "abfcdsbf"
vek = "4564646"
print(f"Jmeno je: {jmeno} a je stary: {vek} let.")

numbers = [8, 7, 3, 4, 9]

numbers.append(6)
numbers.sort()
print(f"serazeny seznam: {numbers}")
print(f"prvni prvek seznamu: {numbers[0]}")
print(f"posledni prvek seznamu: {numbers[-1]}")

student = {
    "jmeno": "pepa",
    "vek": "nevim",
    "predmety": ["Matyka, askjvfdgj"]
}

student ["vek"] = 25
student ["jmeno"] = "pepa"
student ["predmety"] = ["dasdasda", "sdadsagbhgfgfd"]

print ("student:", student)

data = [3,3,3,4,5,6,7,8,9,9,9,10]
uniq_data = set(data)
print(f"Unikatni cisla: {uniq_data}")

for i in range(1, 11):
    if i % 3 == 0:
        print("je delitelne 3")
    elif i % 5 == 0:
        print("je delitelne 5")
    else:
        print(i)


def vypocet_obvodu_obdelniku(delka, sirka):
    return 2 * (delka + sirka)

delka = 45678979456
sirka = 1
print(f"Obvod obdenikus delkou {delka} a sirkou {sirka} je: {vypocet_obvodu_obdelniku}")