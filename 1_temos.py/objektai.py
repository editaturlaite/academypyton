# class House: # klase
#     def __init__(self): # metodas - (jeigu metodas turi aplink save __ __ vadinasi jis vadinamas (dunder/magic metodu))
#         pass

# class House: # klase
#     def __init__(self): # metodas - (jeigu metodas turi aplink save __ __ vadinasi jis vadinamas (dunder/magic metodu))
#         pass

# class House:
#     def __init__(self,color, heigth, width, window_amount): # metodas yra tiesiog funkcija priklausanti klasei
#         self.color = color # savybe - property
#         self.heigth = heigth
#         self.width = width
#         self.window_amount = window_amount
 
# varguolio_namas = House("Red",400,800,6) # mes sukuriame (inicializuojame ) objekta
# pasiturincio_namas = House("Green",600,20000,20) # mes sukuriame (inicializuojame )
 
# print(varguolio_namas.color) # gauname viena is objekto reiksmiu
# print(pasiturincio_namas.color)
 
# varguolio_namas.window_amount = 8 # pakeiciame viena is objekto reiksmiu
# print(varguolio_namas.window_amount) # atspausdiname pakeista objekto reiksme
# turi kontekstinį meniu

# class Dog:
#     def __init__(self, spalva, vardas): # numatytoji reiksme jeigu nieko nenurodome
#         self.color = spalva
#         self.name = vardas
#         self.legs = 4
#     def loti(self):
#         print(f"{self.name} loja - AU AU")
 
#     def __str__(self): # str - specialus metodas, kuris iskvieciamas print metu - skirtas atvaizduoti objekta
#         return f"Šuniukas {self.name} yra {self.color} spalvos"
   
 
# Reksas = Dog("Brown", "Reksas")
 
# Sargis = Dog("Black", "Sargis")
 
# # sarasas = [Reksas,Sargis]
 
# dogs = []
# dogs.append(Reksas)
# dogs.append(Sargis)
 
# for dog in dogs:
#     print(dog)
#     dog.loti()




# class Staciakampis:
#     def __init__(self,aukstis,plotis):
#         self.aukstis = aukstis
#         self.plotis = plotis
#     def perimetras(self):
#         ats = (2*self.aukstis) + 2*(self.plotis)
#         return ats
        
# # imput  

# mazas = Staciakampis(5,2) #vietoj skaiciu imputai

# print(mazas.perimetras())

# 1 UZDUOTIS
# Parašyti klasę Sakinys, kuri turi savybę tekstas irmetodus,kurie:
# •Gražina tekstą atbulai
# •Gražina tekstą mažosiomis raidėmis
# •Gražina tekstą didžiosiomis raidėmis
# •Gražina žodį pagal nurodytą eilės numerį
# •Gražina, kiek teksteyranurodytų simbolių arba žodžių
# •Gražinatekstą su pakeistu nurodytu žodžiu arba simboliu
# •Atspausdina, kiek sakinyje yra žodžių,skaičių,didžiųjų ir mažųjų raidžių
# Susikurti kelis klasės objektus ir išbandyti visus metodus

# class Sakinys:
#     def __init__(self, tekstas):
#         self.eilerastis = tekstas

#     def atbulai(self):
#         apsuktas = self.eilerastis.split()[::-1]
#         return " ".join(apsuktas)
    
#     def mazosiomis(self):
#         return self.eilerastis.lower()
    
#     def didziosiomis(self):
#         return self.eilerastis.upper()

#     def eil_nr(self,indeksas):
#         return self.eilerastis.split()[indeksas]
    
#     def teksto_simboliu_suma(self):
#         return len("".join(self.eilerastis))
    
#     def pakeistas_tekstas(self,keiciamas):
#         return self.eilerastis.replace("buvo",keiciamas)
    
#     def daliu_skaiciavimas(self):
#         zodziu_kiekis = len(self.eilerastis.split())
#         skaiciu_kiekis =0
#         didziuju_kiekis =0
#         mazuju_kiekis =0
        
