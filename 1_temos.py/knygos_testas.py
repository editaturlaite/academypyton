# Tikslas:
# Sukurti Python programą, kuri padėtų valdyti bibliotekos knygų sąrašą. Programa turi būti parašyta procedūriniu stiliumi (be klasių ir objektų) 
# ir panaudoti visas iki šiol išmoktas temas: kintamuosius, ciklus, sąlyginius sakinius, funkcijas bei klaidų tvarkymą.

# Reikalavimai:
# Pagrindinis meniu:
# Programa pradžioje turi rodyti meniu su šiais pasirinkimais:
# 1. Pridėti naują knygą
# 2. Atvaizduoti visų knygų sąrašą
# 3. Ieškoti knygos
# 4. Ištrinti knygą
# 5. Išeiti iš programos

# Meniu rodymas ir pasirinkimų vykdymas turi būti įgyvendintas naudojant ciklą, kad vartotojas galėtų atlikti kelis veiksmus iki pat programos pabaigos.

# Naujos knygos pridėjimas:
# Sukurkite funkciją (pvz., prideti_knyga()), kuri paprašys vartotojo įvesti šiuos duomenis:
# Pavadinimas
# Autorius
# Leidimo metai – privaloma patikrinti, ar įvesti metai yra sveikasis skaičius. Naudokite try-except bloką, kad apdorotumėte neteisingą įvedimą.
# Žanras
# Surinktus duomenis išsaugokite sąraše (pvz., kaip žodynus arba sąrašo elementus), kad vėliau būtų galima juos peržiūrėti ir apdoroti.

# Visų knygų sąrašo atvaizdavimas:
# Sukurkite funkciją (pvz., atvaizduoti_knygas()), kuri išveda visų įvestų knygų sąrašą su indeksais (numeracija).
# Naudokite ciklą, kad pereitumėte per knygų sąrašą ir atvaizduotumėte kiekvienos knygos duomenis.


# Knygos paieška:
# Sukurkite funkciją (pvz., ieskoti_knygos()), kuri paprašys vartotojo įvesti paieškos terminą (gali būti pavadinimas arba autorius).
# Naudokite ciklą ir sąlygas, kad surastumėte ir išvestumėte visas knygas, kurios atitinka įvestą terminą (naudokite dalinį atitikimą, pvz.,
#  if paieskos_terminas in knygos['pavadinimas'] arba panašiai).

# Knygos ištrynimas:
# Sukurkite funkciją (pvz., istrinti_knyga()), kuri leistų vartotojui ištrinti knygą pagal jos numerį arba pavadinimą.
# Jei įvestas identifikatorius (numeris ar pavadinimas) neatitinka jokios esamos knygos, naudokite klaidų tvarkymą (pvz., try-except 
# arba patikrinimus su if) ir informuokite vartotoją apie klaidą.

# Patarimai įgyvendinimui:
# Funkcijų struktūra: Kiekviena pagrindinė funkcija (pridėti, atvaizduoti, ieškoti, ištrinti) turėtų būti aprašyta kaip atskira funkcija. Tai padės suskaidyti užduotį į mažesnius, lengviau valdomus modulius.
# Klaidos tvarkymas: Naudokite try-except blokus, ypač kai tikitės, kad vartotojas gali įvesti neteisingus duomenis (pvz., įvedus ne skaičių metams arba ne egzistuojantį knygos numerį ištrinimui).
# Naudotojo sąveika: Užtikrinkite, kad vartotojas gautų aiškius nurodymus kiekviename žingsnyje. Po kiekvieno atlikto veiksmo grąžinkite vartotoją atgal į pagrindinį meniu, kol nebus pasirinkta išeiti iš programos.
 
# Užduoties vertinimo kriterijai
# Teisingas funkcijų naudojimas: Ar kiekviena funkcija atlieka tik vieną konkretų veiksmą?
# Ciklų ir sąlyginių sakinių panaudojimas: Ar programos struktūra leidžia pakartotinus veiksmus (pvz., grįžimas į meniu) ir tinkamai tvarko skirtingas sąlygas (pvz., neteisingi įvesties duomenys)?
# Klaidų tvarkymas: Ar programa tinkamai apdoroja įvesties klaidas ir praneša apie jas vartotojui?
# Naudotojo sąsaja: Ar programa yra suprantama ir lengvai naudojama?

