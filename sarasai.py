# # sarasas = []
# # print(sarasas)

# skaiciai = [10, 85, 6588888, 0.2]
# zodzizi = ["labas", "kaip", "sekasi"]
# kiti = ["labas, 10,  "]

# sarasas = [] # sukuria tuscia sarasa # kaip ir int ir float ir string sarasas yra tiesiog dar vienas kintamojo tipas
# # print(sarasas)
 
# skaiciai = [10, 85, -9, 1, 105, 10546]
# print(skaiciai)
 
# zodziai = ["Labas", "Kaip", "Sekasi"]
# print(zodziai)
 
# kiti = [True, False, True, True, False, 8.5, "Labas", 4]
# print(kiti)


# skaiciai = [10, 85, -9, 1, 105, 10546]
# print(skaiciai[4])

# skaicius1 = skaiciai[4]

# skaiciai = [10, 85, -9, 1, 105, 5]
# print(skaiciai)
# skaiciai.append(17)
# print(skaiciai)

# skaiciai = [10, 85, -9, 1, 105, 5]
# print(skaiciai)
# skaiciai[1] = -2
# print(skaiciai)

# skaiciai = [10, 85, -9, 1, 105, 5]
# print(skaiciai)
# skaiciai.insert(1,52)
# print(skaiciai)

# skaiciai = [10, 85, -9, 1, 105, 5]
# print(skaiciai)
# skaiciai.pop(2) 
# print(skaiciai)
# skaiciai.remove(1)
# print(skaiciai)

# naujas sarasas:
# sarasas = []
# prideti i sarasa:
# sarasas.append(reiksme)
# Pakeisti reiksme:
# sarasas[indeksas] = nauja_reiksme
# Istrinti reiksme:
# sarasas.pop(indeksas)
# arba
# sarasas.remove(reiksme)

# kiekiai = [5, 15, 36, 1000, -8, 2.5]
# # print(kiekiai)

# # kiekiai.append(600)
# # print(kiekiai)

# # kiekiai.insert(3,601)
# # print(kiekiai)

# # kiekiai.pop(2)
# # print(kiekiai)

# # istrintas = kiekiai.pop(4)
# # print(istrintas)

# # kiekiai[3] = 55
# # print(kiekiai)

# # kiekiai[0] = 900
# # print(kiekiai)

# # kiekiai.clear()
# # print(kiekiai)

# # prekes = ["suris", "morka"]
# # kiekiai.extend(prekes)
# # print(kiekiai)

# UZDUOTIS naujas sarasas
# sarasas[]
# prideti i sarasa sarasas.append(reiksme)
# pakeisti reiksme sarasas[indeksas], nauja_reiksme
# istrinti reiksme sarasas.pop(indeksas) arba sarasas.remove(reiksme)
 
 
# sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sarasas)
 
# sarasas1 = [11, 12, 13, 14, 15]
# sarasas.extend(sarasas1)
# print(sarasas)
 
# sarasas.append(11)
# print(sarasas)
 
# sarasas[8]=sarasas[8] + 8
# sarasas.insert(3, 14)
# print(sarasas)
 
# sarasas.pop(5)
# pasalintas = sarasas.pop(5)
# print(pasalintas)
# print(sarasas)
 
# sarasas.remove(7)
# print(sarasas)
 
# sarasas.reverse()
# print(sarasas)
 
# sarasas.sort(reverse=True)
# print(sarasas)
 
# skaicius = 12
# indeksas = sarasas.index(skaicius)
# print(f"Skaicius {skaicius} yra sarase {indeksas} vietoje")
 
# sarasas1 = sarasas.copy()
# sarasas.clear()
# print(sarasas)
# print(sarasas1)
 
# kiekis = sarasas1.count(14)
# print(kiekis)


# ------------------------------------------------------------

# print("Programa skaičiuotuvas.")
# print()
 
# a = (input("Įveskite pirmą skaičių: "))
# if a.replace(".","").replace("-", "").isdigit() or a == 0:
#     a = float(a)
# else:
#     print(f"{a} nėra skaičius")
 
