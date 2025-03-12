# skaicius = 10
# while skaicius >0 and skaicius<10:
#     skaicius = skaicius - 1
#     print(skaicius)

# DIENOS PIETUS------------------------------

# Aprašymas:
# Sukurk žodyną, kuriame raktai (keys) – savaitės dienos, o reikšmės (values) 
# – siūlomas dienos pietų patiekalas. Tada paklausk vartotojo, kokia šiandien diena, ir išvesk atitinkamą patiekalo rekomendaciją.

# 1.
# Sukurkite ciklą su range komanda, kuris išspausdins skaičius nuo 1 iki 6.

# for skaicius in range(1,7):
#     print(skaicius)

# 2.
# Sukurkite ciklą, kuris išspausdins raides A B C D E

# for raides in "ABCDE":
#     print(raides)

3.
# Sukurkite žodyną {"France": "Paris", "Japan": "Tokyo", "USA": "Washington DC"}, 
# tada sukurkite ciklą, kuris išspausdins šalių pavadinimus, o po to – kitą ciklą, kuris išspausdins sostinių pavadinimus.

# dictionary = {"France": "Paris", "Japan": "Tokyo", "USA": "Washington DC"}

# # for salys in dictionary:
# #     print(salys)
    
# for valstybes in dictionary:

#     # sostines = dictionary.get(sostines)

#     sostines = dictionary[valstybes]
#     print(sostines)

# dictionary.get(sostines) - paima REIKSME is zodyno. nesukelia klaidos jei reiksmes nera. taspats = dictionary[key]/dictionary[valstybes]

# 4.
# Sukurkite ciklą, kuris pereina per sąrašą [1, 10, 9, 4] ir patikrina, ar kiekvienas skaičius yra didesnis už 3.

# listas = [1, 10, 9, 4]

# for skaicius in listas:
#     if skaicius>3:
#         print( skaicius)

# 5.
# Sukurkite ciklą, kuris pereina per sąrašą ["France", "Japan", "the USA"] ir ieško "the USA" sąraše.

# listas = ["France", "Japan", "the USA"]

# for salis in listas:
#     if salis == "the USA":
#         print(" sita salis USA")
#     else:
#         print("tai ne USA")

# 6.
# Sukurkite ciklą, kuris pereina per sąrašą [-1, 2, 3, 0, -4] ir patikrina, ar kiekvienas skaičius yra teigiamas, ar neigiamas.

# listas = [-1, 2, 3, 0, -4]

# for skaicius in listas:
#     if skaicius>0:
#         print(skaicius, "Teigiamas")
#     else:
#         print(skaicius, "neigiamas")

# 7. 
# Create code with a nested loop based on the list of lists
#  [["apple", "orange"], ["carrot", "cabbage"], ["chicken", "beef"]] which produces the output shown below:

# listas = [["apple", "orange"], ["carrot", "cabbage"], ["chicken", "beef"]] 

# for produktai in listas:
#     for po_viena in produktai:
#         print(po_viena)

# DATETIME------------------------------------------

import datetime

# Užduotis 1:
# Parašykite kodą, kuris išveda dabartinę datą ir laiką.

# laikas_dabar = datetime.datetime.now()
# print(laikas_dabar)

# Užduotis 2:
# Sukurkite kintamąjį, kuriame bus jūsų gimimo data (pvz., "1995-05-12") ir išveskite ją kaip datetime objektą.

# dob = "1995-05-12"
# gim_data = datetime.datetime(1995,5,12)
# print(gim_data)

# Užduotis 3:
# Pasinaudokite datetime moduliu ir išveskite, kiek dienų praejo nuo 2020-01-01 iki šiandienos.

# pradzia = datetime.datetime(2020,1,1)
# print(pradzia)
# pabaiga = datetime.datetime.now()
# print(pabaiga)

# praejo = (pabaiga-pradzia).days
# print(praejo)

# Užduotis 4:
# Paverskite tekstinį datą ("2023-08-15") į datetime objektą ir išveskite dienos pavadinimą (pvz., pirmadienis, antradienis).

# data_tekst = "2023-08-15"
# data = datetime.datetime.strptime(data_tekst, "%Y-%m-%d")
# diena = data.strftime("%A")
# print(diena)

# Užduotis 5:
# Naudodami timedelta, sukurkite datą, kuri bus 5 dienos po šiandienos. Išveskite šią datą.

# siandien = datetime.datetime.now()
# dienos = datetime.timedelta(days=5)
# po_5_dienu = siandien+dienos
# print(po_5_dienu)

# Užduotis 6:
# Suskaičiuokite, kiek valandų ir minučių praėjo nuo 2023-01-01 12:00 iki dabar.

# siandien = datetime.datetime.now()
# pradzia = datetime.datetime(2023,1,1)

# praejo_sekundziu = (siandien-pradzia).total_seconds()
# print(praejo_sekundziu)

# minuciu = praejo_sekundziu/60
# valandu = minuciu/60

# print(minuciu)
# print(valandu)





