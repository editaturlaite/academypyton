# try: # Programa megins vykdyti koda kuris yra try bloke
#     print("Prasidejo try blokas")
#     sarasas = [1,2,3]
#     print(sarasas[5])
#     7/0
#     int("Labas")
#     print("Veikiu viskas tvarkoje")
# except ZeroDivisionError: # Jeigu try bloke ivyks klaida, jis vykdys except bloko koda
#     print("Dalyba is nulio negalima")
# except ValueError:
#     print("Negalima tokios reiksmes konvertuoti")
# except IndexError:
#     print("Per mazas/didelis indeksas")

# try: # Programa megins vykdyti koda kuris yra try bloke
#     print("Prasidejo try blokas")
#     "Labas" + 5
#     # sarasas = [1,2,3]
#     # print(sarasas[5])
#     # 7/0
#     # int("Labas")
#     print("Veikiu viskas tvarkoje")
# except ZeroDivisionError as exception: # Jeigu try bloke ivyks klaida, jis vykdys except bloko koda
#     print("Dalyba is nulio negalima")
#     # irasyk i faila, kad ivyko klaida
# except ValueError as ex: # ex = klaidos_tekstas
#     print(f"Negalima tokios reiksmes konvertuoti {ex}")
#     # irasymas i faila
#     # klaidos sutvarkymas
#     # dar kazkas
#     # dar vienas dalykas, su klaida mes isgausime funkcionaluma
# except IndexError as ex:
#     print("Per mazas/didelis indeksas")
# except Exception as e: # negalima except as e -> reikia except Exception as e
#     print("Ivyko nenumatyta klaida")

# try:
#     # 7/0
#     try:
#         int("Labas")
#     except:
#         print("Vidine klaida")
       
#     print("Tesiama pagrindine programa")
# except:
#     print("Isorine klaida")
 
# print("Programa baigta")


# 1 UZDUOTIS--------------------------------------------------------------------------------------------------------------------------

# listas =[2,"5",5,"Rokas",0.5,2.5, 55.5, 100]
# suma = 0

# for elementas in listas:
#     try:
#         suma = suma+float(elementas)
#         print(suma)
        
#     except ValueError:
#         print(f"elemento {elementas} reikšme yra ne skaicius. Sudeti neglima")
#         ivyko_klaida = True
#         break
# if not ivyko_klaida:
#     print("suma: ",suma)

# BUVES
# for skaicius in listas:
#     if type(skaicius) is int or type(skaicius) is float:
#         suma = suma+skaicius
# print(suma)

# PROGRAMA------------

# skaicius = input("Iveskite skaiciu ")
# skaicius_teigiamas = True
# skaicius_neigiamas = False

# try:
#     if int(skaicius) >0:
#         print(skaicius_teigiamas)
#     else:
#         print(skaicius_neigiamas)
# except ValueError:
#     print("Ivedete ne skaiciu")


# BUVES
# skaicius = int(input("Iveskite skaiciu "))
# skaicius_teigiamas = True
# skaicius_neigiamas = False

# if skaicius >0:
#     print(skaicius_teigiamas)
# else:
#     print(skaicius_neigiamas)


# # 1.1 UZDUOTIS
# import datetime

# # dob = "1989-03-26"

# while True:
#     try:
#         dob = input("Iveskite savo gimimo data. Formatu: yyyy-mm-dd ")
#         dabartine_data = datetime.datetime.today()
#         print(dabartine_data)

#         dob = datetime.datetime.strptime(dob, "%Y-%m-%d")
#         print(dob)

#         sekundes = (dabartine_data-dob).total_seconds()
#         print(round(sekundes))

#         minutes = sekundes/60
#         print(round(minutes))

#         val = minutes/60
#         print(round(val))

#         dienos = (dabartine_data-dob).days
#         print(dienos)

#         men = (dabartine_data.year-dob.year)*12 + (dabartine_data.month-dob.month)
#         print(men)

#         metai = dabartine_data.year-dob.year
#         print(metai)
                
#     except ValueError:
#         print("Ivesti duomenys neatitinka prašomo formato. Bandykite dar karta ")


# BUVES
# dob = "1989-03-26"
# dob = input("Iveskite savo gimimo data. Formatu: yyyy-mm-dd ")
# dabartine_data = datetime.datetime.today()
# print(dabartine_data)

