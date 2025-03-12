# class transporto_priemone:
#     def __init__(self, greitis):
#         self.speed = greitis
 
# class sausumos_transporto_priemone(transporto_priemone):
#     def __init__(self, greitis, ratu_kiekis):
#         super().__init__()
#         self.wheel_amount = ratu_kiekis

# class transporto_priemone:
#     def __init__(self, greitis):
#         self.speed = greitis
#     def vaziuoti(self):
#         print("As judu")
 
 
# class sausumos_transporto_priemone(transporto_priemone): # nurodome ka paveldes tarp skliausteliu
#     def __init__(self, greitis, ratu_kiekis):
#         super().__init__(greitis) # sitoje eilute mes kreipiames i tevo init super() - tevas
#         self.wheel_amount = ratu_kiekis
 
#     def vaziuoti(self):
#         super().vaziuoti()
#         print("As vaziuoju zeme")
#     def __str__(self):
#         return f"{self.wheel_amount}, {self.speed}"
   
# class oro_transporto_priemone(transporto_priemone): # nurodome ka paveldes tarp skliausteliu
#     def __init__(self, greitis, sparnu_kiekis):
#         super().__init__(greitis) # sitoje eilute mes kreipiames i tevo init super() - tevas
#         self.wing_amount = sparnu_kiekis
 
#     def vaziuoti(self):
#         super().vaziuoti()
#         print("As skrendu")
#     def __str__(self):
#         return f"{self.wing_amount}, {self.speed}"
   
# class vandens_transporto_priemone(transporto_priemone): # nurodome ka paveldes tarp skliausteliu
#     def __init__(self, greitis):
#         super().__init__(greitis) # sitoje eilute mes kreipiames i tevo init super() - tevas
 
#     def __str__(self):
#         return f"{self.speed}"
   
# class dviratis(sausumos_transporto_priemone) # gali buti ir anukas
 
 
# automobilis = sausumos_transporto_priemone(200,4)
# automobilis.vaziuoti()
# print(automobilis)
 
# lektuvas = oro_transporto_priemone(700,2)
# print(lektuvas)
# lektuvas.vaziuoti()
 
# laivas = vandens_transporto_priemone(30)
 
# laivas.vaziuoti()

# --------------------------------------

# UZDUOTIS
# Sukurkite tris klases Žmogus ir dvi paveldinčias klases Darbuotojas ir Klientas.
#  Žmogus turės vardą pavardę, o Darbuotojas pareigas ir įsidarbinimo datą. O klientas pirkimų kiekį ir paskutinio užsakymo datą.

# Sukurti dvi funkcijas, kurios priims Klientui arba Darbuotojui reikalingas sąvybes -
#  kaip argumentus ir sukurs šiuos objektus, sukūrus grąžins šiuos objektus

# Sukurti po Metodą klientui ir darbuotojui. Kliento metodas, turėtų būti pirkti - ir atnaujinti jo specifines sąvybęs atitinkamai, 
# o Darbuotojo metodas turėtų būti parduoti ir tiesiog pranešti, kad produktas yra parduotas. 
# Taip pat turi parašyti, koks produktas yra parduotas

# Sukurti sąrašą kuriame saugosime Klientus ir Darbuotojus, 
# sukurti funkcijas kurių pagalba galime leisti naudotojui 
# įvesti Kliento arba darbuotojo duomenis ir pasinaudojant jau turimomis funkcijomis, jas pabaigti sukurti.
 
# Leisti naudotojui pasirinkti ar kurti darbuotoją ar klientą
#  ir kurti tol kol bus paspausta tiesiog enter
# Sukūrus įdėti į sąrašą 


# import datetime

# class Zmogus:
#     def __init__(self,vardas, pavarde, amzius):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.amzius = amzius
        
#     def __repr__(self):
#         return f"{self.vardas}, {self.pavarde}"
        
# class Darbuotojas(Zmogus):
#     def __init__(self,pareigos, isidarbinimo_data,vardas, pavarde, amzius):
#         super().__init__(vardas, pavarde, amzius)
#         self.pareigos = pareigos
#         self.isidarbinimo_data = isidarbinimo_data

#     def parduoti(self,produktas):
#         print (f"Parduotas {produktas}")