#         for raide in "".join(self.eilerastis):
#             if raide.isupper():
#                 didziuju_kiekis +=1
#             if raide.islower():
#                 mazuju_kiekis +=1
#             if raide.isdigit():
#                 skaiciu_kiekis +=1
#         return f"Tekste yra {zodziu_kiekis} zodziai, {skaiciu_kiekis} skaiciu, {didziuju_kiekis} didziosios raides, {mazuju_kiekis} mazosios raides."

    # def __str__(self):
    #     return self.eilerastis


# # ivestis = input("Iveskite eilerasti")
# ivestis = "Mano batai buvo du"

# mano_batai =Sakinys(ivestis)

# print(mano_batai.atbulai())

# print(mano_batai.mazosiomis())

# print(mano_batai.didziosiomis())

# pasirinktas_indeksas = int(input("Iveskite norimo zodzio eiles numeri skaiciumi "))

# print(mano_batai.eil_nr(pasirinktas_indeksas - 1)) 

# print(mano_batai.teksto_simboliu_suma())

# ivestis_keiciamas_zodis = input("Iveskite zodi kuri norite pakeisti")
# ivestis_pakeistas_zodis = input("Iveskite zodi kuriuo norite pakeisti")
# keiciamas_zodis = "buvo"
# pakeistas_zodis = "yra"

# print(mano_batai.pakeistas_tekstas(keiciamas_zodis))

# print(mano_batai.daliu_skaiciavimas())

# 4 UZD

# print(mano_batai)

# ---------------------------------------------------------

# ivestis2 = input("Iveskite misle")
# ivestis2 = "buvo Zalia zole bet Ne zole. 123"

# misle = Sakinys(ivestis2)

# print(misle.atbulai())

# print(misle.mazosiomis())

# print(misle.didziosiomis())

# grazinamas_antras_zodis = 1
# print(misle.eil_nr(grazinamas_antras_zodis)) 

# print(misle.teksto_simboliu_suma())

# keiciamas_zodis2 = "zole"
# pakeistas_zodis2 = "varle"

# print(misle.pakeistas_tekstas(keiciamas_zodis))

# print(misle.daliu_skaiciavimas())

# ----------------------------------------------------

# print(mano_batai.atbulai(),misle.atbulai())

# print(mano_batai.mazosiomis(),misle.mazosiomis())

# print(mano_batai.didziosiomis(),misle.didziosiomis())

# print(mano_batai.eil_nr(),misle.eil_nr())

# print(mano_batai.teksto_simboliu_suma(),misle.teksto_simboliu_suma())

# keiciamas_zodis = "yra"

# print(mano_batai.pakeistas_tekstas(keiciamas_zodis),misle.pakeistas_tekstas(keiciamas_zodis2))

# print(mano_batai.daliu_skaiciavimas(),misle.daliu_skaiciavimas())



# 2.UZDUOTIS
# Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) irmetodus,kurie:
# •Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
# •Gražina,ar nurodytos sukakties metai buvo keliamieji
# •Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
# •Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą

# import datetime
# from datetime import timedelta

# class Sukaktis:
#     def __init__(self,pilna_sukakties_data,metai):
#         self.sukakties_data = pilna_sukakties_data
#         self.metai = metai
    
#     def nuo_iki(self):
#         dabartine_data = datetime.datetime.now()
#         praejo_metu = dabartine_data.year - self.sukakties_data.year
#         praejo_menesiu = (dabartine_data.year - self.sukakties_data.year)*12 + (dabartine_data.month - self.sukakties_data.month)
#         praejo_sekundziu = (dabartine_data - self.sukakties_data).total_seconds()
#         praejo_minuciu = praejo_sekundziu/60
#         praejo_valandu = praejo_minuciu/60
#         praejo_dienu = (dabartine_data - self.sukakties_data).days
#         praejo_savaiciu = praejo_dienu/7

#         return f"""Nuo jusu sukakties praejo:
#         {praejo_metu} metu.
#         {praejo_menesiu} menesiu.
#         {round(praejo_savaiciu)} savaiciu.
#         {praejo_dienu} dienu.
#         {round(praejo_valandu)} valandu.
#         {round(praejo_minuciu)} minuciu.
#         {round(praejo_sekundziu)} sekundziu."""
    
