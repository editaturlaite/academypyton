# print(7==7)
# print(8==7)
# amzius = 16
# ar_tiesa = amzius==7
# print(f"yra {ar_tiesa}, kad tau 18")

# amzius = 16
# ar_tiesa = amzius!=7
# print(f"yra {ar_tiesa}, kad tau 18")

# amzius = 18
# ar_tiesa = amzius>7
# print(f"yra {ar_tiesa}, kad tau daugiau 18")

# amzius = 18
# ar_tiesa = amzius>=7
# print(f"yra {ar_tiesa}, kad tau daugiau arba 18")

# amzius = 18
# ar_tiesa = (amzius>=7 and amzius < 65)
# print(f"yra {ar_tiesa}, kad tu pilnametis bet ne sinjoras")

# amzius = 18
# ar_tiesa = (amzius>=7 or amzius < 65)
# print(f"yra {ar_tiesa}, kad tu pilnametis bet ne sinjoras")

# vardas = "antanas"
# amzius = 25
# ar_tiesa = (amzius<65 and vardas == "jonas")
# print(f"yra {ar_tiesa}, kad tu pilnametis ir tavo vardas jonas")



# amzius = 18

# if amzius>=18:
#     print("gali pirkti energerinius")
# # if 5>4: #jei tiesa tai daro kas po dvitaskio
# #     print("tiesa")
# print("prorama baigta")

# amzius = 12
# if amzius>=18:
#     print("gali pirkti energerinius")
# else:
#     print("negali pirkti")
# print("prorama baigta")

# amzius = 6
 
# if amzius>=18:
#     print("Tu gali pirkti energetinius gėrimus")
# else: 
#     print("negali pirkti")
# if amzius > 65: 
#         print("esi senjoras")
# else:
#         print("Nesi senjoras")
 

# print("Programa baigta")

# ---------------------------------------------------------------------------------------------

# vardas = input("Iveskite savo varda ")
# slapt = input("Iveskite slaptazodi ")
# vardas1 = "edita"
# slap1 = "turlaite"
# if vardas == vardas1 and slapt == slap1:
#     print("Sveikinam sekmingai prisijungus.")
# else: 
#     print("Duomenys neteisingi")

# --------------------------------------------------------------------------------------------

# a = int(input("Iveskite skaiciu a"))
# b = int(input("Iveskite skaiciu b"))
# if a<b:
#     print("a mazesnis uz b")
# if a==b:
#     print("a lygu b")
# if a>b:
#     print("a daugiau uz b")

# ----------------------------------------------------------------------------------------------
# amzius = int(input("Iveskite amziu"))
# if amzius <=0:
#     print("kalida")
# if amzius<1 and amzius>0:
#     print("naujagimis")
# if amzius>=1 and amzius<2:
#     print("kudikis")
# if amzius>=2 and amzius<13:
#     print("vaikas")
# if amzius>=13 and amzius<18:
#     print("jaunuolis")
# if amzius>=18 and amzius<65:
#     print("suauges")
# if amzius>=65 and amzius<100:
#     print("senjoras")
# if amzius>=100:
#     print("simtametis")

# -------------------------------------------------------------------------------------------------

# kiekis = int(input("iveskit uzsakoma kieki "))
# kaina_vnt = int(input("iveskite vieneto kaina "))
# suma = kiekis*kaina_vnt
# print(f"bendra suma yra: {suma}")
# if suma>=500:
#     suma = int(suma/1.1)
#     print("jums taikoma 10% nuolaida")
# else:
#     print("Nuolaida netaikoma.")

# if suma<=100:
#     suma = suma+5
#     print(f"Jums taikomas 5 siuntimo mokestis. \nGalutine suma: {suma}")
# else:
#      print(f"Jums taikomas nemokamas siuntimas. \nGalutine suma: {suma}")

# -------------------------------------------------

# amzius = 70
# if amzius > 65:
#     print("Tu esi senjoras")
# if amzius > 18:
#     print("Tu esi suauges")
# if amzius > 3:
#     print("Tu esi vaikas")
 
 
# if amzius > 65:
#     print("Tu esi senjoras")
# elif amzius > 18:
#     print("Tu esi suauges")
# elif amzius > 3: #NEBETIKRINA
#     print("Tu esi vaikas")
# else:
#     print("Netiesa")

# -----------------------------

# amzius = 25
 
