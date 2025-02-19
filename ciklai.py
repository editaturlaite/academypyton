# sarasas = [1,2,3,4,5]

# for skaicius in sarasas:
#     print(skaicius)

# # -----------------------------------

# skaiciai = [8,4,2,1,5]
 
# suma = 0
 
# for skaicius in skaiciai: # 1 iteracija -> skaicius = skaiciai[0] | 2 iteracija -> skaicius = skaiciai[1] | ir t.t. su visomis iteracijomis
#     suma = suma + skaicius
#     print(f"Tarpine suma {suma}, o pridetas skaicius yra {skaicius}")
 
# print(suma)

# ---------------------------------------

# skaiciai = [8,4,2,1,5]

# suma = 0

# for skaicius in skaiciai: # 1 iteracija -> skaicius = skaiciai[0] | 2 iteracija -> skaicius = skaiciai[1] | ir t.t. su visomis iteracijomis
#     suma = suma + skaicius
#     print(f"Tarpine suma {suma}, o pridetas skaicius yra {skaicius}")


# print(suma)


# zodziai = ["Labas", "kaip","sekasi"]

# for zodis in zodziai:
#     print(zodis)

# kiekis = 5
# kartas = 0

# while kartas < kiekis: # Kai kartas pasiekia 5 salyga nebeteisinga
#     print(f"{kartas} yra - Labas")
#     if 1 >5:
#         pass
#     else:
#         pass
#     kartas = kartas + 1 # kartas = 0... +1... Kartas = 1 ..... +1 ... Kartas = 2. 

# kartas = 0
# sarasas = []

# while kartas < 2: # Kai kartas pasiekia 5 salyga nebeteisinga
#     ivestis = input("Iveskite skaiciu: ")
#     sarasas.append(ivestis)
#     kartas = kartas + 1 # kartas = 0... +1... Kartas = 1 ..... +1 ... Kartas = 2. 

# print(sarasas)



# kartas = 0
# sarasas = []

# while kartas < 2: # Kai kartas pasiekia 5 salyga nebeteisinga
#     ivestis = input("Iveskite skaiciu: ")
#     sarasas.append(ivestis)
#     kartas = kartas + 1 # kartas = 0... +1... Kartas = 1 ..... +1 ... Kartas = 2. 

# print(sarasas)


# kartas = 0
# sarasas = []

# if kartas < 2: # Kai kartas pasiekia 5 salyga nebeteisinga
#     ivestis = input("Iveskite skaiciu: ")
#     sarasas.append(ivestis)
#     kartas = kartas + 1 # kartas = 0... +1... Kartas = 1 ..... +1 ... Kartas = 2. 
# if kartas < 2: # Kai kartas pasiekia 5 salyga nebeteisinga
#     ivestis = input("Iveskite skaiciu: ")
#     sarasas.append(ivestis)
#     kartas = kartas + 1 # kartas = 0... +1... Kartas = 1 ..... +1 ... Kartas = 2. 
# if kartas < 2: # Kai kartas pasiekia 5 salyga nebeteisinga
#     ivestis = input("Iveskite skaiciu: ")
#     sarasas.append(ivestis)
#     kartas = kartas + 1 # kartas = 0... +1... Kartas = 1 ..... +1 ... Kartas = 2. 

# print(sarasas)

# kartas =0
# sarasas = []

# while kartas <=10:
#     print(kartas)
#     kartas = kartas + 1

# --------------------------------------------------------

# sarasas = [1,2,3,4,5,6]
# for is_eiles in sarasas:
#     print(is_eiles)

# suma = 0
# for skaicius in sarasas:
#     suma = suma + skaicius
# print(suma)


# skaicius = 1
# while skaicius <=100:
#     print(skaicius)
#     skaicius = skaicius + 1

# import random
 
# print(random.randint(0,10)) # random.randint(nuo,iki) generuoja atsitiktinius skaicius tame rezyje nuo 0 iki 10

# ---------------------------------------------?

# dictionary = {"Jonas":20,"Antanas":25,"Justas":15}


# for raktas in dictionary.keys(): # dictionary.keys() arba dictionary -> eina per raktus
#     print(raktas)

# for reiksme in dictionary.values(): # dictionary.values()  -> eina per reiksmes
#     print(reiksme)

# print(dictionary.items())

# tuplu_sarasas = [('Jonas', 20), ('Antanas', 25), ('Justas', 15)]

# tuplas = (4,9)
# kint1, kint2, kint = tuplas
# print(kint2)