#     def ar_keliamieji_metai(self):
#         if self.metai % 400 == 0 or self.metai % 4 == 0:
#             return "Tai keliamieji metai"

#         elif self.metai % 100 == 0:
#             return "Tai ne keliamieji metai"

#         else:
#             return "Tai ne keliamieji metai"
        
#     def dienu_pridejimas(self,dienos):
#         nauja_data_pridejus = self.sukakties_data + timedelta(days=dienos)
#         return f"Pridejus jusu norima dienu skaiciu, nauja data yra: \n {nauja_data_pridejus}"
    
#     def dienu_atemimas(self,dienos):
#         nauja_data_atemus = self.sukakties_data - timedelta(days=dienos)
#         return f"Atemus jusu norima dienu skaiciu, nauja data yra: \n {nauja_data_atemus}"

#     def __str__(self):
#         return self.sukakties_data.strftime("%Y-%m-%d %H:%M")



# sukakties_metai = int(input("Iveskite sukakties metus "))
# sukakties_menesis = int(input("Iveskite sukakties menesi skaiciumi: pvz jei kovas - '3' "))
# sukakties_diena = int(input("Iveskite sukakties diena skaiciumi "))

# ivesta_sukaktis = datetime.datetime(sukakties_metai,sukakties_menesis,sukakties_diena)

# metines = Sukaktis(ivesta_sukaktis,sukakties_metai)

# print(metines.nuo_iki())

# print(metines.ar_keliamieji_metai())

# pridedamos_dienos = int(input("Iveskite kiek dienu norite prideti prie savo datos "))

# print(metines.dienu_pridejimas(pridedamos_dienos))

# atimamos_dienos = int(input("Iveskite kiek dienu norite atimti is savo datos "))

# print(metines.dienu_atemimas(atimamos_dienos))

# 4 UZD

# print(metines)


# 3.1 UZDUOTIS
# Perdaryti:
# •1 užduotį taip, kad jei kuriant objektą, nepaduodamas joks tekstas,veiksmai turi būti atliekami su „default“ tekstu

# kai_nera_teksto = "Jei nebus teksto tai buvo gerai ir sitas"

# class Sakinys:
#     def __init__(self, tekstas=kai_nera_teksto):
#         self.eilerastis = tekstas

#     def atbulai(self):
#         apsuktas = self.eilerastis.split()[::-1]
#         return " ".join(apsuktas)
    
#     def mazosiomis(self):
#         return self.eilerastis.lower()
    
#     def didziosiomis(self):
#         return self.eilerastis.upper()
    
#     def eil_nr(self,indeksas=1):
#         return self.eilerastis.split()[indeksas]
    
#     def teksto_simboliu_suma(self):
#         return len("".join(self.eilerastis))
    
#     def pakeistas_tekstas(self,keiciamas,naujas):
#         return self.eilerastis.replace(keiciamas,naujas)
    
#     def daliu_skaiciavimas(self):
#         zodziu_kiekis = len(self.eilerastis.split())
#         skaiciu_kiekis =0
#         didziuju_kiekis =0
#         mazuju_kiekis =0
        
#         for raide in "".join(self.eilerastis):
#             if raide.isupper():
#                 didziuju_kiekis +=1
#             if raide.islower():
#                 mazuju_kiekis +=1
#             if raide.isdigit():
#                 skaiciu_kiekis +=1
#         return f"Tekste yra {zodziu_kiekis} zodziai, {skaiciu_kiekis} skaiciu, {didziuju_kiekis} didziosios raides, {mazuju_kiekis} mazosios raides."


# mano_batai =Sakinys()

# print(mano_batai.atbulai())

# print(mano_batai.mazosiomis())

# print(mano_batai.didziosiomis())

# print(mano_batai.eil_nr())

# print(mano_batai.teksto_simboliu_suma())

# # ivestis_keiciamas_zodis = input("Iveskite zodi kuri norite pakeisti")
# # ivestis_pakeistas_zodis = input("Iveskite zodi kuriuo norite pakeisti")
# keiciamas_zodis = "buvo"
# pakeistas_zodis = "yra"

