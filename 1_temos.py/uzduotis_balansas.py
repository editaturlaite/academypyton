
# 1 UZDUOTIS 

# Sukurti minibiudžeto programą, kuri:
# •Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
# •Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
# •Atvaizduotų jau įvestas pajamas ir išlaidas
# •Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)
 
# Patarimas:

import pickle

def pajamu_sumavimas (pajamos):
    pajamu_sarasas.append(pajamos)
    pajamu_suma = sum(pajamu_sarasas)
    return pajamu_suma

def islaidu_sumavimas (islaidos):
    islaidu_sarasas.append(islaidos)
    islaidu_suma = sum(islaidu_sarasas)
    return islaidu_suma

def balanso_skaiciavimas (pliusas,minusas):
    balansas = sum(pliusas) + sum(minusas)
    return balansas


try:
    with open("pajamos.picle","rb")as failas:
        pajamu_sarasas = pickle.load(failas)
except EOFError:
    pajamu_sarasas = []
    
try:
    with open("islaidos.picle","rb")as failas:
        islaidu_sarasas = pickle.load(failas)
except EOFError:
    islaidu_sarasas = []


while True:
    try:
        norima_operacija = int(input("""Pasirinkite norima operacija ir iveskite jos numeri:
                                1. Ivesti pajamas.
                                2. Ivesti islaidas.
                                3. Perziureti pajamas.
                                4. Perziureti islaidas.
                                5. perziureti balansa.
                                6. iseiti is programos. 
                                     : """))
        if norima_operacija<1 or norima_operacija>6:
            print("Pasirinkote neegzistuojanti operacijos numeri.Veskite dar karta.")

    except ValueError:
        print("Ivedete ne skaiciu.Veskite dar karta.")

    try:
        if norima_operacija == 1:
            ivedamos_pajamos =int(input("Iveskite pajamas: "))
            pajamu_sumavimas(ivedamos_pajamos)

        elif norima_operacija == 2:
            ivedamos_islaidos =int(input("Iveskite islaidas su minusu. pvz -100 "))
            islaidu_sumavimas(ivedamos_islaidos)

        elif norima_operacija == 3:
            print(f"Visos jusu itrauktos pajamos: {pajamu_sarasas}\n Ju suma:{pajamu_sumavimas(ivedamos_pajamos)} ")

        elif norima_operacija == 4:
            print(f"Visos jusu itrauktos islaidos: {islaidu_sarasas}\n Ju suma:{islaidu_sumavimas(ivedamos_islaidos)} ")

        elif norima_operacija == 5:
            print(f"Jusu balansas yra: {balanso_skaiciavimas(pajamu_sarasas,islaidu_sarasas)}")

        elif norima_operacija == 6:
            break
    except ValueError:
        print("Ivedete ne skaiciu. Pasirinkite norima operacija ir bandykite dar karta")

print("Programa baigta")

with open("pajamos.picle","ab")as failas:
    pickle.dump(pajamu_sarasas,failas)

with open("islaidos.picle","ab")as failas:
    pickle.dump(islaidu_sarasas,failas)
    
exit()