# class Klientas(Zmogus):
#     def __init__(self, vardas, pavarde, amzius,pirkiniu_kiekis, paskutinio_uzs_data):
#         super().__init__(vardas, pavarde, amzius)
#         self.pirkiniu_kiekis = pirkiniu_kiekis
#         self.paskutinio_uzs_data = paskutinio_uzs_data

#     def pirkti(self):
#         self.pirkiniu_kiekis +=1
#         self.paskutinio_uzs_data = datetime.datetime.now

# def sukurti_darbuotoja(vardas,pavarde,amzius,pareigos, isidarbinimo_data):      
#     darbuotojas = Darbuotojas(pareigos,isidarbinimo_data,vardas,pavarde,amzius)
#     return darbuotojas

# def sukurti_klienta(vardas, pavarde, amzius,pirkiniu_kiekis = 0, paskutinio_uzs_data =None):
#     klientas = Klientas(vardas, pavarde, amzius,pirkiniu_kiekis, paskutinio_uzs_data)
#     return klientas

# def tikrinti_data(ivesta_data):
#     try:
#         ivesta_data == datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
#         return True, ivesta_data
#     except:
#         return False, None
    


# vyras = Klientas("Juste","Balt",30,5,datetime.datetime.now())




# def pagrindinis_meniu():

#     while True:
#         operasija = input(""" Pasirinkite norima operacija: ivedant jos numeri:
#         1. Ivesti darbuotoja:
#         2. Ivesti klienta""")

#         if operasija == "1":
#             vardas1 = input("Iveskite varda")
#             pavarde1 = input("Iveskite pavarde")
#             amzius1 = int(input("Iveskite amziu"))
#             pareigos1 = input("Iveskite pareigas")
#             isidarbinimo_data = input("Iveskite isidarbinimo data formatu yyyy-mm-dd")

#             data,ar_teisinga = tikrinti_data(isidarbinimo_data)

#             if not ar_teisinga:
#                 print("Data ivesta netinkamai")
#                 continue

#             klienai_darbuotojai.append(sukurti_darbuotoja(vardas1,pavarde1,amzius1,pareigos1,data))


#         elif operasija == "2":
#             pass


# klienai_darbuotojai =[]
# pagrindinis_meniu()



# print(klienai_darbuotojai)



# ----------------------------------------------

# # Sukurkite tris klases Žmogus ir dvi paveldinčias klases Darbuotojas ir Klientas.
# # Žmogus turės vardą pavardę, o Darbuotojas pareigas ir įsidarbinimo datą. O klientas pirkimų kiekį ir paskutinio užsakymo datą.
# # Sukurti dvi funkcijas, kurios priims Klientui arba Darbuotojui reikalingas sąvybes - kaip argumentus ir sukurs šiuos objektus,
# # sukūrus grąžins šiuos objektus
# # Sukurti po Metodą klientui ir darbuotojui. Kliento metodas, turėtų būti pirkti - ir atnaujinti jo specifines sąvybęs atitinkamai,
# # o Darbuotojo metodas turėtų būti parduoti ir tiesiog pranešti, kad produktas yra parduotas. Taip pat turi parašyti, koks produktas yra parduotas
 
# # Sukurti sąrašą kuriame saugosime Klientus ir Darbuotojus,
# # sukurti funkcijas kurių pagalba galime leisti naudotojui įvesti Kliento arba darbuotojo duomenis ir pasinaudojant jau turimomis funkcijomis,
# # jas pabaigti sukurti.
# # Leisti naudotojui pasirinkti ar kurti darbuotoją ar klientą ir kurti tol kol bus paspausta tiesiog enter
# # Sukūrus įdėti į sąrašą
 
# import datetime
# class Zmogus:
#     def __init__(self,vardas,pavarde,amzius):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.amzius = amzius
#     def __repr__(self):
#         return f'{self.vardas} {self.pavarde}'
 
# class Darbuotojas(Zmogus):
#     def __init__(self,pareigos,isidarbinimo_data,vardas,pavarde,amzius):
#         self.pareigos = pareigos
#         self.isidarbinimo_data = isidarbinimo_data
#         super().__init__(vardas,pavarde,amzius)
   
#     def parduoti(self,produktas):
#         print(f'Parduotas {produktas}')
 
