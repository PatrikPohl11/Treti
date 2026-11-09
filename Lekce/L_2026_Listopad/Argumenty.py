def scitani(a, b):
    return a+b

soucet = scitani(5, 7)
print ("součet je:", soucet)

soucet2 = scitani(b=10, a=15)
print("soucet je:", soucet2)


def delen(a, b):
    if b== 0:
        return "nelze delit 0"
    else:
        return a/b
print("deleni je:", delen(b=4, a=6))