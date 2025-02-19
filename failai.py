# https://www.w3schools.com/python/module_os.asp?ref=escape.tech

# import os # impportuojame (itraukiame os)
# # os.chdir("Testinis") # pakeicia aplanka
# # os.mkdir("Testinis_vidinis") # musu esamame aplanke sukuria nauja aplanka
# # os.chdir("C:\AMD\AMD-Software-Installer")
# os.mkdir(r"C:\UserBenchmark\Testinis_vidinio_vidinis") # \ simboliukas reiskia, kad po jo eina specialus simbolis
# # du būdai nurodyti kelią arba naudoti dviguba bruksneli - \\ arba parasyti pries stringa r raide
# # print("labas \n sveiki")

# https://www.epochconverter.com/

# import datetime
# print(datetime.datetime.fromtimestamp(1739432495))


# with open("naujas.txt","w") as failas:
#     failas.write("As esu tekstas faile")

# https://www.geeksforgeeks.org/file-mode-in-python/

# with open("naujas.txt","r", encoding="utf-8") as failas: # encoding butinas dirbant su lt ar kitom specialiom raidem
#     # print(failas.readlines())
#     for line in failas.readlines(): # failas = readlines - nuskaito eilutes kaip saraso elementus | readline skaito po eilute
#         print(line, end="")


# 1. UZDUOTIS
# Patarimai:

# Naudoti from datetime import datetime, datetime.today().
# Kintamajam priskirti sakinį, kuriuo bus operuojama, eilutėmis.
# Kai kur galima panaudoti funkcijas iš praeitų pamokų.

# ------1.1------
# Sukurtų failą „Tekstas.txt“ su pilnu tekstu "Zen of Python".

# import this
import os

with open("tekstas.txt", "w") as failas:
    failas.write("""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""")
    

# ----1.2-----
# Atspausdintų tekstą iš sukurto failo.

# with open("tekstas.txt", "r") as failas:
#     print(failas.read())


# ------1.3------
# Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką.

# import datetime

# with open("tekstas.txt","a+")as failas:

#     data = datetime.datetime.today()
#     data = datetime.datetime.strftime(data,"%Y- %m-%d %H:%M")

#     failas.write(f"\n{data}")

#  ------1.4------
# Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).

# with open("tekstas.txt","r+")as failas:
#     visos_eilute = failas.readlines()

#     sunumeruotos = []
#     eilute_nr =0
#     for eilute in visos_eilute:
#         eilute_nr += 1 
#         sunumeruotos.append(f"{eilute_nr}.{eilute}")
#         failas.seek(0)
#         for naujos in sunumeruotos:
#             failas.write(naujos)

# ----

# with open("Tekstas.txt","r") as failas:
#     nuskait_eilutes = failas.readlines()
   
# with open("Tekstas.txt","w") as failas:
#     for eilute in range(len(nuskait_eilutes)):
#         failas.write(f"{eilute+1} {nuskait_eilutes[eilute]}")


# -------
# with open("tekstinis.txt","r") as failas:
#     nuskait_eilutes = failas.readlines()
 
# with open("tekstinis.txt","w") as failas:
#     for nr, eilute in enumerate(nuskait_eilutes): # enumerate | nr = 0 eilute = nuskait_eilutes[0]
#         failas.write(f"{nr+1} {eilute}")

#   ------1.5------
# Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru.".

# with open("tekstas.txt","r+") as failas:
    
#     visos_eil = failas.read()
#     visos_eil = visos_eil.replace("Beautiful is better than ugly.","Gražu yra geriau nei bjauru.")
#     failas.seek(0)
#     failas.write(visos_eil)

#     print(visos_eil)

# ------1.6------
# Atspausdintų visą failo tekstą atbulai.

# with open("tekstas.txt","r+") as failas:

#     visos_eilutes = failas.read()
#     visos_eilutes = visos_eilutes[::-1]
  
#     failas.seek(0)
#     failas.write(visos_eilutes)

#     print(visos_eilutes)

# ------1.7------
# Atspausdintų, kiek faile yra žodžių, skaičių, didžiųjų ir mažųjų raidžių.

# def skaiciavimas(fraze):
#     sujungta = "".join(fraze)
#     zodziu_skaicius = len(sujungta)
#     sujungta2 =sujungta.replace(" ","")
#     print(sujungta2)
#     did_raides = 0
#     maz_raides = 0
#     skaiciai = 0

#     for elementas in sujungta2:
#         if elementas.isupper():
#             did_raides = did_raides + 1
#         elif elementas.islower():
#             maz_raides = maz_raides + 1
#         elif elementas.isdigit():
#             skaiciai = skaiciai + 1

#     return print(f"Jusu tekste yra:\n {zodziu_skaicius} zodziai.\n {did_raides} didziosios raides.\n{maz_raides} mazosios raides.\n{skaiciai} skaiciu.")

# with open("tekstas.txt","r+") as failas:

#     tekstas = failas.readlines()

# skaiciavimas(tekstas)


# --------------1.8-----------
# Nukopijuotų visą sukurto failo tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS.

# with open("tekstas.txt", "r+")as failas:

#     buves_failas = failas.readlines()
#     naujas_failas = []

#     for eilute in buves_failas:
#         naujas_failas.append(eilute.upper())
#         tekstas = "".join(naujas_failas)

#     with open("tekstas2.tex", "w+") as file:
#         file.write(tekstas)
      

# 2 UZDUOTIS
# Sukurti programą, kuri:
# •Leistų vartotojui įvesti norimą eilučių kiekį
# •Įrašytų įvestą tekstą atskiromis eilutėmis į failą
# •Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
 
# Patarimai:
# •Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)


# pavadinimas_naujas = input("Iveskite kuriamo failo pavadinima: ")
# pavadinimas_naujas = "vartotojo"
# while True: 

#     ivestis = input("Iveskite teksto eilute.\nJei norite iseiti is programos spauskite enter.")

#     if ivestis!="":
#         with open ("ztestinis", "a+")as file:
#             file.write(ivestis + "\n")

#     else:
#         break

# os.rename("ztestinis",pavadinimas_naujas)
# exit()


# --------
# if os.path.exists("kuriamas2"):
#     print ("yra")


# 3 UZDUOTIS

# Sukurti programą, kuri:
# •Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
# •Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
# •Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais
 
# Patarimai:
# •Failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_ctime

import datetime

os.mkdir(r"C:\Users\Vartotojas\Desktop\naujas_katalogas")

data = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
print(data)

with open(r"C:\Users\Vartotojas\Desktop\naujas_katalogas\tekstinis_failas.txt","w")as file:
    file.write(data)


print(f"Sukurimo data: {os.stat(r"C:\Users\Vartotojas\Desktop\naujas_katalogas\tekstinis_failas.txt").st_birthtime}")

print(f"failo dydis yra: {os.stat(r"C:\Users\Vartotojas\Desktop\naujas_katalogas\tekstinis_failas.txt").st_size}")

failo_suk_konvertuota = datetime.datetime.fromtimestamp(1739517637.8328428)
print(failo_suk_konvertuota)
    
    


    

