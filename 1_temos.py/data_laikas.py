# datetime
import datetime # bibliotekos ikelimas i musu programa
 
# print(datetime.datetime.today()) # Grazina dabartine data ir laika
# print(datetime.date.today()) # grazina tik data
# print(datetime.datetime.today().time()) # grazina tik laika
 
# dob = datetime.datetime(1992,5,19,19,10,15) # sukuria data ir laika (datetime.date sukurtu tik data)
# print(dob)
 
# suformatuota = dob.strftime("%Y,%m,%d ") # strftime - string from time | suformatuoja data i stringa, pagal nurodymus skliausteliuose
# print(suformatuota)
 
 
# ivestis = input("Iveskite savo gimimo data (yyyy-mm-dd)")
# # 2025-09-05
# dob = datetime.datetime.strptime(ivestis,"%Y-%m-%d") # strptime - parse time from string
# print(dob)
 
# dob = datetime.datetime(1992,5,19,19,10,15) # sukuria data ir laika (datetime.date sukurtu tik data)
# print(dob)

# import datetime
 
# # Create date objects directly
# date1 = datetime.date(2024, 1, 1)
# date2 = datetime.date(2025, 2, 5)
 
# # 2025 - 2024 - 1 * 12 (12) + 1 -> 12 + 1 = 13
# months = (date2.year - date1.year) * 12 + (date2.month - date1.month)
# print("Total months passed:", months)

# 1 UZDUOTIS--------------------------

# listas =[2,"Rokas",5,"Justas",0.5, True, True, 2.5, 55.5, 100]
# suma = 0

# for skaicius in listas:
#     if type(skaicius) is int or type(skaicius) is float:
#         suma = suma+skaicius
# print(suma)

# PROGRAMA------------

# skaicius = int(input("Iveskite skaiciu "))
# skaicius_teigiamas = True
# skaicius_neigiamas = False

# if skaicius >0:
#     print(skaicius_teigiamas)
# else:
#     print(skaicius_neigiamas)
    

# 2 UZDUOTIS-------------------------

# import datetime

# dabartinis_laika = datetime.datetime.today()
# print(dabartinis_laika)

# # dienos = datetime.timedelta(days=5)
# # print(dienos)

# # pries_5 = dabartinis_laika-dienos
# # print(pries_5)

# # # arba

# # print(datetime.datetime.today())
# # print((datetime.datetime.today())-(datetime.timedelta(days=5)))

# # print((datetime.datetime.today())+(datetime.timedelta(hours=8)))

# formatuota_data = dabartinis_laika.strftime("%Y %m %d, %H %M %S")
# print(formatuota_data)

# 3 UZDUOTIS----------------
# dob = "1989-03-26"
# # dob = input("Iveskite savo gimimo data. Formatu: yyyy-mm-dd ")
# dabartine_data = datetime.datetime.today()
# print(dabartine_data)

# dob = datetime.datetime.strptime(dob, "%Y-%m-%d")
# print(dob)

# sekundes = (dabartine_data-dob).total_seconds()
# print(round(sekundes))

# minutes = sekundes/60
# print(round(minutes))

# val = minutes/60
# print(round(val))

# dienos = (dabartine_data-dob).days
# print(dienos)

# men = (dabartine_data.year-dob.year)*12 + (dabartine_data.month-dob.month)
# print(men)

# metai = dabartine_data.year-dob.year
# print(metai)

# from datetime import datetime
# from dateutil.relativedelta import relativedelta
 
# ivestis = input("Iveskite norima data ir laika formatu yyyy-mm-dd hh:mm:ss : ")
# paverstas = datetime.strptime(ivestis, "%Y-%m-%d %H:%M:%S")
 
# dabar = datetime.today()
 
 
# skirtumas = dabar - paverstas  
# rel_skirtumas = relativedelta(dabar, paverstas)  
 
# total_seconds = skirtumas.total_seconds()
# total_minutes = total_seconds / 60
# total_hours = total_seconds / 3600
# total_days = skirtumas.days  
# total_months = (rel_skirtumas.years * 12) + rel_skirtumas.months  
# total_years = rel_skirtumas.years  
 
# print("Jusu ivesta data:", paverstas)
# print("Dabar yra:", dabar)
# print(f"Nuo ivestos datos praejo: {round(total_seconds)} sekundziu")
# print(f"Nuo ivestos datos praejo: {round(total_minutes)} minuciu")
# print(f"Nuo ivestos datos praejo: {round(total_hours)} valandu")
# print(f"Nuo ivestos datos praejo: {total_days} dienu")
# print(f"Nuo ivestos datos praejo: {total_months} menesiu")
# # print(f"Nuo ivestos datos praejo: {total_years} metu")
