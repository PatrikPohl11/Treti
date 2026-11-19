seznam_cisel = [1,2,5,96,8,456,25877,58,36,21,542,159,16,26,325]

print(f"seznam pred upravou: {seznam_cisel}")

seznam_cisel.append(69)
seznam_cisel.append(99)
seznam_cisel.remove(96)
seznam_cisel.insert(3, 1000)

print(f"seznam po uprave: {seznam_cisel}")

seznam_cisel.sort()
print(f"serazeny seznam cisel {seznam_cisel}")