# match amzius:
#     case 18: # if amzius == 18
#         print("Tu aštuoniolika")
#     case 25: # elif amzius == 25
#         print("Tau 25")
#     case 30: # elif amzius == 25
#         print("Tau 30")
#     case 35: # elif amzius == 25
#         print("Tau 35")  

# ---------------------------------------

# bilietas = "Netikras" # "Paprastas"/"Vip"/"Super Vip"
 
# match bilietas:
#     case "Paprastas": # if bilietas == "Paprastas"
#         print("Prašome eiti i stovimas vietas")
#     case "Vip": # elif bilietas == "Vip"
#         print("Prasome eiti į Vip ložę")
#     case "Super Vip":
#         print("Prasome eiti i specialiai jums paruostas vietas")
#     case _: # else
#         print("Netinkamas bilietas")

# ------------------------------------

# ivestis = input("IVeskite skaiciu") # "15" | "Labas"
 
# # if 5 ==5: # 5 ==5 -> True | False
 
# if ivestis.isdigit():
#     print("Visi yra skaiciai")
#     konvertuotas = int(ivestis)
# else:
#     print("Ivedei ne skaiciu")
    
# ---------------------------------------------

# skaicius1 = input("Iveskite skaiciu ")
# if skaicius1.isdigit():
#     kskaicius1 = int(skaicius1)
#     veiksmas = input("Iveskite veiksma " )
# else:
#     print("netinkamas simbolis") 
# elif: veiksmas == ("+") or ("-") or ("*") or ("/"):
#     skaicius2 = input("Iveskite antra skaiciu ")
#     # else:
#     #     print("netinkamas simbolis") 
#     if skaicius2.isdigit():
#             kskaicius2 = int(skaicius2)
#         # else:
#         #     print("netinkamas simbolis") 

  
# # else:
# #      print("netinkamas simbolis")
# match veiksmas:
#     case "+":
#         print(f"Rezultatas  {kskaicius1 + kskaicius2}")
#     case "-":
#         print(f"Rezultatas  {kskaicius1 - kskaicius2}")
#     case "*":
#         print(f"Rezultatas  {kskaicius1 * kskaicius2}")
#     case "/":
#         print(f"Rezultatas  {kskaicius1 / kskaicius2}")
# # else:
# #     print("netinkamas simbolis")
# # veiksmas = input("Iveskite veiksma" )
# # if veiksmas == ("+") or ("-") or ("*") or ("/"):
# # #     skaicius2 = input("Iveskite antra skaiciu")
# # else:
# #     print("netinkamas simbolis")

# # if skaicius2.isdigit():
# #     # print("gerai")
# #     kskaicius2 = int(skaicius2)
# #     # atsakymas = (kskaicius1 + kskaicius2)
# #     # print(f"rezultatas {atsakymas}")
# # else:
# #     print("netinkamas simbolis")
# # match veiksmas:
#     # case "+":
#     #     print(f"Rezultatas  {kskaicius1 + kskaicius2}")
#     # case "-":
#     #     print(f"Rezultatas  {kskaicius1 - kskaicius2}")
#     # case "*":
#     #     print(f"Rezultatas  {kskaicius1 * kskaicius2}")
#     # case "/":
#     #     print(f"Rezultatas  {kskaicius1 / kskaicius2}")

# #darbui namie
# if a.replace(".","").replace("-", "").isdigit() or a == 0: # "-7.5" -> "-75" -> "75" -> True
#     a = float(a) # float("-7.5")
# else:
#     print(f"{a} nėra skaičius")
# print(8**0.5) # kvadratinės šaknies traukim..., kurį pateikė Justas Kvederis
# Justas Kvederis
# 14:16
# print(8**0.5) # kvadratinės šaknies traukimas
# turi kontekstinį meniu

# pvz darbo
# if a.replace(".","").replace("-", "").isdigit() or a == 0: # "-7.5" -> "-75" -> "75" -> True
#     a = float(a) # float("-7.5")
# else:
#     print(f"{a} nėra skaičius")
 
# print(8**0.5) # kvadratinės šaknies traukimas
 
# Įdėkite patikrinimus ar viskas atliekama teisingai, pavyzdžiui, patys suprantate,
# kad dalinti iš nulio negalima, kaip pavyzdys.
# Kam pavyksta, taip pat padarykite, kad jeigu būtų įvestas ne skaičius, programa nenulūžtų,
# bet praneštų naudotojui, kad buvo įvesta neteisinga reikšmė)
 
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
# # else:
#     print("Programos klaida")
 
# ---------------------------------------------
 

