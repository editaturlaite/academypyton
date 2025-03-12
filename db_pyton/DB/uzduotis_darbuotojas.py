import sqlite3

conn =sqlite3.connect(r'C:\\Users\\Vartotojas\\Desktop\\Code Academy\\academypyton\\db_pyton\\uzdaviniai_1paskaita_pyton.db')

cur = conn.cursor()

with conn:
    cur.execute("""
INSERT OR REPLACE INTO DARBUOTOJAS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ASMENSKODAS TEXT UNIQUE NOT NULL,
    VARDAS TEXT NOT NULL,
    PAVARDE TEXT NOT NULL,
    DIRBANUO TEXT NOT NULL,
    GIMIMOMETAI TEXT NOT NULL,
    PAREIGOS TEXT,
    SKYRIUS_PAVADINIMAS TEXT,
    PROJEKTAS_ID INTEGER,
    DEPARTAMENTAS_ID INTEGER
);
""")

darbuotojai = [
    ('38101122335', 'Petras', 'Petraitis', '2009-10-30', '1981-01-11', 'Testuotojas', 'Testavimo', 1, 2),
    ('38010101234', 'Jonas', 'Jonaitis', '2007-05-30', '1980-10-10', 'Programuotojas', 'Java', 2, 1),
    ('38103201435', 'Rimas', 'Plekaitis', '2009-10-30', '1981-03-20', 'Programuotojas', 'Java', 3, 1),
    ('48509141175', 'Zita', 'Lietuvaitė', '2012-06-15', '1985-09-14', 'Projektų vadovė', 'Java', 2, 1),
    ('48410121275', 'Jurga', 'Jurgaityte', '2011-02-12', '1984-10-12', 'Programuotoja', 'C#', 1, 3),
    ('38807201234', 'Giedrius', 'Sabutis', '2009-01-21', '1988-07-20', 'Testuotojas', 'Testavimo', 2, 2),
    ('38807291234', 'Regimantas', 'Sabonis', '2013-01-21', '1988-07-29', 'Testuotojas', 'Testavimo', 3, 2),
    ('38609191234', 'Saulius', 'Sabonis', '2013-01-21', '1986-09-19', 'Testuotojas', 'Testavimo', 3, 2),
    ('38109197598', 'Justas', 'Sabonis', '2011-12-17', '1986-09-19', 'Testuotojas', 'Testavimo', 1, 2),
    ('38904172782', 'Kestas', 'Liutas', '2012-12-11', '1989-04-17', 'Projektų vadovas', 'C#', 1, 3),
    ('38901228523', 'Laikinas', 'Veikejas', '2009-01-22', '1989-01-22', None, None, None, None)
]
cur.executemany("""
    INSERT OR IGNORE INTO DARBUOTOJAS (ASMENSKODAS, VARDAS, PAVARDE, DIRBANUO, GIMIMOMETAI, PAREIGOS, SKYRIUS_PAVADINIMAS, PROJEKTAS_ID, DEPARTAMENTAS_ID)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
""", darbuotojai)

-----------------------------------------------------------------------------------------------------------------------------------------------

def rodyti_viska():
    with conn:
        # 1.Išrinkite visus duomenis iš lentelės “DARBUOTOJAI”.
        cur = conn.cursor()
        cur.execute("""select * from darbuotojas""")
        rezultatai = cur.fetchall()
        for eilute in rezultatai:
            print(eilute)
rodyti_viska()

def rodyti_gimimo_data():
    #2.Išrinkite visus duomenis iš stulpelio “GIMIMO_DATA” - lentelėje “DARBUOTOJAS”.
    with conn:
        cur =conn.cursor()
        cur.execute("""select gimimometai from darbuotojas""")
        rezultatai = cur.fetchall()
        for eilute in rezultatai:
            print(eilute)
rodyti_gimimo_data()

def ideti_darbuotoja_daline_info():
    # 11.Įterpkite į lentelę “DARBUOTOJAI” naują darbuotoją, užpildydami tik laukus 
