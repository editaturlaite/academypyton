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


import datetime

class Zmogus:
    def __init__(self,vardas, pavarde, amzius):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius
        
    def __repr__(self):
        return f"{self.vardas}, {self.pavarde}"
        
class Darbuotojas(Zmogus):
    def __init__(self,pareigos, isidarbinimo_data,vardas, pavarde, amzius):
        super().__init__(vardas, pavarde, amzius)
        self.pareigos = pareigos
        self.isidarbinimo_data = isidarbinimo_data

    def parduoti(self,produktas):
        print (f"Parduotas {produktas}")



class Klientas(Zmogus):
    def __init__(self, vardas, pavarde, amzius,pirkiniu_kiekis, paskutinio_uzs_data):
        super().__init__(vardas, pavarde, amzius)
        self.pirkiniu_kiekis = pirkiniu_kiekis
        self.paskutinio_uzs_data = paskutinio_uzs_data

    def pirkti(self):
        self.pirkiniu_kiekis +=1
        self.paskutinio_uzs_data = datetime.datetime.now

def sukurti_darbuotoja(vardas,pavarde,amzius,pareigos, isidarbinimo_data):      
    darbuotojas = Darbuotojas(pareigos,isidarbinimo_data,vardas,pavarde,amzius)
    return darbuotojas

def sukurti_klienta(vardas, pavarde, amzius,pirkiniu_kiekis = 0, paskutinio_uzs_data =None):
    klientas = Klientas(vardas, pavarde, amzius,pirkiniu_kiekis, paskutinio_uzs_data)
    return klientas

def tikrinti_data(ivesta_data):
    try:
        ivesta_data == datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
        return True, ivesta_data
    except:
        return False, None
    


vyras = Klientas("Juste","Balt",30,5,datetime.datetime.now())




def pagrindinis_meniu():

    while True:
        operasija = input(""" Pasirinkite norima operacija: ivedant jos numeri:
        1. Ivesti darbuotoja:
        2. Ivesti klienta""")

        if operasija == "1":
            vardas1 = input("Iveskite varda")
            pavarde1 = input("Iveskite pavarde")
            amzius1 = int(input("Iveskite amziu"))
            pareigos1 = input("Iveskite pareigas")
            isidarbinimo_data = input("Iveskite isidarbinimo data formatu yyyy-mm-dd")

            data,ar_teisinga = tikrinti_data(isidarbinimo_data)

            if not ar_teisinga:
                print("Data ivesta netinkamai")
                continue

            klienai_darbuotojai.append(sukurti_darbuotoja(vardas1,pavarde1,amzius1,pareigos1,data))


        elif operasija == "2":
            pass


klienai_darbuotojai =[]
pagrindinis_meniu()



print(klienai_darbuotojai)



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
# susitariam gal ilgesnius nei 50 eiluciu det..., kurį pateikė Mantas Jucius
# Mantas Jucius
# 10:57
# susitariam gal ilgesnius nei 50 eiluciu deti failais, o ne txt?
# turi kontekstinį meniu


# turi kontekstinį meniu
