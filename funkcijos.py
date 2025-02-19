# def pasisveikinti(): #visos funkcijos prasideda def (define) + funkcijos_pavadinimas + ():
#     print("Sveiki")
#     print("Funkcija veikia")
# print("Funkcija nebevyksta")
 
# pasisveikinti() # funkcijos iskvietimas / function call
# print("programa baigta")


# def pasisveikinti(vardas): # vardas - argumentas, privaloma pateikti | vardas = "Jonas"
#     vardas = "Simas"
#     print(f"Sveiki {vardas}")
 
# name = "Jonas" # sukuriamas kintamasis name
# pasisveikinti(name) # kvietimo metu privalome pateikti visus argumentus
# pasisveikinti(name)
# pasisveikinti(name)
# pasisveikinti(name)
# print(name)

# def suma(sk1, sk2): # funkcija su 2 argumentais - sk1 ir sk2 | sk1 = 4 | sk2 = 9
#     print(f"suma yra: {sk1+sk2}")
 
# suma(4,9) # eiliskumas svarbus
# suma(5,7) # eiliskumas svarbus
 

#  def suma(sk1, sk2): # funkcija su 2 argumentais - sk1 ir sk2 | sk1 = 4 | sk2 = 9
#     print(f"suma yra: {sk1+sk2}")
 
# suma(4,9) # eiliskumas svarbus
# suma(5,7) # eiliskumas svarbus
 
# def suma(sk1, sk2):
#     return sk1 + sk2 # return zodelis - programai vykstant istato vietoje funkcijos jos grazinama reiksme
 
# grazinta_reiksme = suma(4,9) # grazinta_reiksme = 13
# print(f"Suma yra: {grazinta_reiksme*2}")
 
#  Jeigu funkcijoje nera return, jos iskvietimo rezultatas yra None
 
# Jeigu yra return, rezultatas yra, reiksme nurodyta prie return

# def saraso_spausdinimas(sarasas):
#     # print(sarasas)
#     return 9 # po return funkcija nera vykdoma, sekancios eilutes yra praleidziamios
#     print(sarasas)
 
# saraso_spausdinimas([4,2,5,8,2,20])


#  def pasisveikink(vardas):
#     if vardas == "Justas":
#         return f"Sveiki destytojau {vardas}"
#     else:
#         print("Dar nebaigiau, nes ne destytojas")
#     print("Funkcijos pabaiga")
   
# print(pasisveikink("Justa"))

# 1 UZDUOTIS

# def sumavimas(sk1, sk2, sk3):
#     # print(sk1+sk2+sk3)
#     return (sk1+sk2+sk3)

# sudeta = sumavimas(2,3,5)
# print(sudeta)

# 2 UZDUOTIS

# def pasisveikinimas(vardas):
#     print(f"Sveiki {vardas}")

# vardas = input("Iveskite savo varda ")
# pasisveikinimas(vardas)

# 3 UZDUOTIS

# def tikrinimas(skaicius):
#     if skaicius == 0:
#         print("Skaicius lygus nuliui")
#     elif skaicius <0:
#         print("Skaicius neigiamas")
#     else:
#         print("Skaicius teigiamas")

# ivestas_skaicius = int(input("Iveskite skaiciu "))

# tikrinimas(ivestas_skaicius)

# 4 UZDUOTIS

# def vaisiai (sarasas):
#     ilgis = len(sarasas)
#     return ilgis

# rusys = ["obuolys","kriause","citrina"]

# kiekis = vaisiai(rusys)
# print(kiekis)

# 5 UZDUOTIS

# def grazinimas(sarasas):
#     suma = 0
#     for x in sarasas:
#         suma += x
#     return suma

# skaiciai = [1,2,3,4,5,6]

# print(grazinimas(skaiciai))

# 6 UZDUOTIS

# def kvadratu (sarasas):
#     pakelti = []

#     for x in sarasas:
#         pakelti.append(x*x)

#     return pakelti