# print(mano_batai.pakeistas_tekstas(keiciamas_zodis,pakeistas_zodis))

# print(mano_batai.daliu_skaiciavimas())


# 3.1 UZDUOTIS
# Perdaryti:
# 2 užduotį taip, kad jei kuriant objektą, nepaduodamas jokia data,veiksmai turi būti atliekami su programuotojo gimtadieniu

# import datetime
# from datetime import timedelta

# programuotojo_gimtadienis = (datetime.datetime(1989,3,26))

# class Sukaktis:
#     def __init__(self,metai,pilna_sukakties_data = programuotojo_gimtadienis):
#         self.sukakties_data = pilna_sukakties_data
#         self.metai = metai
    
#     def nuo_iki(self):
#         dabartine_data = datetime.datetime.now()
#         praejo_metu = dabartine_data.year - self.sukakties_data.year
#         praejo_menesiu = (dabartine_data.year - self.sukakties_data.year)*12 + (dabartine_data.month - self.sukakties_data.month)
#         praejo_sekundziu = (dabartine_data - self.sukakties_data).total_seconds()
#         praejo_minuciu = praejo_sekundziu/60
#         praejo_valandu = praejo_minuciu/60
#         praejo_dienu = (dabartine_data - self.sukakties_data).days
#         praejo_savaiciu = praejo_dienu/7

#         return f"""Nuo jusu sukakties praejo:
#         {praejo_metu} metu.
#         {praejo_menesiu} menesiu.
#         {round(praejo_savaiciu)} savaiciu.
#         {praejo_dienu} dienu.
#         {round(praejo_valandu)} valandu.
#         {round(praejo_minuciu)} minuciu.
#         {round(praejo_sekundziu)} sekundziu."""
    
#     def ar_keliamieji_metai(self):
#         if self.metai % 400 == 0 or self.metai % 4 == 0:
#             return "Tai keliamieji metai"

#         elif self.metai % 100 == 0:
#             return "Tai ne keliamieji metai"

#         else:
#             return "Tai ne keliamieji metai"
        
#     def dienu_pridejimas(self,dienos):
#         nauja_data_pridejus = self.sukakties_data + timedelta(days=dienos)
#         return f"Pridejus jusu norima dienu skaiciu, nauja data yra: \n {nauja_data_pridejus}"
    
#     def dienu_atemimas(self,dienos):
#         nauja_data_atemus = self.sukakties_data - timedelta(days=dienos)
#         return f"Atemus jusu norima dienu skaiciu, nauja data yra: \n {nauja_data_atemus}"



# sukakties_metai = int(input("Iveskite sukakties metus "))

# metines = Sukaktis(sukakties_metai)

# print(metines.nuo_iki())

# print(metines.ar_keliamieji_metai())

# pridedamos_dienos = int(input("Iveskite kiek dienu norite prideti prie savo datos "))

# print(metines.dienu_pridejimas(pridedamos_dienos))

# atimamos_dienos = int(input("Iveskite kiek dienu norite atimti is savo datos "))

# print(metines.dienu_atemimas(atimamos_dienos))


# 4. UZDUOTIS
# PRIDETA PRIE PIRMOS IR ANTROS

# 5. UZDUOTIS
# Padarytiminibiudžetoprogramą, kuri:
# •Leistų vartotojui įvesti pajamas
# •Leistų vartotojui įvesti išlaidas
# •Leistų vartotojui parodyti pajamų/išlaidų balansą
# •Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
# •Leistų vartotojui išeiti iš programos
 
# Rekomendacija, kaip galima būtų padaryti:
# •Programa turi turėti klasę Irasas, kuri turėtų argumentus tipas (Pajamos arba Išlaidos) ir suma. Galima prirašyti str metodą, 
# kuris gražintų, kaip bus atvaizduojamas spausdinamas objektas.
# •Programa turi turėti klasę Biudzetas, kurioje būtų:
# •Metodas init, kuriame sukurtas tuščias sąrašas zurnalas, į kurį bus dedami sukurti pajamų ir išlaidų objektai
# •Metodasprideti_pajamu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų pajamų objektą ir įdėtų jį į biudžeto žurnalą
# •Metodasprideti_islaidu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų išlaidų objektą ir įdėtų jį į biudžeto žurnalą
# •Metodasgauti_balansą(self), kuris gražintų žurnale laikomų pajamų ir išlaidų balansą.
# •Metodasparodyti_ataskaita(self), kuris atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).