# class Klientas(Zmogus):
#     def __init__(self,paskutinio_uzs_data,vardas,pavarde,amzius,pirkiniu_kiekis = 0):
#         self.pirkiniu_kiekis = pirkiniu_kiekis
#         self.paskutinio_uzs_data = paskutinio_uzs_data
#         super().__init__(vardas,pavarde,amzius)
 
#     def pirkti(self):
#        self.pirkiniu_kiekis = self.pirkiniu_kiekis + 1
#        self.paskutinio_uzs_data = datetime.datetime.now()
 
 
# def sukurti_darbuotoja(pareigos,isidarbinimo_data,vardas,pavarde,amzius):
#     darbuotojas = Darbuotojas(pareigos,isidarbinimo_data,vardas,pavarde,amzius)
#     return darbuotojas
 
# def sukurti_klienta(vardas,pavarde,amzius,pirkiniu_kiekis = 0,paskutinio_uzs_data = datetime.datetime.now()):
#     klientas = Klientas(vardas,pavarde,amzius,pirkiniu_kiekis,paskutinio_uzs_data = datetime.datetime.now())
#     return klientas
 
# # sukurti funkcijas kurių pagalba galime leisti naudotojui įvesti Kliento arba darbuotojo duomenis ir pasinaudojant jau turimomis funkcijomis,
# # jas pabaigti sukurti.
# # Leisti naudotojui pasirinkti ar kurti darbuotoją ar klientą ir kurti tol kol bus paspausta tiesiog enter
# # Sukūrus įdėti į sąrašą
# # Parašyti funkcija, kuri tikrina ar data yra korektiška ir grąžina tinkamai stringą paversta į datą,
# # kitu atveju prasukime cikla į naują iteracija
 
# def tikrinti_data(data):
#     try:
#         data = datetime.datetime.strptime(data, "%Y-%m-%d")
#         return data, True
#     except:
#         return None, False
 
# def main_menu():
#     while True:
#         veiksmas = input('Rinkites:  Darbuotojas - 1, Klientas - 2: ')
#         if veiksmas == '1':
#             pareigos = input('Iveskite pareigas: ')
#             isidarb_data = input('Iveskite isidarbinimo metus: ')
#             data, ar_teisinga = tikrinti_data(isidarb_data)
#             if not ar_teisinga:
#                 continue
#             vardas = input('Iveskite varda: ')
#             pavarde = input('Iveskite pavarde: ')
#             amzius = int(input('Iveskite amziu: '))
#             klientai_darbuotojai.append(sukurti_darbuotoja(pareigos,data,vardas,pavarde,amzius))
#         elif veiksmas == '2':
#             vardas = input('Iveskite varda: ')
#             pavarde = input('Iveskite pavarde: ')
#             amzius = int(input('Iveskite amziu: '))
#             klientai_darbuotojai.append(sukurti_klienta(vardas,pavarde,amzius))
#         elif veiksmas == '':
#                 break
 
# klientai_darbuotojai = []        
# main_menu()
# print(klientai_darbuotojai)
#

# ----------------------------------ND----------------------------------------------
# 1 UZDUOTIS
# Sukurti programą, kuri:
# •Turėtų klasę Automobilis
# •Automobilis turėtų savybes: metai, modelis, kuro_tipas
# •Automobilis turėtųmetodus: vaziuoti, stoveti, pildyti_degalu,kurie atitinkamai atspausdintų „Važiuoja“, „Priparkuota“, „Degalai įpilti“
# •Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą
# •Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis)
# •Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip, kad jis atspausdintų „Baterija įkrauta“
# •Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“
# •Sukurti norimą Automobilio objektą
# •Sukurti norimą Elektromobilio objektą
# •Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti,pildyti_degalu
# •Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti,stoveti,pildyti_degalu,vaziuoti_autonomiskai

# class Automobilis:
#     def __init__(self ,metai, modelis, kuro_tipas):
#         self.metai =metai
#         self.modelis = modelis
#         self.kuro_tipas = kuro_tipas

#     def vaziuoti(self):
#         print("Vaziuoja")

#     def stoveti(self):
#         print("Priparkuotas")

#     def pildyti_degalu(self):
#         print("Degalai_ipilti")

#     def __str__(self):
#         return f"""Metai - {self.metai}
# Modelis - {self.modelis}
# Kuro tipas - {self.kuro_tipas}"""
    