# sarasas = [1,2,3,4,5,6]

# print(kvadratu(sarasas))


# def nebutini(sk,sk2,sk3=1): # numatytoji reiksme tai reiksme kuri bus naudojama, jeigu nieko nepaduodame
#     return (sk+sk2)*sk3
 
# print(nebutini(sk2=5, sk3=7))
 
 
# def nebutini(sk,sk2,sk3=1): #
#     return (sk+sk2)*sk3
 
# print(nebutini(7,5))
# ---------------------------------------------------------------------------

# 1 UZDUOTIS
# Sukurk funkciją, kuri priima sąrašą skaičių ir grąžina didžiausią skaičių tame sąraše.


# def didziausias (isrinkti):
#     naujas_sarasas = []
#     skaicius = issirinkti[0]

#     for x in isrinkti:
#         naujas_sarasas.append(int(x))
    
#     for z in naujas_sarasas:
#         if z > skaicius:
#             skaicius = z
#     return skaicius

# skaiciu_sarasas =input("Suveskite saraso skaicius ").replace(","," ").split()


# print(f" Didziausias skaicius jusu sarase yra: {didziausias(skaiciu_sarasas)}")

# skaiciu_sarasas = [2,5,10,1,3,101]

# def didziausias (isrinkti):
#     skaicius = 0
#     for x in isrinkti:
#         if x > skaicius:
#             skaicius = x
#     return skaicius

# print(f" Didziausias skaicius sarase yra: {didziausias(skaiciu_sarasas)}")

# 2 UZDUOTIS
# Parašyk funkciją, kuri tikrina, ar duotas skaičius yra lyginis ar nelyginis.

# def tikrinimas(suvestu):

#     if suvestu % 2 ==0:
#         print (f"{round(suvestu)} skaicius yra lyginis")
#     elif suvestu % 2 !=0:
#         print (f"{round(suvestu)} skaicius yra nelyginis")


# try:
#     ivestas_skaicius = input("Iveskite tikrinama skaiciu ")

#     if ivestas_skaicius.isdigit() or ivestas_skaicius.replace(".","").replace("-","").isdigit():
#         ivestas_skaicius = float (ivestas_skaicius)
#     else:
#          raise ValueError ("Ivedete ne skaiciu")
    
# except ValueError as ex:
#     print(ex)
#     exit()

# tikrinimas(ivestas_skaicius)


# def tikrinimas(suvestu):
#         if suvestu % 2 ==0:
#             print (f"{suvestu} skaicius yra lyginis")
#         elif suvestu % 2 !=0:
#             print (f"{suvestu} skaicius yra nelyginis")
        
# ivestas_skaicius = int(input("Iveskite tikrinama skaiciu "))

# tikrinimas(ivestas_skaicius)

# 3 UZDUOTIS
# Parašyk funkciją, kuri gauna skaičių n ir grąžina n daugybos lentelę nuo 1 iki 10.

# def dauginimui (ivestis):
#     daugikliai = [0,1,2,3,4,5,6,7,8,9,10]

#     for x in daugikliai:
#         rezult = ivestis*x
#         print (f"{ivestis}*{x}={rezult}")

# pasirinktas_skaicius = int(input ("Iveskite skaiciu "))

# dauginimui(pasirinktas_skaicius)

# 4 UZDUOTIS
# Sukurk funkciją, kuri pašalina visus pasikartojančius elementus iš sąrašo. (galite naudoti set, jeigu mokate)

# sarasas = [2,5,10,1,3,101,2,5,10,1,3,101,2,5,10,1,3,101]

# def pasikartojantiems(pradinis_sarasas):
#     setas = set(pradinis_sarasas)
#     return setas


# print(pasikartojantiems(sarasas))

# PERZIURETI IR PATAISYTI-----------------------------------------------

# """ Sukurkite funkciją, kuri priima skaičių sąrašą ir grąžina jų kvadratų sąrašą. """
 