# dob = datetime.datetime.strptime(dob, "%Y-%m-%d")
# print(dob)

# sekundes = (dabartine_data-dob).total_seconds()
# print(round(sekundes))

# minutes = sekundes/60
# print(round(minutes))

# val = minutes/60
# print(round(val))

# dienos = (dabartine_data-dob).days
# print(dienos)

# men = (dabartine_data.year-dob.year)*12 + (dabartine_data.month-dob.month)
# print(men)

# metai = dabartine_data.year-dob.year
# print(metai)



# 2 UZDUOTIS ---------------------------------------------------------
# Buggy Code: Count occurrences of a specific element.
# numbers = [3, 1, 3, 2, 3, 4, 5]
# target = 3
# count = 0
# for i in range(len(numbers)):
#     if numbers[i] == target:
#         count += 1  
# print(f"The number {target} appears {count} times.")

# BUVES
# Buggy Code: Count occurrences of a specific element.
# numbers = [3, 1, 3, 2, 3, 4, 5]
# target = 3
# count = 0
# for i in range(len(numbers)):
#     if numbers[i] == target:
#         count =+ 1  
# print("The number " + target + " appears " + count + " times.")


# 3 UZDUOTIS----------------------------------------------------------

# Buggy Code: Merge two lists alternately.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# merged = []
# for i in range(len(list1)):
#     merged.append(list1[i])
#     merged.append(list2[i])
# print("The merged list is: " + str(merged))

# BUVES
# # Buggy Code: Merge two lists alternately.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# merged = []
# for i in range(len(list1)):
#     merged.append(list1[i])
#     merged.append(list2[i+1])
# print("The merged list is: " + str(merged))


# 4 UZDUOTIS--------------------------------------------------------------------

# Buggy Code: Calculate the sum of border elements in a 4x4 matrix.
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# border_sum = 0
# eilute = len(matrix)
# stulpelis = len(matrix[0])

# for i in range(eilute):
#     for j in range(stulpelis):
#         if i == 0 or i == eilute-1 or j == 0 or j == stulpelis-1:
#             border_sum += matrix[i][j]
# print(f"The sum of the border elements is: {border_sum}")


# BUVES
# # Buggy Code: Calculate the sum of border elements in a 4x4 matrix.
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# border_sum = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if (i == 0 and i == len(matrix)-1) or (j == 0 and j == len(matrix[0])-1):
#             border_sum += matrix[i][j]
# print("The sum of the border elements is: " + border_sum)



# 5 UZDUOTIS-------------------------------------------------------------------

# Tikslas:
# Sukurti programą, kuri cikliškai prašo vartotojo įvesti sveikąjį skaičių, kol bus įvesta teisinga reikšmė.
# Reikalavimai:
# Įvesties tikrinimas:
# Naudokite try/except bloką, kai bandoma įvesties eilutę konvertuoti į sveikąjį skaičių.
# Jei įvyko ValueError, naudokite raise su pritaikyta žinute, pvz.:
# "Neteisinga įvestis: prašome įvesti teisingą sveikąjį skaičių!"
# Ciklas:
# Pakartokite įvesties tikrinimą tol, kol vartotojas įves teisingą sveikojo skaičiaus reikšmę.
# Finally:
# Naudokite finally bloką, kuris po kiekvieno bandymo atspausdintų pvz.:
# "Bandymas baigtas" nepriklausomai nuo to, ar įvyko klaida.

# while True:
#     try:
#         skaicius = input("Iveskite sveikaji skaiciu ")

#         if skaicius.isdigit():
#           print("Ivesta teisinga reiksme")
#           break

#         else:
#             raise ValueError ("Ivesta reiksme neteisinga. Bandykite dar karta")

#     except ValueError as ex :
#         print(ex)
#     finally:
#         print("Bandymas baigtas")


# 6 UZDUOTIS--------------------------------------------------------------

# Tikslas:
# Parašyti programą, kuri paprašys įvesti du skaičius (skaitiklį ir vardiklį) ir atliks dalijimo operaciją.
# Reikalavimai:
# Įvesties konvertavimas:
# Įvestis paversti į skaičius (naudokite int() arba float()) su try/except bloku, kad sugautumėte konvertavimo klaidas (ValueError).
# Dalijimo operacija:
# Naudokite try/except bloką dalijimo operacijai.
# Jei vardiklis yra lygus nuliui, naudokite raise su pritaikyta klaidos žinute, pvz.:
# "Dalinti iš nulio neleidžiama!".
# Finally:
# Po dalijimo (sėkmingo ar ne) atspausdinkite žinutę:
# "Skaičiavimas baigtas".