# symbol = input("Įveskite metematinį veiksmą\n(Pvz.: +, -, *, /, n^2 arba root) ")
# if symbol == "n^2":
#     print("\tPirmas įvestas skaičius, bus keliamas antro skaičiaus laipsniu")
# elif symbol == "root":
#     print("\tIš pirmo įvesto skaičiaus, bus traukiama antro skaičiaus laipsnio šaknis")
 
# b = (input("Įveskite antrą skaičių: "))
# if b.replace(".","").replace("-", "").isdigit() or b == 0:
#     b = float(b)
# else:
#     print(f"{b} nėra skaičius")
 
# if type(a) == float and type(b) == float:
#     match symbol:
#         case "+":
#             print(f"Rezultatas: {a} + {b} = {a+b}")
#         case "-":
#             print(f"Rezultatas: {a} - {b} = {a-b}")
#         case "*":
#             print(f"Rezultatas: {a} * {b} = {a*b}")
#         case "/":
#             if a == 0:
#                 print("Nulio dalinti negalima")
#             elif b == 0:
#                 print("Iš nulio dalinti negalima")
#             else:
#                 print(f"Rezultatas: {a} / {b} = {a/b}")
#         case "n^2":
#             print(f"Rezultatas: {a} ^ {b} = {a**b}")
#         case "root":
#             print(f"Rezultatas: {b}root({a}) = {a**b}")
#         case _:
#             print("Tokios operacijos šiuo metu nėra")
# else:
#     print("Programos klaida")


# ****************************************************************
# # SKAICIUOTUVAS SKAICIUOTUVAS SKAICIUOTUVAS SKAICIUOTUVAS
# ***************************************************************






# skaicius1 = input("Iveskite pirma skaiciu ")
# if skaicius1.replace(".","").replace("-", "").isdigit() or skaicius1 == 0:
#     skaicius1 = float(skaicius1)

#     veiksmas = input("Iveskite veiksma; +, -, *, arba /")
#     if veiksmas == "+" or veiksmas == "-" or veiksmas == "*" or veiksmas == "/":
#         skaicius2 = input("Iveskite antra skaiciu ")

#         if skaicius2.replace(".","").replace("-", "").isdigit() or skaicius2 == 0:
#             skaicius2 = float(skaicius2)

#             match veiksmas:
#                 case "+":
#                     print(f"Rezultatas  {skaicius1 + skaicius2}")
#                 case "-":
#                     print(f"Rezultatas  {skaicius1 - skaicius2}")
#                 case "*":
#                     print(f"Rezultatas  {skaicius1 * skaicius2}")
#                 case "/":
#                     print(f"Rezultatas  {skaicius1 / skaicius2}")
#         else:
#             print("netinkamas simbolis")
#     else:
#         print("Netinkamas veiksmas")
# else:
#     print("netinkamas simbolis")

# -------------------------------------------------------------

# sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sarasas)
 
# sarasas1 = [11, 12, 13, 14, 15]
# sarasas.extend(sarasas1)
# print(sarasas)
 
# sarasas.append(11)
# print(sarasas)
 
# sarasas[8]=sarasas[8] + 8
# sarasas.insert(3, 14)
# print(sarasas)
 
# sarasas.pop(5)
# pasalintas = sarasas.pop(5)
# print(pasalintas)
# print(sarasas)
 
# sarasas.remove(7)
# print(sarasas)
 
# sarasas.reverse()
# print(sarasas)
 
# sarasas.sort(reverse=True)
# print(sarasas)
 
# skaicius = 12
# indeksas = sarasas.index(skaicius)
# print(f"Skaicius {skaicius} yra sarase {indeksas} vietoje")
 
# sarasas1 = sarasas.copy()
# sarasas.clear()
# print(sarasas)
# print(sarasas1)
 
# kiekis = sarasas1.count(14)
# print(kiekis)
 
# --------------------------------------

