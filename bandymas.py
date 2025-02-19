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

# # produktai = ["obuolys", "bananas", "arbuzas", "kriause", "citrina", "vyšnia"]

# # indeksas = input("Iveskite indeksa ")

# # try: 
# #     if indeksas.isdigit:
# #         indeksas = int(indeksas)
# #         print(indeksas)       
# #     else:
# #         raise ValueError ("Ivedete ne sveikaji skaiciu ")

# # except ValueError as ex:
# #     print(ex)

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

# PRIDET SARASO ZODYNUOSE!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def auto_ivedimas (auto_biblioteka):
    
#     pavadinimas = input("ivesk pavadinima")
#     spalva = input("ivesk spalva")
#     metai = input("isvesk metus")

#     naujas_auto = {"pavadinimas":pavadinimas, "spalva":spalva, "metai":metai}
#     auto_biblioteka.append(naujas_auto)

#     numeris = 1
#     for auto in range(len(auto_biblioteka)):
#         auto_biblioteka[auto]["numeris"] = numeris
#         # arba tas pats sukuria zodyne nauja reiksme
#         # auto_biblioteka["numeris"] = numeris
#         numeris += 1


#     atnaujinto_saraso_tekstas = "atnaujintas sarasas:\n"

#     for auto in auto_biblioteka:
#         atnaujinto_saraso_tekstas += f"Pavadinimas{auto['pavadinimas']}. Spalva: {auto['spalva']}. Metai:{auto['metai']}"
#         # arba jei nori ne teksto tik numeri pridet
#         # atnaujinto_saraso_tekstas += f"{numeris} - {auto['pavadinimas']}.{auto['spalva']}.{auto['metai']}"
#     return atnaujinto_saraso_tekstas



# auto_sarasas = []
# print(auto_ivedimas(auto_sarasas))


# ISTRINT SARASO ZODYNUOSE!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def auto_istrynimas (auto_biblioteka,istrinamas_auto):
    
#     pavadinimas = "audi"
#     spalva = "zalia"
#     metai = "1999"

#     naujas_auto = {"pavadinimas":pavadinimas, "spalva":spalva, "metai":metai}
#     auto_biblioteka.append(naujas_auto)

#     # for auto in auto_biblioteka:
#     #     if istrinamas_auto == auto["pavadinimas"]: #jei tikslus pavadinimas ne dalinis
#     #         auto_biblioteka.remove(auto)

#     #     #jeigu tik dalinis pavadinimas tam kad nepraleistu eilutes kuri pasislenka istrynus einam nuo galo. -1 pradedam nuo galo -1 einam iki
#     #     # pradzios -1 einam atgal per viena zingsni

#     for i in range(len(auto_biblioteka)-1,-1,-1):#jau eina per indeksus
#         if istrinamas_auto in auto_biblioteka[i]["pavadinimas"]: #jei dalinis pavadinimas in
#             del auto_biblioteka [i]

    
#     print(auto_biblioteka)


# istrinama_reiksme = "au"
# auto_sarasas = []
# print(auto_istrynimas(auto_sarasas,istrinama_reiksme))

# print(auto_sarasas)

# def atvaizdavimas (auto_sarasas):
    
#     numeriai = 1
#     for auto in auto_sarasas:
#         auto["Numeriai"] = numeriai
#         numeriai +=1

#     sunumeruotas = "sunumeruotas sarasas\n"

#     for auto in auto_sarasas:
#         sunumeruotas += f"{auto["Numeriai"]}. pav {auto["pavadinimas"]}, sp {auto["spalva"]}\n"

#     return sunumeruotas



auto_biblioteka = [
    {"pavadinimas": "Audi", "spalva": "raudona", "metai": "2005"},
    {"pavadinimas": "BMW", "spalva": "mėlyna", "metai": "2010"},
    {"pavadinimas": "Mercedes", "spalva": "juoda", "metai": "2018"},
    {"pavadinimas": "Volkswagen", "spalva": "balta", "metai": "2015"},
    {"pavadinimas": "Toyota", "spalva": "žalia", "metai": "2020"}
]

print(atvaizdavimas(auto_biblioteka))