# while True:
#     skaitiklis = input("Iveskite skaitikli ")

#     try:
#         if skaitiklis.isdigit() or skaitiklis.replace(".","").replace("-","").isdigit():
#             skaitiklis = float(skaitiklis)
#             vardiklis = input("Iveskite vardikli ")
#         else:
#             raise ValueError ("Ivedete ne skaiciu ")


#         if vardiklis.isdigit() or vardiklis.replace(".","").replace("-","").isdigit():
#            vardiklis = float(vardiklis)
               
#         else:
#             raise ValueError ("Ivestas ne skaicius. Bandykite is naujo")


#         try:
#             if vardiklis ==0:
#                 raise ZeroDivisionError ("Dalyba is 0 negalima")
#             else:
#                 atsakymas = skaitiklis/vardiklis
#                 print (f"Atakymas {atsakymas}")
#         except ZeroDivisionError as dal:
#                print(dal)
#         finally:
#             print("skaiciavimas baigtas")

#     except ValueError as ex:
#         print(ex)
    


# # 7 UZDUOTIS--------------------------------------------------------------------

# Tikslas:
# Sukurti programą, kuri turi iš anksto apibrėžtą sąrašą (pvz., vaisių sąrašą) ir paprašyti vartotojo įvesti indeksą, 
# kad būtų pasiektas atitinkamas sąrašo elementas.
# Reikalavimai:
# Sąrašo sukūrimas:
# Apibrėžkite sąrašą, pvz.:
# ["obuolys", "bananas", "vyšnia"].
# Indekso įvedimas:
# Paprašykite vartotojo įvesti indeksą ir jį konvertuokite į sveikąjį skaičių su try/except bloku (klaidoms, jei įvesta ne
#  sveikojo skaičiaus reikšmė).
# Sąrašo pasiekimas:
# Naudokite kitą try/except bloką, kad bandytumėte pasiekti sąrašo elementą.
# Jei indeksas yra neteisingas (gaunami IndexError), sugaukite klaidą ir praneškite vartotojui.
# Jei vartotojas įveda neigiamą indeksą, naudokite raise su žinute:
# "Neigiami indeksai neleidžiami!".
# Finally:
# Baigus bandymą, nepriklausomai nuo rezultato, atspausdinkite:
# "Paieška sąraše baigta".

# produktai = ["obuolys", "bananas", "arbuzas", "kriause", "citrina", "vyšnia"]
# ilgis = len(produktai)

# indeksas = input("Iveskite indeksa ")

# try: 
#     if indeksas.isdigit() or indeksas.replace("-","").isdigit():
#         indeksas = int(indeksas)   
#         try:
#             if indeksas>(ilgis-1):
#                 raise IndexError ("Indeksas uz saraso ribu")
            
#             if indeksas<0:
#                 raise ValueError ("Neigiami indeksai neleidziami")
            
#             print(f"{indeksas} indekse yra {produktai[indeksas]}")

#         except ValueError as nei:
#             print(nei)
#         except IndexError as ind:
#             print(ind) 
#     else:
#         raise ValueError ("Ivedete ne sveikaji skaiciu ")
    
# except ValueError as ex:
#     print(ex)   
# finally:
#     print("Paieska sarase baigta")


# 8 UZDUOTIS---------------------------------------------

# Tikslas:
# Parašyti programą, kuri paprašys vartotojo įvesti datą formatu "YYYY-MM-DD" ir bandys konvertuoti ją į datetime objektą.
# Reikalavimai:
# Datos įvedimas:
# Paprašykite vartotojo įvesti datą nurodytu formatu.
# Datos konvertavimas:
# Naudokite datetime.strptime metodą iš datetime modulio, kad konvertuotumėte įvesties eilutę.
# Įveskite šią operaciją į try/except bloką, kad sugautumėte ValueError, jei formatas neteisingas.
# Klaidos valdymas:
# Jei įvyko klaida, naudokite raise su žinute:
# "Neteisingas formatas! Prašome naudoti YYYY-MM-DD.".
# Finally:
# Po bandymo atspausdinkite:
# "Datos patikrinimas baigtas".