# def skaiciu_kvadratai(sarasas):
#     return [skaicius ** 2 for skaicius in sarasas if isinstance(skaicius, (int, float))]
 
# # Test the function
# test_sarasas = [1, 2, 3, 4, 5, 6, 7, True, "Labas"]
# print(skaiciu_kvadratai(test_sarasas))

# # Sukurk funkciją, kuri priima sąrašą skaičių ir grąžina didžiausią skaičių tame sąraše.
 
# def the_highest_number (listas_def):
#     highest = listas_def[0]
#     for i in listas_def:
#         if int(i) > int(highest):
#             highest = i
#     return highest
 
 
# listas = input(' iveskite skaicius: ')
# listas = listas.split()
 
# print(the_highest_number(listas))

# # Parašyk funkciją, kuri tikrina, ar duotas skaičius yra lyginis ar nelyginis.
 
# def odd_even(num):
#     if num % 2 == 0:
#         rez = "Lyginis"
#     else:
#         rez = "Nelyginis"
#     return rez    
     
 
# while True:
#     try:
#         input_num = input("Įveskite skaičių: ")
#         num_conversion = int(input_num)
#         break  
#     except ValueError:
#         print("Bloga įvestis, įveskite skaičių: ")
#        # continue - siuo atveju nera butinas
       
# print(f"{input_num} yra {odd_even(num_conversion)} skaičius")

# def tikrinamas(skaitmuo):
#     if skaitmuo %2 == 0:
#         return "Lyginis: "
#     else:
#         return "Nelyginis: "
   
 
# ivestis = input("Jei norite paleisti programą, spauskite ENTER. Jei norite išjungti, įveskite 'off': ")
# if ivestis.lower() == "off":
#     print("Programa išjungta.")
# else:
#     while True:
#         try:
#             skaicius = int(input("Įveskite sveikąjį skaičių: "))
#             print(f"skaičius yra: {tikrinamas(skaicius)}")
#         except ValueError:
#             print("Klaida: Įveskite sveikąjį skaičių: ")
 

#  # Parašyk funkciją, kuri gauna skaičių n ir grąžina n daugybos lentelę nuo 1 iki 10.
# # Pvz., daugybos_lentele(5) turėtų grąžinti 5 x 1 = 5, 5 x 2 = 10, ir t.t.
 
# def mult_table(num):
#     results = []
#     for i in range(1,11):
#         mult = num * i
#         results.append(mult)
#     return results
 
# while True:
#     try:
#         user_input = input("Įveskite skaičių: ")
#         num_conversion = int(user_input)
#         break
#     except ValueError:
#         print("Bloga įvestis, įveskite skaičių: ")
 
# result_list = mult_table(num_conversion)
 
# for i in range (1,11):
#     print(f"{num_conversion} * {i} = {result_list[i-1]}")

#     # Sukurk funkciją, kuri pašalina visus pasikartojančius elementus iš sąrašo. (galite naudoti set, jeigu mokate)
 
# def remove_similar(given_list):
#     new_set = set(given_list)
#     return new_set
 
# while True:
#     user_input = input("Įveskite skaičius atskirtus tarpais: ")
 
#     string_list = user_input.split()
 
#     try:
#         user_list = []
#         for i in string_list:
#             num = int(i)
#             user_list.append(num)
#         break
#     except ValueError:
#         print("Bloga įvestis, veskite tik skaičius")
#        # continue
 
# print(remove_similar(user_list))

# while True:
#     pasirinkimas = input("1. Prideti knyga \n2. Atvaizduoti knygas\njeigu norite isjungti paspauskite q")
#     if pasirinkimas == 1:
#         # kvieciame funkcija prideti knyga
#     elif pasirinkimas == 2:
#         # kvieciame funkcija parodyti visas knygas
#     elif pasirinkimas == 'q':
#         break # bet jeigu visa programa yra while cikle, po break irgi programa nutruks
#         exit() # po exit programa nutraukiama
# turi kontekstinį meniu