# import pickle
    
# class Irasas:

#     def __init__(self,suma):
#         self.ivesta_suma = suma

#         if self.ivesta_suma>=0:
#             self.ivestas_tipas = "Pajamos"
#         else:
#             self.ivestas_tipas = "Islaidos"

#     def __str__(self):
#         return f"{self.ivestas_tipas} - {self.ivesta_suma}"

# class Biudzetas:

#     def __init__(self):
#         self.zurnalas = []

#     def prideti_pajamu_irasa(self,suma):
#         irasas = Irasas(suma)
#         self.zurnalas.append(irasas)
    
#     def prideti_islaidu_irasa(self,suma):
#         irasas =Irasas(suma)
#         self.zurnalas.append(irasas)
        
#     def skaiciuoti_balansa(self):
#         pajamos = 0
#         islaidos = 0
#         for irasas in self.zurnalas:
#             if irasas.ivestas_tipas == "Pajamos":
#                 pajamos += irasas.ivesta_suma
#             elif irasas.ivestas_tipas == "Islaidos":
#                 islaidos += abs(irasas.ivesta_suma)
#         return pajamos-islaidos
    
#     def rodyti_ataskaita(self):
#         ataskaita = "Jusu balanso ataskaita:\n"
#         for irasas in self.zurnalas:
#             ataskaita += f"{irasas.ivestas_tipas}: {irasas.ivesta_suma}\n"
#         return ataskaita

# biudzetas = Biudzetas()

# try:
#     with open("pajamos_islaidos.pickle","rb")as failas:
#         biudzetas.zurnalas = pickle.load(failas)
# except (EOFError,FileNotFoundError):
#     print("Nera duomenu pradeta nuo naujo")
    
# while True:
#     try:
#         norima_operacija = int(input("""Pasirinkite norima operacija ir iveskite jos numeri:
#                                 1. Ivesti pajamas arba islaidas. Islaidas veskite su '-' zenklu :
#                                 2. perziureti balansa.
#                                 3. Perziureti biudzeto ataskaita.
#                                 4. iseiti is programos. 
#                                      : """))
#         if norima_operacija<1 or norima_operacija>4:
#             print("Pasirinkote neegzistuojanti operacijos numeri.Veskite dar karta.")

#         if norima_operacija == 1:

#             ivedamos_pajamos_islaidos=int(input("Iveskite pajamas arba islaidas. Islaidas veskite su '-' zenklu : "))
#             irasas = Irasas(ivedamos_pajamos_islaidos)
#             print(irasas)

#             if ivedamos_pajamos_islaidos>=0:
#                 biudzetas.prideti_pajamu_irasa(ivedamos_pajamos_islaidos)
#             else:
#                 biudzetas.prideti_islaidu_irasa(ivedamos_pajamos_islaidos)

#         elif norima_operacija == 2:
#             print(f"Jusu balansas yra: {biudzetas.skaiciuoti_balansa()}")

#         elif norima_operacija == 3:
#             print(biudzetas.rodyti_ataskaita())

#         elif norima_operacija == 4:
#             break
#     except ValueError:
#         print("Ivedete ne skaiciu. Pasirinkite norima operacija ir bandykite dar karta")

# print("Programa baigta")

# with open("pajamos_islaidos.pickle","wb")as failas:
#     pickle.dump(biudzetas.zurnalas,failas)
    
# exit()

# VILIAUS KODAS-------------------------------------------------------------------------

# import pickle
 
 
# class Entry:
#     def __init__(self, type, sum):
#         self.type = type
#         self.sum = sum
 
#     def __str__(self):
#         return f"{self.type}: {self.sum}"
 
 
# class Budget:
#     def __init__(self):
#         self.journal = []
 
#     def add_income_entry(self, sum):
#         entry = Entry("pajamos", sum)
#         self.journal.append(entry)
 