# sarasas = (kintamasis,8,2,4) # [] - sarasas | () - tuple | {} - setas | {raktas:reiksme} - zodynas

# for key, value in dictionary.items(): # key, value = ('Jonas', 20) | kvp = ('Antanas', 25)
#     print(f"Raktas yra: {key} o reiksme {value}")



# sarasas = range(10,100) # range(nuo,iki) generuoja skaicius (antras skaicius ne imtinai)

# print(list(sarasas))

# for skaicius in range(20): # range(20) = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#     print(skaicius)

# for skaicius in range(5,20,3): # range(nuo,iki,zingsnis) | taip pat kaip ir stringe stringas[nuo:iki:zingsnis]
#     print(skaicius)

# tuplas = (4,2,8,5)

# for skaicius in tuplas:
#     if skaicius > 6:
#         print(skaicius)
#     else:
#         print(f"netinkamas skaicius {skaicius}")


# ar_neteisingas = True
# # 2> 3 -> False
# # 3> 1 -> True
# while ar_neteisingas:
#     ivestis = input("Iveskite tik skaiciu 5")
#     if ivestis == "5": 
#         ar_neteisingas = False

# print("Programa Baigta")


# ar_neteisingas = True
# # 2> 3 -> False
# # 3> 1 -> True
# while ar_neteisingas:
#     ivestis = input("Iveskite tik skaiciu 5")
#     if ivestis.isdigit():
#         if int(ivestis) == 5: 
#             ar_neteisingas = False

# print("Programa Baigta")

# a = 0
# while True:
#     a = a +1
#     print(a)

# sarasas = [8,5,2,6,9,3, 6] # surasti ar sarase yra 4 (reiksme) | -> in yra tiesiog pasleptas ciklas

# for elementas in sarasas:
#     if elementas == 6:
#         print("Egzistuoja")
#         break # nutraukia cikla, siuo atveju 4 iteracijos metu, ir 9 3 ir 6 net nebetikrina

# print("Programa baigta")

# sarasas = [8,5,2,6,9,3, 6] # suradus skaiciu didesni nei 7 ji atspaudinti

# for skaicius in sarasas:
#     if skaicius > 7:
#         print(skaicius)
#     else:
#         continue # praleisti likusia iteracijos dali
#     #cia vykdoma tik jeigu nesuveike continue
#     print("Dar kazka darau")


# sarasu_sarasas = [14,[4,7,5],8,9]

# for elementas in sarasu_sarasas:
#     if type(elementas) == list:
#         for el in elementas: # elementas = [4,7,5]
#             print(el)


# for sk in range(10):
#     for sk2 in range(10):
#         print(f"sk: {sk} ir sk2: {sk2}")

# for sk in range(10):
#     pass

# print("labas")


# import random

# print(random.randint(0,10)) # random.randint(nuo,iki) generuoja atsitiktinius skaicius tame rezyje nuo 0 iki 10


# ----------------------------------------

# PIRMA UZDUOTIS--------------------------

# sarasas = []
# teigiamas_skaicius = True
# suma = 0

# while teigiamas_skaicius:
#     skaicius = int(input("Iveskite skaiciu "))

#     if skaicius >=0:
#         sarasas.append(skaicius)
    
#     if skaicius <0:
#         teigiamas_skaicius = False
#         break

# for skaicius in sarasas:
#     suma = suma + skaicius

# print(f"Saraso teigiamu skaiciu suma yar: {suma}")

# ANTRA UŽDUOTIS -------------------------------------


# tekstas = list(input("Iveskite 5 zodzius ").split())
# ilgis = len(tekstas)

# while ilgis<5:
#     prideti = input(" iveskite dar viena zodi ")
#     tekstas.append(prideti)
#     ilgis = ilgis + 1

# if ilgis>5:
#     print("per daug zodziu ")
#     exit()

# for zodiai in tekstas[1:5]:
#     print(f"zodis:  {zodiai},ilgis:  {len(zodiai)}, indeksas: {tekstas.index(zodiai)}")

# TRECIA UZDUOTIS-------------------------------------------

# import random

# issuktas_skaicius = random.randint(1,6)
# print(issuktas_skaicius)

# while issuktas_skaicius:
    
#     if issuktas_skaicius == 5:
#         print("Laimejai...")
#         break
#     else:
#         print("Pralaimejai..")
#         break

# KETVIRTA UZDUOTIS-----------------------------

# keliamieji = []

# for metai in range(1900,2100):
#     if metai % 400 == 0 or metai % 4 == 0:
#         keliamieji.append(metai)
# print(keliamieji)


