# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} # Netuscias zodynas

# dictionary = {} # tuscias zodynas

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} # Netuscias zodynas

# print(dictionary) # atspausdiname zodyna

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} # Netuscias zodynas

# print(dictionary["Mantas"]) # reiksmes gaunamos pagal rakta

# dictionary["Jonas"] = 8 # Pakeisti zodyno reiksme
# print(dictionary)

# ismesta = dictionary.pop("Mantas") # ismeta elementa ir grazina reiksme (ismeta pagal rakta)
# print(ismesta)

# del dictionary["Mantas"] # Ismeta elementa negrazindamas reiksmes

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} # Netuscias zodynas

# dictionary["Petras"] = 20 # Naujo elemento idejimas | Jeigu tokio rakto nera ides, jeigu yra pakeis reiksme
# print(dictionary)

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14, 7 : 15} # Netuscias zodynas

# dictionary[7] = "dvidesimt" # Naujo elemento idejimas | Jeigu tokio rakto nera - ides, jeigu yra - pakeis reiksme
# print(dictionary)

# dictionary = {1:7, 2:8, 3:9} 
# print(dictionary[2])

# dictionary = {"Jonas":[8,9,4,10], "Mantas":[2,5,8,10], "Karolis":[10,10,9,10]} 
# karolis_grades = dictionary["Karolis"] # karolis_grades = [10,10,9,10]
# last_grade = karolis_grades[-1]
# print(last_grade)

# dictionary = {"Jonas":[8,9,4,10], "Mantas":[2,5,8,10], "Karolis":[10,10,9,10]} 
# last_grade = dictionary["Karolis"][-1] # dictionary["Karolis"] -> [10,10,9,10] -> [10,10,9,10] [-1]
# print(last_grade)

# dictionary = {"Jonas":{"Mantas":15, "Rimas": 23}, "Mantas":[2,5,8,10], "Karolis":[10,10,9,10]} #sarasai gali tureti sarasus
# print(dictionary)

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14, "Jonas":12} # Zodyno raktai yra unikalus
# print(dictionary)

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} 

# new_dictionary = dictionary.copy() # zodynai yra refference tipo (nuorodos)
# dictionary.clear()
# print(new_dictionary)

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} 
# print(dictionary.keys()) # atiduos sarasa raktu
# print(dictionary.values()) # atiduos sarasa reiksmiu

# print(dictionary.get("Petras")) # grazina reiksme jeigu yra, jeigu nera grazina None
# print(dictionary["Petras"]) # Grazina reiksme jeigu yra, jeigu nera klaida/nuluzta

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} 

# dictionary1 = {"Petras": 19, "kristupas": 17, "Mantas": 18} 
# dictionary.update(dictionary1) # update - apjungia zodynus, jeigu yra dublikuotu reiksmiu antro zodyno reiksmes prioritizuojamos


# Sandelis-------------------------------------------------------

# Sandelis ={"morkos":12, "salierai":13, "obuoliai":56, "svogunai":75}
# print(Sandelis)

# print(Sandelis["salierai"])

# Sandelis["bulves"] = 66
# print(Sandelis)

# Sandelis.pop("bulves")
# print(Sandelis)

# Sandelis["morkos"] = 222
# print(Sandelis)

# Sandelis.clear()
# print(Sandelis)

# sandelis2 = Sandelis.copy
# print(sandelis2)

# brokas = Sandelis.get("morkos")
# print(brokas)

# darzoves_kiekis = Sandelis.items()
# print(darzoves_kiekis)

# darzoviu_sarasas = Sandelis.keys()
# print(darzoviu_sarasas)

# Sandelis.popitem()
# print(Sandelis)

# sviezios_morkos = Sandelis.setdefault("d", "22")
# # print(sviezios_morkos)
# print(Sandelis)

# Sandelis.update({"apelsinai":"13"})
# print(Sandelis)

# kiekiai = Sandelis.values()
# print(kiekiai)

# x2 = "ropes", "agurka"
# y2 = 11
# kitassar = Sandelis.fromkeys(x2, y2)
# print(kitas)

# -------------------------------------------
# 1 UZDUOTIS

# import this

# tekstas = "There should be one-- and preferably only one --obvious way to do it."


# # atspauzdintas antro zodzio paskutinis simbolis
# print(tekstas[11])

# # atsp pirmas tecio zodzio simb
# print(tekstas[13])

# # atsp pirmas zodis
# print(tekstas[0:5])

# # atsp paskutinis zodis
# # simboliu_skaicius = len(tekstas)
# # print(simboliu_skaicius)
# print(tekstas[66:68])

# # atsp fraze atbulai
# print(tekstas[::-1])

# # atskirti zodziai
# listas = [tekstas.split()]
# print(listas)

# # pakeistas zodis
# naujas_sakinys = tekstas.replace("preferably","ideally")
# print(naujas_sakinys)