# (asmens_kodas, vardą, pavardę, gimimo metus). Pareigas ir skyriaus pavadinimą palikite neužpildytus.
    with conn:
        cur = conn.cursor()
        cur.execute("""insert into darbuotojas (asmenskodas,vardas,pavarde,gimimometai)
                values ('45689712565','Ruta','Rimkute','1978-12-10')""")
        cur.execute("""insert into darbuotojas (asmenskodas,vardas,pavarde,gimimometai)
                values ('45689712566','Edita','Rimkute','1978-12-10')""")
        cur.execute("""insert into darbuotojas (asmenskodas,vardas,pavarde,gimimometai)
                values ('45689712576','Egle','Rimkute','1978-12-10')""")
        conn.commit()
ideti_darbuotoja_daline_info()

def ideti_darbuotoja_daline_info(asmenskodas,vardas,pavarde,gimimometai):
    # 11.Įterpkite į lentelę “DARBUOTOJAI” naują darbuotoją, užpildydami tik laukus 
# (asmens_kodas, vardą, pavardę, gimimo metus). Pareigas ir skyriaus pavadinimą palikite neužpildytus.
    with conn:
        cur = conn.cursor()
        cur.execute("""insert into darbuotojas (asmenskodas,vardas,pavarde,gimimometai)
                values (?,?,?,?)""",(asmenskodas,vardas,pavarde,gimimometai))
        conn.commit()
        
ideti_darbuotoja_daline_info('4589712576','Monika','Rimkute','1978-12-10')

def istrinti_pagal_metus(metai):
    with conn:
    # 13.Ištrinkite lentelės “DARBUOTOJAI” įrašą, kurio gimimo data yra tokia, kurią jūs sukūrėte.
        cur =conn.cursor()
        cur.execute("delete from darbuotojas where gimimometai=?",(metai,))
        conn.commit
istrinti_pagal_metus("1978-12-10")
    

# 2 UZDUOTIS---------------------------------------------------------------------------------------------------------------------

# •Sukurti programą, kuri:
# •Sukurtų duomenų bazę
# •Sukurtų lentelę paskaitos su stulpeliais pavadinimas, destytojas ir trukme
# •Sukurtų tris paskaitas: ('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80) ir ('Java', 'Tomas', 80)
# •Atspausdintų tik tas paskaitas, kurių trukmė didesnė už 50
# •Atnaujintų paskaitos „Python“ pavadinimą į „Python programavimas“
# •Ištrintų paskaitą, kurios dėstytojas – „Tomas“
# •Atspausdintų visas paskaitas (visą lentelę)

conn =sqlite3.connect("uzduotis2.db")

cur = conn.cursor()

def sukurti_lentele():
    with conn:
        cur.execute("""create table if not exists paskaitos (id integer primary key autoincrement,pavadinimas text unique not null,
                    destytojas text not null, trukme integer not null)""")
        conn.commit() #kada reikia?

def sukurti_paskaitas(iterpiamos_paskaitos):
    with conn:
        cur.executemany("""insert into paskaitos (pavadinimas,destytojas,trukme)
                    values (?,?,?)""",iterpiamos_paskaitos)

def ieskoti_pagal_laika():
    with conn:
        cur.execute("select * from paskaitos where trukme >50")
        isvestis = cur.fetchall()
    return isvestis

def atnaujinti_pavadinima(senas_pav,naujas_pav):
    with conn:
        cur.execute("update paskaitos set pavadinimas = ? where pavadinimas = ?",(naujas_pav,senas_pav))

def istrinti_paskaita(trinama_atitiktis):
    with conn:
        cur.execute("delete from paskaitos where destytojas = ?",trinama_atitiktis)

def rodyti_viska():
    with conn:
        cur.execute("select * from paskaitos")
        paskaitos = cur.fetchall()

    return paskaitos

# --------------------------------------------------------------------------------------------------------------------------------------------

sukurti_lentele()

paskaitos = [('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80),('Java', 'Tomas', 80)]
sukurti_paskaitas(paskaitos)

print(ieskoti_pagal_laika())

pavadinimas = 'Python'
atnaujintas_pavadinimas = 'Python programavimas'
atnaujinti_pavadinima(pavadinimas,atnaujintas_pavadinimas)

destytojas = ('Tomas',)
istrinti_paskaita(destytojas)

print(rodyti_viska())






