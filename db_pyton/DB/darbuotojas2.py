import sqlite3

conn =sqlite3.connect(r'C:\\Users\\Vartotojas\\Desktop\\Code Academy\\academypyton\\db_pyton\\darbuotojas2_pyton.db')

cur = conn.cursor()

# cur.executescript("""
# -- Create PROJEKTAS table
# CREATE TABLE IF NOT EXISTS PROJEKTAS (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     PAVADINIMAS VARCHAR(255) NOT NULL
# );

# INSERT INTO PROJEKTAS (PAVADINIMAS) VALUES
# ('Izola'),
# ('Registrų Centras'),
# ('Kaunas');

# -- Create SKYRIUS table with PRIMARY KEY
# CREATE TABLE IF NOT EXISTS SKYRIUS (
#     PAVADINIMAS VARCHAR(255) PRIMARY KEY,
#     VADOVAS_ASMENSKODAS VARCHAR(255)
# );

# INSERT INTO SKYRIUS (PAVADINIMAS, VADOVAS_ASMENSKODAS) VALUES
# ('Java', '48509141175'),
# ('Testavimo', '38804172782'),
# ('C#', '38904172782');

# -- Create DEPARTAMENTAS table
# CREATE TABLE IF NOT EXISTS DEPARTAMENTAS (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     PAVADINIMAS VARCHAR(255) NOT NULL,
#     SKYRIUS_PAVADINIMAS VARCHAR(255),
#     FOREIGN KEY (SKYRIUS_PAVADINIMAS) REFERENCES SKYRIUS(PAVADINIMAS)
# );

# INSERT INTO DEPARTAMENTAS (PAVADINIMAS, SKYRIUS_PAVADINIMAS) VALUES
# ('IT', 'Java'),
# ('QA', 'Testavimo'),
# ('Development', 'C#');

# -- Create DARBUOTOJAS table
# CREATE TABLE IF NOT EXISTS DARBUOTOJAS (
#     ASMENSKODAS CHAR(11) PRIMARY KEY,
#     VARDAS VARCHAR(255) NOT NULL,
#     PAVARDE VARCHAR(255) NOT NULL,
#     DIRBANUO DATE NOT NULL,
#     GIMIMOMETAI DATE NOT NULL,
#     PAREIGOS VARCHAR(255),
#     SKYRIUS_PAVADINIMAS VARCHAR(255),
#     PROJEKTAS_ID INTEGER,
#     DEPARTAMENTAS_ID INTEGER,
#     FOREIGN KEY (SKYRIUS_PAVADINIMAS) REFERENCES SKYRIUS(PAVADINIMAS),
#     FOREIGN KEY (PROJEKTAS_ID) REFERENCES PROJEKTAS(ID),
#     FOREIGN KEY (DEPARTAMENTAS_ID) REFERENCES DEPARTAMENTAS(ID)
# );

# INSERT INTO DARBUOTOJAS (ASMENSKODAS, VARDAS, PAVARDE, DIRBANUO, GIMIMOMETAI, PAREIGOS, SKYRIUS_PAVADINIMAS, PROJEKTAS_ID, DEPARTAMENTAS_ID) VALUES
# ('38101122335', 'Petras', 'Petraitis', '2009-10-30', '1981-01-11', 'Testuotojas', 'Testavimo', 1, 2),
# ('38010101234', 'Jonas', 'Jonaitis', '2007-05-30', '1980-10-10', 'Programuotojas', 'Java', 2, 1),
# ('38103201435', 'Rimas', 'Plekaitis', '2009-10-30', '1981-03-20', 'Programuotojas', 'Java', 3, 1),
# ('48509141175', 'Zita', 'Lietuvaitė', '2012-06-15', '1985-09-14', 'Projektų vadovė', 'Java', 2, 1),
# ('48410121275', 'Jurga', 'Jurgaityte', '2011-02-12', '1984-10-12', 'Programuotoja', 'C#', 1, 3),
# ('38807201234', 'Giedrius', 'Sabutis', '2009-01-21', '1988-07-20', 'Testuotojas', 'Testavimo', 2, 2),
# ('38807291234', 'Regimantas', 'Sabonis', '2013-01-21', '1988-07-29', 'Testuotojas', 'Testavimo', 3, 2),
# ('38609191234', 'Saulius', 'Sabonis', '2013-01-21', '1986-09-19', 'Testuotojas', 'Testavimo', 3, 2),
# ('38109197598', 'Justas', 'Sabonis', '2011-12-17', '1986-09-19', 'Testuotojas', 'Testavimo', 1, 2),
# ('38503142412', 'Jonas', 'Kalnas', '2009-05-11', '1985-03-24', 'Programuotojas', 'Java', 1, 1),
# ('39003142412', 'Stasys', 'Sakalas', '2009-05-11', '1990-03-24', 'Programuotojas', 'Java', 3, 1),
# ('37803142412', 'Povilas', 'Vakalas', '2012-11-11', '1978-03-14', 'Programuotojas', 'C#', 2, 3),
# ('38804172782', 'Deivydas', 'Piliukas', '2011-12-11', '1988-04-17', 'Projektų vadovas', 'Testavimo', 2, 2),
# ('38904172782', 'Kestas', 'Liutas', '2012-12-11', '1989-04-17', 'Projektų vadovas', 'C#', 1, 3),
# ('38901228523', 'Laikinas', 'Veikejas', '2009-01-22', '1989-01-22', NULL, NULL, NULL, NULL);
# """)