#     def add_expense_entry(self, sum):
#         entry = Entry("išlaidos", sum)
#         self.journal.append(entry)
 
#     def get_balance(self):
#         total_income = sum(entry.sum for entry in self.journal if entry.type == "pajamos")
#         total_expenses = sum(entry.sum for entry in self.journal if entry.type == "išlaidos")
#         balance = total_income + total_expenses
#         return balance
 
#     def show_report(self):
#         for entry in self.journal:
#             print(entry)
 
 
# def load_file():
#     try:
#         with open("budget.pickle", "rb") as file:
#             budget = pickle.load(file)
#         return budget
#     except FileNotFoundError:
#         return Budget()
 
 
# def save_file(budget):
#     with open("budget.pickle", "wb") as file:
#         pickle.dump(budget, file)
 
# def main_menu(budget):
#     while True:
#         print("\nPgrindinis meniu:")
#         print("1. Pridėti pajamas / išlaidas")
#         print("2. Rodyti balansą")
#         print("3. Rodyti ataskaitą")
#         print("Q. Baigti")
 
#         choice = input("Pasirinkite veiksmą iš meniu (1-3) 'Q' - Baigti:\n ")
 
#         if choice == "1":
#             add = True
#             while add:    
#                 try:
#                     amount = float(input("Įveskite pajamas / išlaidas(-): "))
#                     if amount > 0:
#                         budget.add_income_entry(amount)
 
#                         print("Pajamos pridėtos")
#                     elif amount < 0:
#                         budget.add_expense_entry(amount)
                       
#                         print ("Išlaidos pridėtos")
#                     elif amount == 0:
#                         print("Pajamos / išlaidos negali būti 0")        
#                 except ValueError:
#                     print("Netinkama įvestis, įveskite skaičių.")
#                 while True:
#                     ask = input("Ar norite tęsti? Taip/Ne ")
#                     if ask.capitalize() == "Taip":
#                         add = True
#                         break
#                     elif ask.capitalize() == "Ne":
#                         add = False  
#                         break
#                     else:
#                         continue
 
#         elif choice == "2":
#             print("Balansas:", budget.get_balance())
 
#         elif choice == "3":
#             print("\n Biudžeto ataskaita:")
#             budget.show_report()
 
#         elif choice.upper() == "Q":
#             print("Duomenys išsaugoti")
#             save_file(budget)
#             break
 
#         else:
#             print("Neteisingas meniu pasirinkimas, bandykite dar kartą.")
 
 
# budget = load_file()
# print("Mini biudžetas v2!")
# main_menu(budget)
# print("Viso gero!")

# VILIAUS KODAS ----------------------------------------------------

# 6. UZDUOTIS
# Klasė „BankoSąskaita“: Sukurkite klasę BankoSąskaita, kuri turi savybes savininkas, balansas. 
# Pridėkite metodus įnešti_pinigų, išimti_pinigų ir gauti_balansą. Sukurkite objektą ir išbandykite visus metodus.

# class Banko_sask:
#     def __init__(self,vartotojas):
#         self.savininkas = vartotojas
#         self.balansas = 0

#     def inesti_pinigu(self,suma):
#         self.balansas += suma

#     def isimti_pinigu(self,suma):
#         self.balansas -= suma

#     def rodyti_balansa(self):
#         return f"Jusu balansas yra: {self.balansas}"
    
        
#  balansas_uz = Banko_sask("edita")

# try:
#     with open("bankomatas.pickle", "rb") as failas:
#         balansas_uz.balansas = pickle.load(failas)
# except (EOFError,FileNotFoundError)


# vartotojo_duomenys = ("Iveskite vartotojo duomenis: 'Vardas Pavarde: ")

# bankomatas = Banko_sask(vartotojo_duomenys)

# inesti_suma = int(input("Iveskite norima inesti pinigu suma: "))
# bankomatas.inesti_pinigu(inesti_suma)

# isimti_suma = int(input("Iveskite norima issimti pinigu suma: "))
# bankomatas.isimti_pinigu(isimti_suma)

# print(bankomatas.rodyti_balansa())