# import datetime

# data = input("Iveskite data formatu: yyyy-mm-dd ")

# try:
#     konvertuota_data = datetime.datetime.strptime(data,"%Y-%m-%d")
#     print(konvertuota_data)

# except ValueError:
#     print("Neteisingas formatas! Prašome naudoti YYYY-MM-DD.")
#     # raise ValueError ("Neteisingas formatas! Prašome naudoti YYYY-MM-DD.")

# finally:
#     print("Datos patikrinimas baigtas")



# 9 UZDUOTIS----------------------------------------------------------
# Tikslas:
# Sukurti programą su iš anksto apibrėžtu žodynu (pvz., šalių ir jų sostinių) ir paprašyti vartotojo įvesti raktą (šalies pavadinimą), kad gautų atitinkamą reikšmę.
# Reikalavimai:
# Žodyno sukūrimas:
# Apibrėžkite žodyną, pvz.:
# {"Lietuva": "Vilnius", "Prancūzija": "Paryžius", "Japonija": "Tokijas"}.
# Įvesties tikrinimas:
# Paprašykite vartotojo įvesti šalies pavadinimą.
# Jei įvestis yra tuščia, naudokite raise su ValueError ir žinute:
# "Įvestis negali būti tuščia!".
# Raktų paieška:
# Naudokite try/except bloką, kad bandytumėte gauti reikšmę pagal įvestą raktą.
# Jei rakto nėra (gaunami KeyError), sugaukite klaidą ir praneškite vartotojui.
# Finally:
# Baigus paiešką, atspausdinkite:
# "Žodyno paieška baigta".

# salys_sostines = {"Lietuva": "Vilnius", "Prancūzija": "Paryžius",
#  "Japonija": "Tokijas", "Vokietija": "Berlynas", "Italija": "Roma", "Ispanija": "Madridas"}

# try:
#     raktas = input("Iveskite salies pavadinima  ")
#     if raktas  == "":
#         raise ValueError ("Įvestis negali būti tuščia!")

#     try:
#         reiksme = salys_sostines.get(raktas)
#         if reiksme is None:
#             raise KeyError ("Tokios salies sarase nera.")
#         print(f"{raktas} sostine yra: {reiksme}")

#     except K as re:
#         print(re)

# except ValueError as ex:
#     print(ex)
# finally:
#     print("Žodyno paieška baigta")


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

# import datetime

# try:
#     try:
#         pradzia = input("Iveskite pradzios data siuo formatu: YYYY-MM-DD ")
#         pradzia = datetime.datetime.strptime(pradzia, "%Y-%m-%d")
#     except ValueError:
#         print("Neteisingas datos formatas! Prašome naudoti YYYY-MM-DD.")
#         klaida = True
#         if klaida:
#             exit()

#     try:
#         pabaiga = input("Iveskite pabaigos data siuo formatu: YYYY-MM-DD ")
#         pabaiga = datetime.datetime.strptime(pabaiga, "%Y-%m-%d")
#     except ValueError:
#         print("Neteisingas datos formatas! Prašome naudoti YYYY-MM-DD.")
#         klaida = True
#         if klaida:
#             exit()

#     try:
#         if pradzia>=pabaiga:
#             raise ValueError ("Pradžios data turi būti ankstesnė nei pabaigos data.")
#     except ValueError as pb:
#         print(pb)

# finally:
#     print("Datos įvedimo bandymas baigtas.\n ")

# savaitgalio_diena = 0
# menesio_pirma = 0
# dienu_skaicius = 0


# while pradzia<=pabaiga:
#     if pradzia.weekday() == 5 or pradzia.weekday() == 6:
#         savaitgalio_diena +=1

#     if pradzia.day == 1:
#         menesio_pirma += 1
#     dienu_skaicius += 1
#     pradzia += datetime.timedelta(days=1)

# print(f"Bendras dienu skaicius: {dienu_skaicius}")
# print(f"Laikotarpyje {savaitgalio_diena} savaitgalio dienu")
# print(f"ir {menesio_pirma} menesiu\n ")

# print("Datos analizė baigta.")