# zodynas = [{"pavadinimas":"Haris poteris","metai":1999,"Zanras":"Fantastika"}, {"pavadinimas":"Robinas Hudas","metai":1969,"Zanras":"Romanas"}]
 
# print(zodynas)
# print(zodynas[0]['Zanras'])
# turi kontekstinį meniu


# def galutine_kaina(kaina,kiekis,nuolaida,ar_taikoma_nuolaida): # nuolaida - 0.9
#     gal_kaina = kaina * kiekis
 
#     if ar_taikoma_nuolaida:
#         gal_kaina = gal_kaina * nuolaida
#     return gal_kaina
 
# rezultatas = galutine_kaina(10,1,0,False)
 
# print(f"Jusu galutine kaina yra: {rezultatas}")

# 
# globalus = 10
# def funkcija():
#     lokalus = 12
#     suma = globalus + lokalus
#     print(suma)
 
# kita_suma = globalus + lokalus
 
# funkcija()
# globalus = 10
 
# def funkcija():
#     global globalus # global zodelis funkcijoje pasako, kad jos viduje naudosime ne kopija o originala(t.y. globalu kintamaji)
#     lokalus = 12
#     globalus = 19 # is esmes yra kopija globalaus padaryta lokaliu
#     suma = globalus + lokalus # lokalus islieka funkcijos viduje
#     print(suma)
 
# # kita_suma = globalus + lokalus
 
# # print(kita_suma)
# funkcija()
# print(globalus)

# def kubu(sk):
#     return sk ** 3
 
# funkcija = lambda sk: sk ** 3
 
# print(funkcija(5))
# sar = []
# for sk in range(11):
#     if sk > 3:
#         sar.append(sk*2)
 
# sarasas = [sk*5 for sk in range(11) if sk > 3] # ka ideti i sarasa | ciklas | dejimo salyga
 
# print(sarasas)
 
# sarasas = [x+1 if x >= 45 else x+5 for x in range(10)] # ka ideti i sarasa | dejimo salyga | ciklas
# print(sarasas)

# def kubu(sk):
#     return sk ** 3
 
# skaiciai = "4 8 5 9 5 21 5 8 4 536".split()
# # print(skaiciai)
 
# # ns = []
# skaiciai = [int(sk) for sk in skaiciai] # padarom visus skaicius integeriais
 
# sarasas = list(map(kubu, skaiciai)) # map pritaiko funkcija kiekvienam saraso elementui atitinka toki dalyka:
 
# # for sk in skaiciai:
# #     ns.append(kubu(sk))
 
# print(sarasas)



# 1.1 UZDUOTIS
# 1.Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args)

# def didziausias(*args):
#     did = args[0]
#     for skaicius in args:
#         if skaicius>did:
#             did = skaicius
#     return did

# print(f"Didziausias saraso skaicius: {didziausias(2,10,8,1)}")

# # 1.2 UZDUOTIS
# # 2.Gražintų paduotą stringą atbulai.

# def grazina_atbulai(ivestis):
#     ivestis_atbulai = ivestis.split()
#     return ivestis_atbulai[::-1]

# # vartotojo_fraze = "Man salta"
# vartotojo_fraze = input("Iveskite savo fraze is keliu zodziu: ")
# print(f"Jusu fraze atbulai yra: {grazina_atbulai(vartotojo_fraze)}")

# 1.3 UZDUOTIS
# 3.Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.

# def skaiciavimas(fraze):
#     zodziu_skaicius = len(fraze.split())
#     fraze = list(fraze.replace(" ",""))
#     did_raides = 0
#     maz_raides = 0

#     for elementas in fraze:
#         if elementas.isupper():
#             did_raides = did_raides + 1
#         elif elementas.islower():
#             maz_raides = maz_raides + 1

#     return f"Jusu frazeje yra:\n {zodziu_skaicius} zodziai.\n {did_raides} didziosios raides.\n{maz_raides} mazosios raides."

