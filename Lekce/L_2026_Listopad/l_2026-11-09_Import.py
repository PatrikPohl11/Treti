import math

print(f"Číslo PI: {math.pi}")
print("Sinus 90°:", math.sin(math.pi/2))

def bezpecne_deleni(a,b):
    try:
        vysledek = a / b
    except ZeroDivisionError as zde:
        print(F"Chyba: {zde}")
        return None
    except Exception as e:
        zprava = f"Nelze delit objekt {a} / {b}: {e}"
        raise Exception(zprava)
    finally:
        print("deleni provedeno")
        print("tento blok se provede vzdy")
    return vysledek

print(bezpecne_deleni(10, 2))
print(bezpecne_deleni(10, 0))