# tekstas atvirksciai
# tekstas1 = input("Iveskite savo teksta")
# tekstas2 = tekstas1[::-1]
# print(f"Jusu tekstas atvirksciai: \n{tekstas2}")

# ANTRA UZDUOTIS------------------------------------

# metai = int(input("Iveskite metus "))
# if metai % 400 == 0 or metai % 4 == 0:
#     print("Taip tai keliamieji metai")
# elif metai % 100 == 0:
#     print("Ne tai ne keliamieji metai")
# else:
#     print("Ne tai ne keliamieji metai")


# TRECIA UZDUOTIS------------------------

# listas = [1,5,8,3,6,7,2,1,9,4,2,6,5,8,4,2,5,6,9,9,9,6,6,1,1,0,4,7,2,35,]
# viena komanda
# print(set(listas))
# jei sukurt kita
# listas2 = set(listas)
# print(listas2)

# tuplas = (1,5,8,3,6,7,2,1,9,4,2,6,5,8,4,2,5,6,9,9,9,6,6,1,1,0,4,7,2,35,1,5,8,3,6,7,2,1,9,4,2,6,5,8,4,2,5,6,9,9,9,6,6,1,1,0,4,7,2)
# sarasas = [1,5,8,3,6,7,2,1,9,4,2,6,5,8,4,2,5,6,9,9,9,6,6,1,1,0,4,7,2,35,1,5,8,3,6,7,2,1,9,4,2,6,5,8,4,2,5,6,9,9,9,6,6,1,1,0,4,7,2]

# import time 
# pradzia = time.perf_counter()

# print(sarasas)

# pabaiga = time.perf_counter()

# uztruktas_laikas = (pabaiga - pradzia)*1000
# print(uztruktas_laikas)
# # matosi printinant kartu
# import time 
# pradzia = time.perf_counter()

# print(tuplas)

# pabaiga = time.perf_counter()

# uztruktas_laikas = (pabaiga - pradzia)*1000
# print(uztruktas_laikas)

# KETVIRTA UZDUOTIS---------------------
# 1

# vardas = input("Iveskite savo varda: ")
# pavarde = input("Iveskite savo pavarde: ")
# amzius = input("Iveskite savo amziu: ")

# listas = [vardas,pavarde,amzius]
# print(listas)

# 2

# elementas1 = 8
# elementas2 = 3
# elementas3 = 6
# elementas4 = 2
# elementas5 = 1

# # # elementas1 = input("Iveskite pima elementa ")
# # # elementas2 = input("Iveskite antra elementa ")
# # # elementas3 = input("Iveskite trecia elementa ")
# # # elementas4 = input("Iveskite ketvirta elementa ")
# # # elementas5 = input("Iveskite ppenkta elementa ")

# listas = [elementas1, elementas2, elementas3, elementas4, elementas5]
# naujas_elementas = input("Iveskite nauja elementa ")

# if naujas_elementas in listas:
#     print("Yra")
# else:
#     print("Nera")

# 3

# vardas = input("Iveskite savo varda betkaip kelis kartus: ")
# vardas1 = vardas.title()
# vardas2 = vardas1.replace(" ","")
# print(f"Sveiki,{vardas2}")

# 4 

# balas = int(input("Iveskite savo bala "))

# if balas>=0 and balas<=49:
#     print("Neislaikete")
# elif balas>49 and balas<=64:
#     print("Patenkinamai")
# elif balas>50 and balas <=79:
#     print("Gerai")
# elif balas>79 and balas<=89:
#     print("Labai gerai")
# elif balas>89 and balas<=100:
#     print("Puikiai")
# else:
#     print("Ivesties kalida")

# 5

# listas = [1,2,3,4,5]
# skaicius = int(input("Iveskite skaiciu "))
# if skaicius in listas:
#     listas.remove(skaicius)
#     print(listas)
# else:
#     listas.append(skaicius)
#     print(listas)

# 6

# zodynas = {"Justas":10, "Ruta":3, "Simas":8}
# vardas = input("Iveskite ieskoma varda ")

# if vardas in zodynas:
#     print("pazymyas yra: ",zodynas[vardas])
# else:
#     print("Tokio vardo nera ")


# 7

# tekstas = str(input("Iveskite savo teksta"))
# listas = tekstas.split()
# ilgis = len(listas)
# print(ilgis)
# if ilgis<5:
#     print("Tekstas per trumpas")

# 8

# Sukurkite sąrašą ir leiskite naudotojui įrašyti du indeksus, sukeiskite tuose indeksuose esančių elementų reikšmes.

# listas = [1,2,3,4,5,6,7,8,9,10,11]

# indeksas1 = 10
# indeksas2 = 5

# # indeksas1 = int(input("Iveskite 1 indeksa (nuo 0 iki 10) "))
# # indeksas2 = int(input("Iveskite 2 indeksa (nuo 0 iki 10) "))


# listas[indeksas1],listas[indeksas2]=listas[indeksas2],listas[indeksas1]

# print(listas)


# 9