# ivestis = "2025 LABAI salta salta"
# # ivestis = input("Iveskite fraze is keliu zodziu ")

# print(skaiciavimas(ivestis))

# 1.4 UZDUOTIS
# 4.Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.

# def grazinimas (pateiktas):
#     unikalus = set(pradinis_sarasas)

#     return f"Unikalios reiksmes jusu sarase yra: {unikalus}"

# pradinis_sarasas = [2,10,6,2,10,6,2,10,6]

# print(grazinimas(pradinis_sarasas))

# def grazinimas (pateiktas): !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     pradinis_elementas = pateiktas[0]
#     for elementas in pateiktas:
#         if elementas != pradinis_elementas:
#             unikalus.append(elementas)

#     return unikalus

# pradinis_sarasas = [2,10,True,6,2,10,6,"saule",2,10,6]

# print(grazinimas(pradinis_sarasas))


# 1.5 UZDUOTIS
# 5.Gražintų, ar paduotas skaičius yra pirminis.

# def skaiciu_atrinkimas (tikrinamas):
#     if tikrinamas<=1:
#         return " ne pirminis"
    
#     for i in range(2, tikrinamas):

#         if tikrinamas % i == 0:
#             return " ne pirminis"
    
#     return " pirminis"

# skaicius = int(input("Iveskite skaiciu: "))

# print(f"Ivestas skaicius yra{skaiciu_atrinkimas(skaicius)}")


# 1.6 UZDUOTIS
# 6.Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo

# def zodziu_rykiavimas(fraze):
#     isrykiuotas = fraze.split()

#     return isrykiuotas[::-1]

# # ivestis = "Jau greit pavasaris"
# ivestis = input("Iveskite fraze is keliu zodziu: ")

# print(zodziu_rykiavimas(ivestis))


# 1.7 UZDUOTIS
# 7.Gražina, ar paduoti metai yra keliamieji, ar ne.

# def metu_tikrinimas (pasirinkti_metai):

#     if pasirinkti_metai % 400 == 0 or pasirinkti_metai % 4 == 0:
#         return "Tai keliamieji metai"

#     elif pasirinkti_metai % 100 == 0:
#         return "Tai ne keliamieji metai"

#     else:
#         return "Tai ne keliamieji metai"
    
# # ivestis = 2000
# ivestis = int(input("Iveskite metus kuriuos norite patikrinti: "))

# print(metu_tikrinimas(ivestis))


# 1.8 UZDUOTIS
# 8.Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.

# import datetime

# def sukaktis (pirmine_data):

#     dabartine_data = datetime.datetime.today()
#     pirmine_data = datetime.datetime.strptime(pirmine_data,"%Y-%m-%d")

#     sekundes = (dabartine_data-pirmine_data).total_seconds()
#     minutes = sekundes/60
#     val = minutes/60
#     dienos = (dabartine_data-pirmine_data).days
#     menesiai = (dabartine_data.year-pirmine_data.year)*12+(dabartine_data.month-pirmine_data.month)
#     metai = dabartine_data.year-pirmine_data.year

#     return f"Nuo sukakties datos praejo:\n{metai} metai.\n{menesiai} menesiu.\n{dienos} dienu.\n{val} valandu.\n{minutes} minuciu.\n{sekundes} sekundziu."

# # ivestis = "1989-03-26"
# ivestis = input("Iveskite sukakties data formatu: yyyy-mm-dd ")

# print(sukaktis(ivestis))


# 2.1 UZDUOTIS
# 1.Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.

# def validus_kodas(A,B,C,D,E,F,G,H,I,J,K):
#    suma1 = A*1 + B*2 + C*3 + D*4 + E*5 + F*6 + G*7 + H*8 + I*9 + J*1
#    if suma1 % 11 != 10:
#       K = suma1
#    else suma1 % 11 == 10:
#       suma1 = A*3 + B*4 + C*5 + D*6 + E*7 + F*8 + G*9 + H*1 + I*2 + J*3
      

#    return 0




