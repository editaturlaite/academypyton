# 10 UZDUOTIS --------------------------------------------------------------

# Tikslas:
# Parašykite programą, kuri paprašys įvesti dvi datas formatu "YYYY-MM-DD" (pradžios ir pabaigos datas) ir atliks šiuos veiksmus:
# Datos įvedimas ir validacija:
# Paprašykite vartotojo įvesti pradžios ir pabaigos datas.
# Naudokite try/except bloką, kad patikrintumėte, ar įvestos datos atitinka formatą "YYYY-MM-DD" ir konvertuotumėte jas į datetime objektus.
# Jei datos formatas neteisingas, naudokite raise su žinute, pvz.:
# "Neteisingas datos formatas! Prašome naudoti YYYY-MM-DD."
# Patikrinkite, ar pradžios data yra ankstesnė arba lygi pabaigos date. Jei ne, išmeskite klaidą su žinute:
# "Pradžios data turi būti ankstesnė nei pabaigos data."
# Naudokite finally bloką, kad nepriklausomai nuo klaidų, būtų atspausdinta žinutė, pvz.:
# "Datos įvedimo bandymas baigtas."
# Datos intervalo analizė:
# Naudodami ciklą, iteruokite per visas dienas nuo pradžios iki pabaigos datos (įskaitant abi datas).
# Kiekvienai dienai atlikite šiuos patikrinimus:
# Jei diena yra savaitgalis (šeštadienis arba sekmadienis), suskaičiuokite ją.
# Jei diena yra mėnesio pirmoji diena (t. y. dienos numeris lygus 1), suskaičiuokite ją.
# Taip pat apskaičiuokite bendrą dienų skaičių šiame intervale.
# Rezultatų atspausdinimas:
# Atspausdinkite:
# Bendrą dienų skaičių.
# Savaitgalių skaičių.
# Mėnesio pirmųjų dienų skaičių.
# Pabaigoje atspausdinkite žinutę:
# "Datos analizė baigta."

import datetime

try:
    try:
        pradzia = input("Iveskite pradzios data siuo formatu: YYYY-MM-DD ")
        pradzia = datetime.datetime.strptime(pradzia, "%Y-%m-%d")
    except ValueError:
        print("Neteisingas datos formatas! Prašome naudoti YYYY-MM-DD.")
        klaida = True
        if klaida:
            exit()

    try:
        pabaiga = input("Iveskite pabaigos data siuo formatu: YYYY-MM-DD ")
        pabaiga = datetime.datetime.strptime(pabaiga, "%Y-%m-%d")
    except ValueError:
        print("Neteisingas datos formatas! Prašome naudoti YYYY-MM-DD.")
        klaida = True
        if klaida:
            exit()

    try:
        if pradzia>=pabaiga:
            raise ValueError ("Pradžios data turi būti ankstesnė nei pabaigos data.")
    except ValueError as pb:
        print(pb)

finally:
    print("Datos įvedimo bandymas baigtas.\n ")

savaitgalio_diena = 0
menesio_pirma = 0
dienu_skaicius = 0


while pradzia<=pabaiga:
    if pradzia.weekday() == 5 or pradzia.weekday() == 6:
        savaitgalio_diena +=1

    if pradzia.day == 1:
        menesio_pirma += 1
    dienu_skaicius += 1
    pradzia += datetime.timedelta(days=1)

print(f"Bendras dienu skaicius: {dienu_skaicius}")
print(f"Laikotarpyje {savaitgalio_diena} savaitgalio dienu")
print(f"ir {menesio_pirma} menesiu\n ")

print("Datos analizė baigta.")