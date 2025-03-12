# sarasas = [7,1,4,5,8,96]
 
# with open("test.txt","r") as failas:
#     gautas = failas.read()
 
# gautas_sar = gautas.replace("[","").replace("]","").split(", ")
 
# print(gautas_sar)
# ------

# import pickle
 
# sarasas = [7,1,4,5,8,96]
 
# with open("failas.pickle","wb") as failas: # wb - write bytes
#     pickle.dump(sarasas,failas) # beveik tas pats kas write | pickle.dump(turinys,failas)
 
# with open("failas.pickle","rb") as failas: # rb - read bytes
#     grazintas = pickle.load(failas) # beveik tas pats kas write | pickle.dump(turinys,failas)
# grazintas.append(19)
# print(grazintas)
# turi kontekstinį meniu

import pickle # biblioteka kuri skirta irasyti ir nuskaityti i faila sudetingus objektus
 
# sarasas = [  
#     {"Pavadinimas":"Haris Poteris ir išminties akmuo","Autorius":"J.K.Rowling","Išleidimo metai":1997,"Žanras":"Fantastinė"},
#     {"Pavadinimas":"Žiedų valdovas: žiedo brolija","Autorius":"J.R.R.Tolkien","Išleidimo metai":1954,"Žanras":"Fantastinė"},
#     {"Pavadinimas":"1984","Autorius":"G. Orwell","Išleidimo metai":1949,"Žanras":"Distopija"},
#     {"Pavadinimas":"Pietinia kronikas","Autorius":"R. Kmita","Išleidimo metai":2017,"Žanras":"Romanas"},
#     {"Pavadinimas":"Mažas gyvenimas","Autorius":"H. Yanagihara","Išleidimo metai":2015,"Žanras":"Romanas"},
#     {"Pavadinimas":"Haris Poteris ir paslapčių kambarys","Autorius":"J.K.Rowling","Išleidimo metai":1998,"Žanras":"Fantastinė"},
#     {"Pavadinimas":"Puikus naujas pasaulis","Autorius":"A. Huxley","Išleidimo metai":1932,"Žanras":"Distopija"},
#     {"Pavadinimas":"Kopa","Autorius":"F. Herbert","Išleidimo metai":1965,"Žanras":"Mokslinė fantastika"}
#     ]
 
# with open("failas.pickle","wb") as failas: # wb - write bytes
#     pickle.dump("Labas",failas) # beveik tas pats kas write | pickle.dump(turinys,failas)
 
# with open("failas.pickle","rb") as failas: # rb - read bytes
#     grazintas = pickle.load(failas) # ka idejom ta ir pasiemame
# # grazintas.append(19)
# # grazintas.append({"Pavadinimas":"Pridetinis","Autorius":"F. Herbert","Išleidimo metai":1965,"Žanras":"Mokslinė fantastika"})
# print(grazintas)
# turi kontekstinį meniu

# ------

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

# pajamu_sarasas = []
# islaidu_sarasas = []
try:
    with open("balansas.picle","rb")as failas:
        pajamu_sarasas = pickle.load(failas)
except EOFError:
    pajamu_sarasas = []
    
try:
    with open("balansas.picle","rb")as failas:
        islaidu_sarasas = pickle.load(failas)
except EOFError:
    islaidu_sarasas = []


while True:
    norima_operacija = int(input("""Pasirinkite norima operacija ir iveskite jos numeri:
                            1. Ivesti pajamas.
                            2. Ivesti islaidas.
                            3. Perziureti pajamas.
                            4. Perziureti islaidas.
                            5. perziureti balansa.
                            6. iseiti is programos. """))
    if norima_operacija == 1:
        ivedamos_pajamos =int(input("Iveskite pajamas: "))
        print(pajamu_sumavimas(ivedamos_pajamos))

    elif norima_operacija == 2:
        ivedamos_islaidos =int(input("Iveskite islaidas su minusu. pvz -100 "))
        print(islaidu_sumavimas(ivedamos_islaidos))

    elif norima_operacija == 3:
        print(f"Visos jusu pajamos yra {pajamu_sarasas}")

    elif norima_operacija == 4:
           print(f"Visos jusu islaidos yra {islaidu_sarasas}")

    elif norima_operacija == 5:
        print(balanso_skaiciavimas(pajamu_sarasas,islaidu_sarasas))

    elif norima_operacija == 6:
        break
print("Programa baigta")

with open("balansas.picle","ab")as failas:
    pickle.dump(pajamu_sarasas,failas)

with open("balansas.picle","ab")as failas:
    pickle.dump(islaidu_sarasas,failas)
    
exit()