# conn.commit()

# cur.execute("SELECT COUNT(*) FROM DARBUOTOJAS")
# print("✅ Įrašų kiekis:", cur.fetchone()[0])

# ------------------------------------------------------------------------------------------------------------------------------------------

# −1.Išrinkite duomenis apie darbuotoją (asmens kodą, vardą ir pavarde) iš lentelės DARBUOTOJAS kurie būtų gimę 1988m liepos 20d.

# def isrinkti_viena_pagal_data():
#     with conn:
#         cur.execute("select asmenskodas,vardas,pavarde from darbuotojas where gimimometai = '1988-07-20'")
#         isrinkta = cur.fetchall()
#         return isrinkta
# print(isrinkti_viena_pagal_data())

# −2.Išrinkite visus duomenis apie darbuotojus  iš lentelės DARBUOTOJAS, kurie yra gimę iki 1988m liepos 29d

# def isrinkti_visus_pagal_data():
#     with conn:
#         cur.execute("select * from darbuotojas where gimimometai <'1988-07-29'")
#         isrinkta = cur.fetchall()
#         return isrinkta
# print(isrinkti_visus_pagal_data())

# 3.Išrinkite duomenis apie darbuotojus(dirba nuo kada ir gimimo metus) 
# iš lentelės DARBUOTOJAS, kurie būtų įsidarbinę nuo 2009m spalio 30d iki 2012m lapkričio 11d.

# def isrinkti_pagal_isidarbinima():
#     with conn:
#         cur.execute("select dirbanuo, gimimometai from darbuotojas where dirbanuo between '2009-10-30' and '2012-11-11'")
#         isrinkta = cur.fetchall()
#         return isrinkta
# print(isrinkti_pagal_isidarbinima())

# −4.Išrinkite duomenis apie darbuotojus (vardą, Skyrių ir Projekto ID)
# iš lentelės DARBUOTOJAS kurie dirba 2 ir 3 projektuose. (Panaudoti IN operatorių).

# def isrinkti_su_in():
#     with conn:
#         cur.execute("""select vardas, skyrius_pavadinimas, projektas_id from darbuotojas
#                      where projektas_id in (2,3)""")
#         pateiktis = cur.fetchall()
#         return pateiktis
# print(isrinkti_su_in())

# −5.Išrinkite duomenis (vardą, pavarde ir asmens kodą) apie visas moteris iš lentelės DARBUOTOJAS (panaudojant operatorių LIKE).

# def isrinkti_moteris():
#     with conn:
#         cur.execute("select vardas, pavarde, asmenskodas from darbuotojas where asmenskodas like '4%'")
#         pateiktis = cur.fetchall()
#         return pateiktis
# print(isrinkti_moteris())

# 6.Išrinkite visus duomenis apie visus darbuotojus iš lentelės DARBUOTOJAS,  kurie yra gimę 12 diena (panaudojant operatorių LIKE).