# ivestis =list("48903261522")
# paversta_skaiciais = [int(skaicius) for skaicius in ivestis]
# print(paversta_skaiciais)

# validus_kodas(paversta_skaiciais[0],paversta_skaiciais[1],paversta_skaiciais[2],paversta_skaiciais[3],paversta_skaiciais[4],paversta_skaiciais[5],paversta_skaiciais[6],paversta_skaiciais[7],paversta_skaiciais[8],paversta_skaiciais[9],paversta_skaiciais[10])


# 3.1 UZDUOTIS
# 1.Sukurti funkciją, kuri grąžintų True reikšmę, 
# jei įvesto skaičiaus pirma skaitmenų pusė yra lygi antrąjai, priešingu atveju grąžintų False.

# def grazinimas(ivestas_skaicius):
#    ivestas_skaicius = list(ivestas_skaicius)
#    paversta_skaiciais = [int(skaicius) for skaicius in ivestas_skaicius]
  
#    print(paversta_skaiciais)

#    ilgis = len(paversta_skaiciais)
#    print(ilgis)

#    if ilgis % 2 == 0:
#       puses_ilgis = ilgis/2
#       puses_ilgis = 0

#       for x in range

   #       print(puses_ilgis)
   #       print(paversta_skaiciais)
   #       print(ivestas_skaicius)
#    return 0

# ivestis = "1597"
# # ivestis = input("iveskite skaiciu: ")

# grazinimas(ivestis)


# 3.2 UZDUOTIS
# 2.Parašyti funkciją, kuri grąžintų, kiekvieno elemento gretimą skaičių. Pvz:
#       Input: 5678
#       Output: 5 – 46, 6 – 57, 7 – 68, 8 - 79

# def poru_kurimas(ivestas_skaicius):
#     ilgis = len(ivestas_skaicius)

#     for skaicius in ivestas_skaicius[0:(ilgis-2)]:
        

#     print()
    
#     return 0


# ivestis = "5869"
# # ivestis = input("Iveskite skaiciu")

# poru_kurimas(ivestis)



# -------------------------------------
# 1.Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
 
# def max_number(*args):
#     return max(args)
 
# stringas = input("Įveskite norimus skaičius atskirdami juos tarpeliais: ").split()
# stringas = [int(e) for e in stringas]
# print("Jūsų sukurtas sąrašas:", stringas)
# # print("Didžiausias skaičius sąraše yra:", max_number(*stringas))
# print("Didžiausias skaičius sąraše yra:", max_number(4, 5, 99, 7))
 
#-----------------------------------------------------------------------
# 2.Gražintų paduotą stringą atbulai.
 
# def backw(stri):
#     return stri[::-1]
 
# stringas = input("\nĮveskite norimus elementus atskirdami tarpeliais: ")
# print("Jūsų sukurti elementai:", stringas)
# print("Elementai buvo apversti:", backw(stringas))
 
#-----------------------------------------------------------------------
# 3.Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
 
# def exam(sentence):
#     words = sentence.split()
#     count_words = len(words)
#     upper_c = sum(1 for e in sentence if e.isupper())
#     lower_c = sum(1 for e in sentence if e.islower())
#     is_digit = sum(1 for e in sentence if e.isdigit())
#     exam = (f"Sakinyje yra {count_words} žodžiai, {upper_c} - didžiosios raidės, {lower_c} - mažosios raidės ir {is_digit} skaičiai")
#     return exam
 
# sentence = input("Sukurkite sakinį: ")
# print(f'Jūsų sukurtas sakinys: {sentence}')
# print(exam(sentence))
     
#-----------------------------------------------------------------------
# 4.Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.
# 1.Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
 
# def max_number(*args):
#     return max(args)
 
# stringas = input("Įveskite norimus skaičius atskirdami juos tarpeliais: ").split()
# stringas = [int(e) for e in stringas]
# print("Jūsų sukurtas sąrašas:", stringas)
# # print("Didžiausias skaičius sąraše yra:", max_number(*stringas))
# print("Didžiausias skaičius sąraše yra:", max_number(4, 5, 99, 7))
 