# class Elektromobilis(Automobilis):
#     def __init__(self, metai, modelis, kuro_tipas):
#         super().__init__(metai, modelis, kuro_tipas)

#     def vaziuoti_autonomiskai(self):
#         print("Vaziuoja autonomiskai")

#     def pildyti_degalu(self):
#         print("Bterija ikrauta")

# auto =Automobilis(2020,"Audi","benzinas")
# print(auto)

# auto_elektrinis = Elektromobilis(2025,"Nisan","elektra")
# print(auto_elektrinis)
        
# automobiliai = [auto,auto_elektrinis]      
# for automobilis in automobiliai:
#     automobilis.vaziuoti()
#     automobilis.stoveti()
#     automobilis.pildyti_degalu()

# auto_elektrinis.vaziuoti()
# auto_elektrinis.stoveti()
# auto_elektrinis.pildyti_degalu()
# auto_elektrinis.vaziuoti_autonomiskai()




# # 2.UZDUOTIS 
# # Sukurti programą, kuri:
# # •Turėtų klasę Darbuotojas
# # •Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
# # •Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
# # •Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
# # •Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą, dirbant darbuotojui 5 dienas per savaitę
# # •Sukurti norimą Darbuotojo objektą
# # •Sukurti norimą NormalusDarbuotojas objektą
# # •Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima

# import datetime

# class Darbuotojas:
#     def __init__(self, vardas, valandos_ikainis, dirba_nuo):
#         self.vardas = vardas
#         self.valandos_ikainis =valandos_ikainis
#         self.dirba_nuo = dirba_nuo

#     def __isdirbtos_dienos(self):
#         dirbta_dienu = (datetime.datetime.now() - self.dirba_nuo).days
#         return dirbta_dienu
    
#     def paskaiciuoti_atlyginima(self):
#         atlyginimas = self.__isdirbtos_dienos()*8*self.valandos_ikainis
#         return atlyginimas

#     def __str__(self):
#         return f"{self.vardas} - {self.valandos_ikainis} - {self.dirba_nuo}"

# class Normalus_darbuotojas(Darbuotojas):
    
#     def paskaiciuoti_atlyginima(self):
#         atlyginimas_normalaus = (self.__isdirbtos_dienos()-(self.__isdirbtos_dienos()//7)*2)*8*self.valandos_ikainis
#         return atlyginimas_normalaus

# valandinis_atlygis = 5
# isidarbinimo_data = datetime.datetime(2025,2,1)

# darbuotojas_tomas = Darbuotojas("Tomas",valandinis_atlygis,isidarbinimo_data)
# print(darbuotojas_tomas)

# normalus_saulius = Normalus_darbuotojas("Saulius",valandinis_atlygis,isidarbinimo_data)
# print(normalus_saulius)
        
# print(darbuotojas_tomas.paskaiciuoti_atlyginima())        

# print(normalus_saulius.paskaiciuoti_atlyginima())
        


# 3 UZDUOTIS 

# Patobulinti 5 pamokos biudžeto programą:
# •Sukurti tėvinę klasę Irasas, kurioje būtų savybės suma , iš kurios klasės PajamuIrasas ir IslaiduIrasas paveldėtų visas savybes.
# •Į klasę PajamuIrasas papildomai pridėti savybes siuntejas ir papildoma_informacija, kurias vartotojas galėtų įrašyti.
# •Į klasę IslaiduIrasas papildomai pridėti savybes atsiskaitymo_budas ir isigyta_preke_paslauga, kurias vartotojas galėtų įrašyti.
# •Atitinkamai perdaryti klasės Biudzetas metodus gauti_balansa ir gauti_ataskaita kad pasiėmus įrašą iš žurnalo, 
# atpažintų, ar tai yra pajamos ar išlaidos (pvz., panaudojus isinstance() metodą) ir atitinkamai atliktų veiksmus.
# •Padaryti, kad vartotojui (per konsolę) būtų leidžiama įrašyti pajamų ir išlaidų įrašus, peržiūrėti balansą ir ataskaitą.


import pickle
    
class Irasas:

    def __init__(self,suma):
        self.ivesta_suma = suma

        # if self.ivesta_suma>=0:
        #     self.ivestas_tipas = "Pajamos"
        # else:
        #     self.ivestas_tipas = "Islaidos"

    def __str__(self):
        return self.ivesta_suma
    
