
 
def clean_data():
    global biblioteka
    biblioteka = {}
    if os.path.exists("biblioteka.pickle"):
        os.remove("biblioteka.pickle")
        return "\nDuomenys ištrinti.\n"
    else:
        return "\nKol kas duomenų nėra.\n"
 
 
# def max_number(numbers): # nemaisyti kalbu
#     # print(max(numbers))
#     return max(numbers) # naudojame tik tuos kintamuosius kurie buvo paduoti kaip argumentai arba sukurti funkcijoje
 
# number_list = [8,5,1,5,6,4,9]
 
# # print(max_number(number_list))
 
# # gauti didziausia skaiciu esanti sarase ir prie jo pridetu 2
 
# print(max_number(number_list)+2)
 
#number_list = ... privalome keisti globalia reiksme kurios galbut nenoretumem keisti
# dirbti is kito failo, kitas programuotojas... negaletu keisti paduodamu reiksmiu... funkcija dalinai netenka savo prasmes
 
 
# def max_number(numbers): # funkcija skirta vienam dalykui, ir neturetu printinti prasyti inputu ir skaiciuoti viename
#     # input... iveskite savo norimus skaicius
#     return max(numbers)
 
# number_list = [8,5,1,5,6,4,9]
 
# print(max_number(number_list)+2)
 
 
# load_data
# read file and return data
 
# save_data
# write to file and return True/False (pavyko ar nepavyko irasyti i faila)
 
# kint1 = input()
# kint2 = input()
# input... input... input - susrenkame informacija
# prideti_knyga(autorius=input1,zanras=input2...)
# sarasas.append(nauja_knyga)
# save_data(sarasas) - kvietimas
#printinam kad viskas pavyko ir klausiam ka daryti toliau (jau ne funkcijoje)
 
# kintamuosius vadiname logiskai FUNKCIJAS TAIP PAT
 
# Ka ismokstame - ta ir naudojame
 
 