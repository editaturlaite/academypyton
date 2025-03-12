import sqlite3 # leis atlikti veiksmus su duomenų baze
 
conn = sqlite3.connect(r'Data/Studentu.db') # greitkelis kuriuo judes duomenis
 
cur = conn.cursor() # automobilis, kuris vazines tuo greitkeliu
 
cur.execute("""
            CREATE TABLE IF NOT EXISTS "Students" (
    "id"    INTEGER NOT NULL UNIQUE,
    "name"  TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "age"   INTEGER DEFAULT 19,
    PRIMARY KEY("id" AUTOINCREMENT)
);
            """) # automobilio pakrovimas
 
conn.commit() # Vaziuok
 
cur.execute("""Insert into Students(Name,last_name,age) values('Karolis','Karolaitis',37)""")
 
conn.commit()
 
conn.close()
 

 # import sqlite3 # leis atlikti veiksmus su duomenų baze
 
# conn = sqlite3.connect(r'Data/Studentu.db') # greitkelis kuriuo judes duomenis (jeigu tokios db neras, jis sukurs)
 
# cur = conn.cursor() # automobilis, kuris vazines tuo greitkeliu
 
# def sukurti_studentu_lentele():
#     cur.execute("""
#                 CREATE TABLE IF NOT EXISTS "Students" (
#         "id"  INTEGER NOT NULL UNIQUE,
#         "name"    TEXT NOT NULL,
#         "last_name"   TEXT NOT NULL,
#         "age" INTEGER DEFAULT 19,
#         PRIMARY KEY("id" AUTOINCREMENT)
#     );
#                 """) # automobilio pakrovimas
#     conn.commit()
 
# sukurti_studentu_lentele()
# with conn: # atitinka ir commit ir close viename
#     cur.execute("""Insert into Students(Name,last_name,age) values('Karolis','Karolaitis',37)""")
 
 
#     cur.execute("Select * From Darbuotojas Where Vardas = 'Petras' ")
 
#     darbuotojai = cur.fetchall() # cia automobilis dar turi pas jus parvaziuoti, del to naudojam automobili
#     # print(darbuotojai) # darbuotojai yra sarasas kuriame pilna tuple [(1),(2),(3)]
 
#     for darbuotojas in darbuotojai:
#         print(darbuotojas)
 
# cur.execute("""Insert into Students(Name,last_name,age) values('Karolis','Karolaitis',37)""") # is naujo atidaro
# conn.commit()
# # kai jis baigiasi visas musu komandas sucommitina ir uzdaro greitkeli
 
 
 
import sqlite3 # leis atlikti veiksmus su duomenų baze
 
conn = sqlite3.connect(r'Data/Studentu.db') # greitkelis kuriuo judes duomenis (jeigu tokios db neras, jis sukurs)
 
cur = conn.cursor() # automobilis, kuris vazines tuo greitkeliu
 
def sukurti_studentu_lentele():
    cur.execute("""
                CREATE TABLE IF NOT EXISTS "Students" (
        "id"    INTEGER NOT NULL UNIQUE,
        "name"  TEXT NOT NULL,
        "last_name" TEXT NOT NULL,
        "age"   INTEGER DEFAULT 19,
        PRIMARY KEY("id" AUTOINCREMENT)
    );
                """) # automobilio pakrovimas
    conn.commit()
 
sukurti_studentu_lentele()
 
def add_student(name,last_name,age):
    with conn:
        cur.execute(f"""Insert into Students(Name,last_name,age) values(?,?,?)""",(name,last_name,age))
        # Update Students Set Name = ?, last_name = ? ,(name,last_name)
        # """Insert into Students(Name,last_name,age) values('Justas' Delete From Students ','{last_name}',{age})"""# sql injection
 
 
vardas = input("Iveskite varda: ") # Justas', 'Delete From Database'
add_student(vardas,"Justaitis",30)
# with conn: # atitinka ir commit ir close viename
   
 
 
# kai jis baigiasi visas musu komandas sucommitina ir uzdaro greitkeli