# metai = int(input("Iveskite metus "))
# if metai % 400 == 0 or metai % 4 == 0:
#     print("Taip tai keliamieji metai")
# elif metai % 100 == 0:
#     print("Ne tai ne keliamieji metai")
# else:
#     print("Ne tai ne keliamieji metai")

# PENKTA UZDUOTIS--------------------------------------------------

# Raidžių išskaidymas
# •	Paprašykite naudotojo įvesti trumpą žodį arba frazę.
# •	Panaudokite for ciklą, kad išvestumėte kiekvieną įvesto teksto simbolį (raidę, tarpą) naujoje eilutėje.

# fraze = input("Iveskite fraze ")

# for simbolis in fraze:
#     print(simbolis)

# SESTA UZDUOTIS-----------------------------

# Skaičių pakėlimas laipsniu
# •	Paprašykite naudotojo įvesti du skaičius: pagrindą (base) ir laipsnį (power) (pvz., 2 ir 3).
# •	Sukurkite ciklą, kuris dauginimo būdu apskaičiuotų base^power (nereikėtų naudoti integruotos ** operacijos).
# •	Išveskite gautą rezultatą.
# Pavyzdys: Jei naudotojas įveda 2 ir 3, rezultatas: 2^3 = 8.


# base = input("Iveskite pagrindini skaiciu ")
# power = input("Iveskite  laipsni  ")
# base = int(base)
# power = int(power)
# rezultatas = 1

# for _ in range(power):
#     rezultatas = rezultatas*base

# print(rezultatas)

# rezultatas = base**power
# print (rezultatas)

# SEPTINTA UZDUOTIS-------------------------------

# Simbolių paieška
# •	Paprašykite naudotojo įvesti sakinį.
# •	Tuomet leiskite įvesti raidę (ar kitą simbolį), kurio bus ieškoma sakinyje.
# •	Naudodami for ciklą suskaičiuokite, kiek kartų ši raidė pasikartoja sakinyje, ir išveskite rezultatą.

# sakinys = input("Iveskite sakini ").replace(" ","")

# simbolis = input("Iveskite ieskoma simboli ")

# kartai = sakinys.count(simbolis)
# print(kartai)


# ASTUNTA UZDUOTIS------------------

# Žodžių išskaidymas ir spausdinimas
# •	Paprašykite naudotojo įvesti sakinio ilgį (kiek žodžių planuoja įvesti).
# •	Tegul naudotojas įveda kiekvieną žodį atskirai. Visus žodžius išsaugokite sąraše.
# •	Naudodami for ciklą išveskite žodžius atvirkštine tvarka (nuo paskutinio iki pirmo).

# norimas_ilgis = int(input("iveskite busimo sakinio zodziu skaiciu "))

# sarasas =[]
# saraso_ilgis = 0

# while saraso_ilgis < norimas_ilgis:
#     zodis = input("Iveskite zodi ")
#     sarasas.append(zodis)
#     # print(sarasas)
#     saraso_ilgis = saraso_ilgis + 1
#     # print(saraso_ilgis)

# for atbulai in sarasas[::-1]:
#     print(atbulai)


# DEVINTA UZDUOTIS-----------------------------

# Žodžio apsukimas
# •	Paprašykite naudotojo įvesti žodį ar trumpą frazę.
# •	Sukurkite programą, kuri, naudodama for ciklą, atspausdintų šį žodį (pvz., "Kava" → "avaK"). Nenaudokite [::-1] ar reverse
# •	Išveskite gautą apsuktą tekstą.

# fraze = "morka"
# fraze_atbulai  = []

# for apsukti in fraze:
#     fraze_atbulai.insert(0,apsukti)
# print(fraze_atbulai)

# fraze_atbulai_spauzdinti = "".join(fraze_atbulai)
# print(fraze_atbulai_spauzdinti)
   

# DESIMTA UZDUOTIS-----------------------------------

# Didžiausios reikšmės radimas be max
# Susikurkite sąrašą, pvz. [3, 7, 1, 12, 9].
# Naudodami for ciklą raskite didžiausią elementą sąraše (nenaudokite max() funkcijos).
# Išveskite rastą reikšmę.

# listas = [3, 7, 1, 12, 9]
# dabartinis_skaicius = 0

# for skaicius in listas:

#     if skaicius>dabartinis_skaicius:
#         dabartinis_skaicius = skaicius

# print(f"Didziausias skaicius yra: {dabartinis_skaicius}")








   





