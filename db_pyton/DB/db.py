# import sqlite3 # leis atlikti veiksmus su duomenų baze
 
# conn = sqlite3.connect(r'Data/Studentu.db') # greitkelis kuriuo judes duomenis
 
# cur = conn.cursor() # automobilis, kuris vazines tuo greitkeliu
 
# cur.execute("""
#             CREATE TABLE IF NOT EXISTS "Students" (
#     "id"    INTEGER NOT NULL UNIQUE,
#     "name"  TEXT NOT NULL,
#     "last_name" TEXT NOT NULL,
#     "age"   INTEGER DEFAULT 19,
#     PRIMARY KEY("id" AUTOINCREMENT)
# );
#             """) # automobilio pakrovimas
 
# conn.commit() # Vaziuok
 
# cur.execute("""Insert into Students(Name,last_name,age) values('Karolis','Karolaitis',37)""")
 
# conn.commit()
 
# conn.close()
 

#  # import sqlite3 # leis atlikti veiksmus su duomenų baze
 
# # conn = sqlite3.connect(r'Data/Studentu.db') # greitkelis kuriuo judes duomenis (jeigu tokios db neras, jis sukurs)
 
# # cur = conn.cursor() # automobilis, kuris vazines tuo greitkeliu
 
# # def sukurti_studentu_lentele():
# #     cur.execute("""
# #                 CREATE TABLE IF NOT EXISTS "Students" (
# #         "id"  INTEGER NOT NULL UNIQUE,
# #         "name"    TEXT NOT NULL,
# #         "last_name"   TEXT NOT NULL,
# #         "age" INTEGER DEFAULT 19,
# #         PRIMARY KEY("id" AUTOINCREMENT)
# #     );
# #                 """) # automobilio pakrovimas
# #     conn.commit()
 
# # sukurti_studentu_lentele()
# # with conn: # atitinka ir commit ir close viename
# #     cur.execute("""Insert into Students(Name,last_name,age) values('Karolis','Karolaitis',37)""")
 
 
# #     cur.execute("Select * From Darbuotojas Where Vardas = 'Petras' ")
 
# #     darbuotojai = cur.fetchall() # cia automobilis dar turi pas jus parvaziuoti, del to naudojam automobili
# #     # print(darbuotojai) # darbuotojai yra sarasas kuriame pilna tuple [(1),(2),(3)]
 
# #     for darbuotojas in darbuotojai:
# #         print(darbuotojas)
 
# # cur.execute("""Insert into Students(Name,last_name,age) values('Karolis','Karolaitis',37)""") # is naujo atidaro
# # conn.commit()
# # # kai jis baigiasi visas musu komandas sucommitina ir uzdaro greitkeli
 
 
 
# import sqlite3 # leis atlikti veiksmus su duomenų baze
 
# conn = sqlite3.connect(r'Data/Studentu.db') # greitkelis kuriuo judes duomenis (jeigu tokios db neras, jis sukurs)
 
# cur = conn.cursor() # automobilis, kuris vazines tuo greitkeliu
 
# def sukurti_studentu_lentele():
#     cur.execute("""
#                 CREATE TABLE IF NOT EXISTS "Students" (
#         "id"    INTEGER NOT NULL UNIQUE,
#         "name"  TEXT NOT NULL,
#         "last_name" TEXT NOT NULL,
#         "age"   INTEGER DEFAULT 19,
#         PRIMARY KEY("id" AUTOINCREMENT)
#     );
#                 """) # automobilio pakrovimas
#     conn.commit()
 
# sukurti_studentu_lentele()
 
# def add_student(name,last_name,age):
#     with conn:
#         cur.execute(f"""Insert into Students(Name,last_name,age) values(?,?,?)""",(name,last_name,age))
#         # Update Students Set Name = ?, last_name = ? ,(name,last_name)
#         # """Insert into Students(Name,last_name,age) values('Justas' Delete From Students ','{last_name}',{age})"""# sql injection
 
 
# vardas = input("Iveskite varda: ") # Justas', 'Delete From Database'
# add_student(vardas,"Justaitis",30)
# # with conn: # atitinka ir commit ir close viename
   
 
 
# kai jis baigiasi visas musu komandas sucommitina ir uzdaro greitkeli

# -- Select * From DARBUOTOJAS Where GIMIMOMETAI BETWEEN '1986-09-19' AND '1988-07-29'
 
# -- SELECT * From DARBUOTOJAS Where SKYRIUS_PAVADINIMAS in ('Java','C#') -- WHere SKYRIUS_PAVADINIMAS = Java OR = C#
 
# -- SELECT * FROM DARBUOTOJAS Where PAVARDE Like 'P%' -- like nurodo, kad mes ieskosime pagal dali atitikimo, tai reiskias, nurodysime tik

# -- -- kazkokia ar stringo ar kazkieno kito dali, kurios ieskosime, mes nezinome tikslios reiksmes arba mums aktualu gauti visus panasius

# -- -- bet neb8tinai su ta pacia reiksme

# -- -- % - bet koks kiekis bet kokiu simboliu
 
# -- SELECT * FROM DARBUOTOJAS Where ASMENSKODAS Like '4%'

# -- _ betkoks simbolis bet tik vienas sombolis

# -- SELECT * FROM DARBUOTOJAS Where PAVARDE Like '__u%' 