# def isrinkti_visus_diena():
#     with conn:
#         cur.execute("select * from darbuotojas where gimimometai like '%12'")
#         pateiktis = cur.fetchall()
#         return pateiktis
# print(isrinkti_visus_diena())

# −7.išrinkite visus projektus iš lentelės PROJEKTAS kad projekto pavadinime 3 raidė būtų ‘u’.

# def isrinkti_3u():
#     with conn:
#         cur.execute("select * from projektas where pavadinimas like '__u%'")
#         pateiktis = cur.fetchall()
#         return pateiktis
# print(isrinkti_3u())

# ----------------------------------------------------------------------------------------------------------------------------

# −8.Išrinkite visus darbuotojus iš lentelės DARBUOTOJAS, kuriems nepaskirtos jokios pareigos.

# def isrinkti_be_pareigu():
#     with conn:
#         cur.execute("select * from darbuotojas where pareigos is null")
#         pateiktis = cur.fetchall()
#         return pateiktis
# print(isrinkti_be_pareigu())

# −9.Išrinkite duomenis apie darbuotoją (vardą, pavardę, nuo kada dirba ir pareigas)
# kad tenkintų sąlygas: (dirba nuo 2011-02-12 ir jų pareigos yra Programuotojai).

# def isrinkti_pagal_salyga():
#     with conn:
#         cur.execute("select vardas, pavarde, dirbanuo, pareigos from darbuotojas where dirbanuo >= '2011-02-12' and pareigos = 'programuotojas'")
#         pateiktis = cur.fetchall()
#         return pateiktis
# print(isrinkti_pagal_salyga())

# −10.Išrinkite duomenis apie darbuotojus (vardą, pavardę, skyriaus pavadinimą ir projekto ID) 
# iš lentelės DARBUOTOJAS su sąlyga, kad jie butų iš Java skyriaus arba 1 projekto.

# def isrinkti_su_or():
#     with conn:
#         cur.execute("""select vardas, pavarde, skyrius_pavadinimas, projektas_id from darbuotojas
#                      where skyrius_pavadinimas = 'java' or projektas_id = '1'""")
#         pateiktis = cur.fetchall()
#         return pateiktis
# print(isrinkti_su_or())

# −11.Išrinkite visus darbuotojų vardus išskyrus tuos, kurių vardai prasideda raide ‘S’ .

# def isrinkti_vardus():
#     with conn:
#         cur.execute("select vardas from darbuotojas where vardas not like 's%'")
#         pateiktis = cur.fetchall()
#         return pateiktis
# print(isrinkti_vardus())

# −12.Išrinkite duomenis ( vardą, dirba nuo kada ir gimimo metus)  iš lentelės “DARBUOTOJAS”,
# apie visus darbuotojus tik ne tuos, kurie įsidarbino  nuo 2009m spalio 30d iki 2012m lapkričio 11d.

# def isrinkti_duomenis():
#     with conn:
#         cur.execute("""select vardas, dirbanuo, gimimometai from darbuotojas 
#                     where dirbanuo not between '2009-10-30' and '2012-11-11' """)
#         pateiktis = cur.fetchall()
#         return pateiktis
# print(isrinkti_duomenis())

# −13.Išrinkite duomenis apie darbuotojus (vardą, pavardę ir gimimo metus)
# iš lentelės DARBUOTOJAS ir išrikiuokite visus duomenis nuo seniausio žmogaus iki jauniausio.

# def isrinkti_nuo_seniausio():
#     with conn:
#         cur.execute("""select vardas, pavarde, gimimometai from darbuotojas order by gimimometai """)
#         pateiktis = cur.fetchall()
#         return pateiktis
# print(isrinkti_nuo_seniausio())

# −14.Išrinkite duomenis apie darbuotojus (vardą, pavardę ir gimimo metus)
# iš lentelės DARBUOTOJAS ir išrikiuokite visus duomenis nuo jauniausio žmogaus iki seniausio.

# def isrinkti_nuo_jauniausio():
#     with conn:
#         cur.execute("""select vardas, pavarde, gimimometai from darbuotojas order by gimimometai desc """)
#         pateiktis = cur.fetchall()
#         return pateiktis
# print(isrinkti_nuo_jauniausio())