# tekstas = "mano tekstas su zodziu programavimas"
# tekstas = input("Iveskite savo teksta ").capitalize().split()
# tekstas1  = tekstas.capitalize()
# if "Programavimas" in tekstas:
#     print("yra")
# else:
#     print("nera")

# 10

# slapt = list("Edi22")
# slapt = list(input("iveskite 5 simboliu slaptazodi  "))

# ilgis = len(slapt)

# rastas_skaicius = False
# rasta_didz_raide =False
# rasta_mazoj_raide = False

# if ilgis == 5:
#     print("Tikrinamas slaptazodis")


#     if slapt[0].isnumeric():
#         rastas_skaicius = True
        
#     elif slapt[1].isnumeric():
#         rastas_skaicius = True
        
#     elif slapt[2].isnumeric():
#         rastas_skaicius = True
        
#     elif slapt[3].isnumeric():
#         rastas_skaicius = True
        
#     elif slapt[4].isnumeric():
#         rastas_skaicius = True


#     if slapt[0].isupper():
#         rasta_didz_raide = True
        
#     elif slapt[1].isupper():
#         rasta_didz_raide = True
        
#     elif slapt[2].isupper():
#         rasta_didz_raide = True
        
#     elif slapt[3].isupper():
#         rasta_didz_raide = True
        
#     elif slapt[4].isupper():
#         rasta_didz_raide = True


#     if slapt[0].islower:
#         rasta_mazoj_raide = True

#     elif slapt[1].islower:
#         rasta_mazoj_raide = True
    
#     elif slapt[2].islower:
#         rasta_mazoj_raide = True
    
#     elif slapt[3].islower:
#         rasta_mazoj_raide = True
  
#     elif slapt[4].islower:
#         rasta_mazoj_raide = True


#     if rastas_skaicius == True and rasta_didz_raide == True and rasta_mazoj_raide == True :
#         print("Slaptazodis teisingas")
#     else:
#         print("Slaptazodis neteisingas")
#         exit()

# else:
#     print("Per trumpas slaptazodis")
#     exit()


# 11
# Naudotojas įveda 3 atsitiktinius skaičius, išrykiuokite juos nuo mažiausio iki didžiausio, nenaudodami ciklų

# pirmas = int(input("Iveskite pirma bet koki skaiciu "))
# antras = int(input("Iveskite antra bet koki skaiciu "))
# trecias = int(input("Iveskite trecia bet koki skaiciu "))

# # pirmas = 5
# # antras = 18
# # trecias = 1

# listas = [pirmas,antras, trecias]
# listas.sort()

# print(listas)

# 12
# Turi būti žodynas, kuriame saugomi valiutų kursai (EUR, USD, GBP). Vartotojas įveda pradinę valiutą, tikslinę valiutą ir sumą. 
# Programa konvertuoja sumą pagal kursą. Jei valiuta neegzistuoja – išveda klaidos pranešimą.

# valiutu_kursai = {"ZAR":20.42, "USD":1.06, "PLN":4.34, "JPI":165.17, "EUR":1.00}

# pradine_valiuta =input("Iveskite pradine valiuta ")
# tiksline_valiuta = input("Iveskite tiksline valiuta ")

# # pradine_valiuta = "EUR"
# # tiksline_valiuta = "ZAR"

# if pradine_valiuta not in valiutu_kursai or tiksline_valiuta not in valiutu_kursai:
#     print("klaida")
#     exit()

# suma = int(input("Iveskite suma "))
# # suma = 10

# pradine_suma = (valiutu_kursai.get(pradine_valiuta))*10
# print(pradine_suma)

# konvertuota_suma = pradine_suma*(valiutu_kursai.get(tiksline_valiuta))
# print(konvertuota_suma)

# print(f"Konvertuota suma yra: {konvertuota_suma:.2f}")

# ---------KITAS VARIANTAS-----

# exchange_rate = {
#     "EUR": {"EUR": 1.0,
#             "USD": 1.04,
#             "GBP": 0.84},
#     "USD": {"EUR": 0.96,
#             "USD": 1.0,
#             "GBP": 0.81},
#     "GBP": {"EUR": 1.2,
#             "USD": 1.24,
#             "GBP": 1.0}
# }
 
# user_input = input("Įveskite pradinę valiutą(EUR, USD, GBP), tikslinę valiutą(EUR, USD, GBP) ir sumą: ").replace(",", "").split()
# # EUR GBP 50 -> ["Eur", "GBP", 50] | user_input[0] = EUR | user_input[1] = GBP | user_input[2] = "50"
# if user_input[0] in exchange_rate and user_input[1] in exchange_rate:
#     rate = exchange_rate[user_input[0]][user_input[1]] # exchange_rate[user_input[0]] {"EUR": 1.0, "USD": 1.04,"GBP": 0.84}
#     output = float(user_input[2]) * rate # 50 * 0.84
 
#     print(f"{user_input[2]} {user_input[0]} yra {output} {user_input[1]}")
# turi kontekstinį meniu