# -- SELECT * FROM DARBUOTOJAS Where VARDAS Like '___as' -- atspausdinti visus zmones kuriu vardas yra 5 raides ir baigiasi as
 
# -- SELECT * From DARBUOTOJAS Where PAREIGOS IS NULL -- tai ieskome kur yra null

# -- Select * From DARBUOTOJAS Where (PAREIGOS = kazkas AND kitas = Kazkas) OR Kitas = kazkas
 
# -- SELECT * From DARBUOTOJAS ORDER BY VARDAS DESC -- DESC rikiuoja nuo Z iki A, o pagal nutylejima nuo A iki Z
 
# -- SELECT * From DARBUOTOJAS ORDER BY VARDAS ASC, PAVARDE DESC -- galima rikiuoti pagal kelis stulpelius ir ASC yra Nuo A IKI Z
 
# -- Select upper(Vardas) From DARBUOTOJAS Where lower(PAVARDE) = 'jonaitis'
 
# -- Select upper(Vardas) as vard_did, PAVARDE From DARBUOTOJAS Where vard_did = 'PETRAS' --
 
# -- SELECT CONCAT(Vardas,' ', PAVARDE) as pilnas_vardas From DARBUOTOJAS Where pilnas_vardas = 'Petras Petraitis'
 
# -- SELECT CONCAT(Vardas,' ', PAVARDE) as pilnas_vardas,* From DARBUOTOJAS
 
# Update DARBUOTOJAS Set Vardas = upper(VARDAS) Where Vardas = 'laikinas'
 
 
 
# geri
 
# haha
 
# geri
 
# -- Selects all columns from the DARBUOTOJAS table where the birth year is between '1986-09-19' and '1988-07-29'

# SELECT * FROM DARBUOTOJAS WHERE GIMIMOMETAI BETWEEN '1986-09-19' AND '1988-07-29';
 
# -- Selects all records from DARBUOTOJAS where SKYRIUS_PAVADINIMAS is either 'Java' or 'C#'

# SELECT * FROM DARBUOTOJAS WHERE SKYRIUS_PAVADINIMAS IN ('Java','C#');
 
# -- Selects all records from DARBUOTOJAS where the last name (PAVARDE) starts with 'P'

# SELECT * FROM DARBUOTOJAS WHERE PAVARDE LIKE 'P%';
 
# -- Selects all records where the personal code (ASMENSKODAS) starts with '4'

# SELECT * FROM DARBUOTOJAS WHERE ASMENSKODAS LIKE '4%';
 
# -- Selects all records where the last name (PAVARDE) has any two characters followed by 'u' and then any other characters

# SELECT * FROM DARBUOTOJAS WHERE PAVARDE LIKE '__u%';
 
# -- Selects all records where the first name (VARDAS) is exactly five letters long and ends with 'as'

# SELECT * FROM DARBUOTOJAS WHERE VARDAS LIKE '___as';
 
# -- Selects all records where the job position (PAREIGOS) is NULL (missing value)

# SELECT * FROM DARBUOTOJAS WHERE PAREIGOS IS NULL;
 
# -- Selects all records where PAREIGOS equals some value AND another condition is met, OR another field equals some value

# SELECT * FROM DARBUOTOJAS WHERE (PAREIGOS = 'kazkas' AND kitas = 'Kazkas') OR Kitas = 'kazkas';
 
# -- Selects all records from DARBUOTOJAS and orders the results by first name (VARDAS) in descending order (Z to A)

# SELECT * FROM DARBUOTOJAS ORDER BY VARDAS DESC;
 
# -- Selects all records and orders them first by first name (VARDAS) in ascending order (A to Z), and then by last name (PAVARDE) in descending order (Z to A)

# SELECT * FROM DARBUOTOJAS ORDER BY VARDAS ASC, PAVARDE DESC;
 
# -- Selects the first name (VARDAS) converted to uppercase where the lowercase last name (PAVARDE) is 'jonaitis'

# SELECT UPPER(VARDAS) FROM DARBUOTOJAS WHERE LOWER(PAVARDE) = 'jonaitis';
 
# -- Attempts to select uppercase first names (VARDAS) and last names (PAVARDE) where the alias "vard_did" equals 'PETRAS' (This will cause an error because aliases cannot be used in WHERE clauses)

# SELECT UPPER(VARDAS) AS vard_did, PAVARDE FROM DARBUOTOJAS WHERE vard_did = 'PETRAS';
 
# -- Selects a concatenated full name (VARDAS and PAVARDE with a space in between) and renames the column as "pilnas_vardas" where the full name matches 'Petras Petraitis'

# SELECT CONCAT(VARDAS, ' ', PAVARDE) AS pilnas_vardas FROM DARBUOTOJAS WHERE pilnas_vardas = 'Petras Petraitis';
 
# -- Selects all columns along with a concatenated full name column (VARDAS + PAVARDE) named "pilnas_vardas"

# SELECT CONCAT(VARDAS, ' ', PAVARDE) AS pilnas_vardas, * FROM DARBUOTOJAS;
 
# -- Updates the first name (VARDAS) to uppercase where the first name is 'laikinas'

# UPDATE DARBUOTOJAS SET VARDAS = UPPER(VARDAS) WHERE VARDAS = 'laikinas';

 