def knygos_pridejimas (nauja_knyga):
    
        pavadinimas = input("Iveskite knygos pavadinima: ")
        autorius = input("Iveskite knygos autoriu: ")
        yra_klaida = True
        while yra_klaida:
            try:
                metai = int(input("Iveskite knygos isleidimo metus: "))
                yra_klaida = False
            except ValueError:
                print("Metai ivedami skaiciais. Ivedete ne skaicius")
                
        zanras = input("Iveskite knygos zanra: ")
        nauja_knyga = {"Pavadinimas":pavadinimas, "Autorius":autorius, "Metai":metai, "Zanras":zanras}
        knygu_sarasas.append(nauja_knyga)

        return nauja_knyga

def knygos_atvaizdavimas (visos_knygos):

    numeriai = 1
    for knyga in visos_knygos:
       knyga["numeris"] = numeriai
       numeriai += 1

    atnaujintos_visos_knygos = "Sunumeruotas knygu sarasas:\n"

    for knyga in visos_knygos:
        atnaujintos_visos_knygos += f"{knyga["numeris"]}.{knyga["Pavadinimas"]}-{knyga["Autorius"]},{knyga["Metai"]},{knyga["Zanras"]}.\n"

    return atnaujintos_visos_knygos
    
def knygos_paieska (ieskoma_knyga,visos_knygos):

    rastos_knygos = []
    for indeksas_zodyno in range(len(visos_knygos)-1,-1,-1):
        if ieskoma_knyga in visos_knygos[indeksas_zodyno]["Pavadinimas"] or ieskoma_knyga in visos_knygos[indeksas_zodyno]["Autorius"]:

                # print(f"{knyga["Pavadinimas"]}-{knyga["Autorius"]},{knyga["Metai"]},{knyga["Zanras"]}.")
            rastos_knygos.append(visos_knygos[indeksas_zodyno])
    if rastos_knygos == []:
        print("Tokios knygos nera")

    else:
        isrinktos_knygos = "Pagal jusu uzklausa rastos knygos:\n"

        for knyga in rastos_knygos:
            isrinktos_knygos += f"{knyga["numeris"]}.{knyga["Pavadinimas"]}-{knyga["Autorius"]},{knyga["Metai"]},{knyga["Zanras"]}.\n"

        print(isrinktos_knygos)

def knygos_istrynimas (trinama_knyga,visos_knygos):

    for indeksas in range(len(visos_knygos)-1,-1,-1):
        if trinama_knyga in visos_knygos[indeksas]["Pavadinimas"]:
            #trinama_knyga in visos_knygos [indeksas]["numeris"] or 
            del visos_knygos[indeksas]
            print("Knyga istrinta")
        else:
            print("Istrinti negalima. Tokios knygos nera")
        
            
knygu_sarasas = [{"Pavadinimas":"One Hundred Years of Solitude", "Autorius":"Gabriel García Márquez", "Metai":"1967", "Zanras":"magical realism"},{"Pavadinimas":"The Great Gatsby", "Autorius":"George Orwell", "Metai":"1997", "Zanras":"fantasy"}]


while True:

    pasirinkta_programa = int(input("""\nPasirinkite norima operacija ivesdami jos numeri:
                                1. Prideti nauja knyga
                                2. Atvaizduoti visu knygu sarasa
                                3. Ieskoti knygos
                                4. Istrinti knyga
                                5. Iseiti is programos
                                ^ """ ))
    if pasirinkta_programa ==1:

        ivedama_knyga = {}
        print(knygos_pridejimas(ivedama_knyga))

    elif pasirinkta_programa ==2:

        print(knygos_atvaizdavimas(knygu_sarasas))

    elif pasirinkta_programa ==3:

        paieska = input("Iveskite ieskoma termina: knygos pavadinima arba autoriu. ")
        
        knygos_paieska(paieska,knygu_sarasas)
            

    elif pasirinkta_programa ==4:

        istrynimas = input("Iveskite istrinamos knygos pavadinima arba numeri: ")
        knygos_istrynimas(istrynimas,knygu_sarasas)

    elif pasirinkta_programa ==5:
        print("Programa baigta")
        exit()


            
       
            
         
        
       












# # 1 prideti knyga

# def pridejimas (pavadinimas,autorius,metai):