class Pajamu_irasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas =siuntejas
        self.papildoma_informacija = papildoma_informacija

class Islaidu_irasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas =atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

class Biudzetas:

    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self,suma, siuntejas, papildoma_informacija):
        irasas = Pajamu_irasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(irasas)
    
    def prideti_islaidu_irasa(self,suma,atsiskaitymo_budas, isigyta_preke_paslauga):
        irasas =Islaidu_irasas(suma,atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(irasas)
        
    def skaiciuoti_balansa(self):
        pajamos = 0
        islaidos = 0
        for irasas in self.zurnalas:
            if isinstance(irasas,Pajamu_irasas):
                pajamos += irasas.ivesta_suma
            elif isinstance(irasas,Islaidu_irasas):
                islaidos += abs(irasas.ivesta_suma)

            # if irasas.ivestas_tipas == "Pajamos":
            #     pajamos += irasas.ivesta_suma
            # elif irasas.ivestas_tipas == "Islaidos":
            #     islaidos += abs(irasas.ivesta_suma)
        return pajamos-islaidos
    
    def rodyti_ataskaita(self):
        ataskaita = "Jusu balanso ataskaita:\n"
        for irasas in self.zurnalas:
            if isinstance (irasas,Pajamu_irasas):
                ataskaita += f"\nPajamos: {irasas.ivesta_suma}\nSiuntejas: {irasas.siuntejas}\nPapildoma informacija: {irasas.papildoma_informacija}\n"
            elif isinstance (irasas,Islaidu_irasas):
                ataskaita += f"\nIslaidos: {irasas.ivesta_suma}\nIsigyta preke/paslauga: {irasas.isigyta_preke_paslauga}\nAtsiskaitymo budas: {irasas.atsiskaitymo_budas}\n"
        return ataskaita

biudzetas = Biudzetas()

try:
    with open("pajamos_islaidos.pickle","rb")as failas:
        biudzetas.zurnalas = pickle.load(failas)
except (EOFError,FileNotFoundError):
    print("Nera duomenu pradeta nuo naujo")
    
while True:
#     try:
#         norima_operacija = int(input("""Pasirinkite norima operacija ir iveskite jos numeri:
#                                 1. Ivesti pajamas.
#                                 2. Ivesti islaidas.
#                                 3. perziureti balansa.
#                                 4. Perziureti biudzeto ataskaita.
#                                 5. iseiti is programos. 
#                                      : """))
#         if norima_operacija<1 or norima_operacija>4:
#             print("Pasirinkote neegzistuojanti operacijos numeri.Veskite dar karta.")

#         if norima_operacija == 1:

#             ivedamos_pajamos_islaidos=int(input("Iveskite pajamas: "))
#             irasas = Irasas(ivedamos_pajamos_islaidos)
#             ivestas_siuntejas = input("Iveskite siuntejo duomenis:\n Vardas Pavarde: ")
#             ivesta_papildoma_info = input("Iveskite norima papildoma informacija: ")
#             biudzetas.prideti_pajamu_irasa(ivedamos_pajamos_islaidos,ivestas_siuntejas,ivesta_papildoma_info)

#         elif norima_operacija == 2:

#             ivedamos_pajamos_islaidos=int(input("Iveskite islaidas. Islaidas veskite su '-' zenklu : "))
#             ivestas_atsiskaitymo_budas = input("Iveskite atsiskaitymo buda: Kortele/Pavedimu: " )
#             ivesta_isigyta_preke = input("Iveskite isigytos prekes/paslaugos pavadinima: ")
#             biudzetas.prideti_islaidu_irasa(ivedamos_pajamos_islaidos,ivestas_atsiskaitymo_budas,ivesta_isigyta_preke)

#         elif norima_operacija == 3:
#             print(f"Jusu balansas yra: {biudzetas.skaiciuoti_balansa()}")

#         elif norima_operacija == 4:
#             print(biudzetas.rodyti_ataskaita())

#         elif norima_operacija == 5:
#             break
#     except ValueError:
#         print("Ivedete ne skaiciu. Pasirinkite norima operacija ir bandykite dar karta")

# print("Programa baigta")

# with open("pajamos_islaidos.pickle","wb")as failas:
#     pickle.dump(biudzetas.zurnalas,failas)
    
# exit()