#-----------------------------------------------------------------------
# 2.Gražintų paduotą stringą atbulai.
 
# def backw(stri):
#     return stri[::-1]
 
# stringas = input("\nĮveskite norimus elementus atskirdami tarpeliais: ")
# print("Jūsų sukurti elementai:", stringas)
# print("Elementai buvo apversti:", backw(stringas))
 
#-----------------------------------------------------------------------
# 3.Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
 
# def exam(sentence):
#     words = sentence.split()
#     count_words = len(words)
#     upper_c = sum(1 for e in sentence if e.isupper())
#     lower_c = sum(1 for e in sentence if e.islower())
#     is_digit = sum(1 for e in sentence if e.isdigit())
#     exam = (f"Sakinyje yra {count_words} žodžiai, {upper_c} - didžiosios raidės, {lower_c} - mažosios raidės ir {is_digit} skaičiai")
#     return exam
 
# sentence = input("Sukurkite sakinį: ")
# print(f'Jūsų sukurtas sakinys: {sentence}')
# print(exam(sentence))
     
#-----------------------------------------------------------------------
# 4.Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.
 
# def unique(elements):
#     my_list = elements.split()
#     unique = set(my_list)
#     return list(unique)
 
# elements = input("\nĮveskite norimus elementus atskirdami tarpeliais: ")
# print(unique(elements))
# #  


# 5.Gražintų, ar paduotas skaičius yra pirminis.
 
# def ar_pirminis(sk : int):
#     if sk == 1 or sk == 2:
#         return True
#     for i in range(3, sk):
#         if sk % i == 0:
#             return False
#     return True
 
# print(ar_pirminis(int(input("Iveskite skaiciu: \n"))))
 
 
 
 
 
# 6.Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
 
# def atbulas(tekstas : str):
#     zodziai = tekstas.split()
#     return " ".join([zodis for zodis in zodziai[::-1]])
 
# print(atbulas(input("Iveskite teskta: \n")))
 
 
 
# 7.Gražina, ar paduoti metai yra keliamieji, ar ne.
# def ar_keliamieji(metai):
#     return (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0)
 
# print(ar_keliamieji(int(input("Iveskite metus: \n"))))
 
 
# 8.Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.
# import datetime, dateutil
# import dateutil.relativedelta
# def kiek_laiko(sukaktis : datetime.datetime):
#     skirtumas = dateutil.relativedelta.relativedelta(datetime.datetime.now(), sukaktis)
#     print(f"Metu: {skirtumas.years}")
#     print(f"Menesiu: {skirtumas.months}")
#     print(f"Dienu: {skirtumas.days}")
#     print(f"Valandu: {skirtumas.hours}")
#     print(f"Minuciu: {skirtumas.minutes}")
#     print(f"Sekundziu: {skirtumas.seconds}")
 
# kiek_laiko(datetime.datetime.strptime(input("Iveskite data: YYYY-MM-DD HH:MM:SS \n"), "%Y-%m-%d %H:%M:%S"))
 
 
 
#  --------------------------------------------------------

# 2 UZDUOTIS

# 1.Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.
# 2.Padaryti, kad programa sugeneruotų teisingą asmens kodą 
# (panaudojus anksčiau sukurtą funkciją) pagal įvestą lytį, gimimo datą ir eilės numerį).

def asmens_kodas(skaiciai):
    
    konvertuota_ivestis = [int(skaitmuo)for skaitmuo in skaiciai]
    raides = ["A","B","C","D","E","F","G","H","I","J","K"]
    raides = konvertuota_ivestis

    S = "A"*1 + "B"*2 + "C"*3 + "D"*4 + "E"*5 + "F"*6 + "G"*7 + "H"*8 + "I"*9 + "J"*1
    print(S)
    





    return 0





ivestis = "48903261522"
asmens_kodas(ivestis)