#     nauja_knyga = {"pavadinimas":pavadinimas,"autorius":autorius, "metai":metai }
    
#     return nauja_knyga
     
# def atvaizdavimas (turinio):
#     numeris = 0
#     for leidinys in turinio:
#         numeris +=1
#         knygu_sarasas = leidinys.update({"numeris":numeris})
       
#     print(f"{leidinys["numeris"]}. {leidinys["pavadinimas"]}. {leidinys["autorius"]}. {leidinys["metai"]}.")
#     return knygu_sarasas



# def paieska (raktinis_zodis):

#     rastos_knygos = []
#     for knyga in knygu_sarasas:
            
#         if raktinis_zodis in knyga["pavadinimas"] or raktinis_zodis in knyga["autorius"]:
#             rastos_knygos.append(knyga["pavadinimas"])
                
#     if rastos_knygos:
#         print(f"pagal jusu uzklausa rasta knyga: {rastos_knygos}\n")
#     else:
#         print("Tokios knygos nera")


# def istrynimas (irasas):
#     try:
#         for knyga in knygu_sarasas:

#             if irasas in knyga["pavadinimas"] or str(knyga["numeris"]):
#                 del(knygu_sarasas[knyga])
#                 print(knygu_sarasas)
#                 return knygu_sarasas
            
#             else:
#                  raise ValueError ("Tokios knygos nera, todel jos istrinti negalima ")
#     except ValueError as kny:
#         print(kny)
    
        

                     

            
        


# # knygu_sarasas = {"pavadinimas":"Vandens pažadas","autorius":"Abraham Verghese","metai": 2015,"pavadinimas":"Adelinos vaiduokliai","autorius":"H. D. Carlton","metai": 2000,"pavadinimas":"Trečias kartas nemeluoja","autorius":"Irena Buivydaitė","metai": 2021}

# knygu_sarasas = [{"pavadinimas":"Vandens pažadas","autorius":"Abraham Verghese","metai": 2015},{"pavadinimas":"Vandens pažadas2","autorius":"Abraham Verghese","metai": 2015},{"pavadinimas":"Adelinos vaiduokliai","autorius":"H. D. Carlton","metai": 2000},{"pavadinimas":"Trečias kartas nemeluoja","autorius":"Irena Buivydaitė","metai": 2021}]

# while True:
#         try:
#             norima_operacija = input("Pasirinkite norima operacija, ivesdami operacijos numeri:\n 1. Pridėti naują knygą.\n 2. Atvaizduoti visų knygų sąrašą.\n 3. Ieškoti knygos.\n 4. Ištrinti knygą.\n 5. Išeiti iš programos.\n Pageidaujamos programos numeris: ")
#             print(norima_operacija)

#             if norima_operacija == "1":
#                 print("pirma oper")

#                 pavadinimas1 = input("Iveskite knygos pavadinima: ")
#                 autorius1 = input("Iveskite knygos autoriu: ")
#                 metai1 = (input("Iveskite knygos isleidimo metus: "))

#                 try:
#                     if metai1.isdigit():
#                         pridejimas(pavadinimas1,autorius1,metai1)
#                         knygu_sarasas=knygu_sarasas.append(pridejimas(pavadinimas1,autorius1,metai1))
#                         print(f"prideta knyga: {pridejimas(pavadinimas1,autorius1,metai1)}")
#                     else:
#                         raise ValueError("Neteisingai ivesti metai!Bandykite ivesti is naujo.")
                    
#                 except ValueError as rx:
#                     print(rx)

#             elif norima_operacija == "2":
#                 print("antra oper")

#                 atvaizdavimas(knygu_sarasas)
                
#             elif norima_operacija == "3":
#                 print("trecia oper")
#                 ieskoma_fraze = input("Iveskite ieskomos knygos pavadinima arba autoriu: ")
#                 paieska(ieskoma_fraze)

#             elif norima_operacija == "4":
#                 print("Ketvirta oper")
#                 istrinama_knyga = input("Iveskite pavadinima knygos, kuria norite istrinti: ")
#                 istrynimas(istrinama_knyga)

#             elif norima_operacija == "5":
#                 print("Programa baigta")
#                 exit()
                

#             else:
#                 raise ValueError ("Tokio pasirinkimo nera")
#         except ValueError as ex:
#              print(ex)



    

        