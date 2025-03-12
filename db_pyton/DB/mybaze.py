import mysql.connector # import sqlite3
 
# Define connection parameters
config = {
    "host": "localhost", # kokiam kompiuteryje veikia. mano_serveris.com
    "user": "editat", # naudotojo vardas
    "password": "SniegasPavasary2025", # koks slaptazodis
    "database": "studentu_pav" # kokia duomenu baze (koks pavadinimas duomenu bazes)
} # zodynas su nustatymais
 
# Connect to MySQL
try:
    conn = mysql.connector.connect(**config) # greitkelio atidarymas
    cursor = conn.cursor() # sukuriam automobili
   
    # Test query
    # cursor.execute("SHOW TABLES") # pakraunam automobili
    # tables = cursor.fetchall() # gaunam automobilio parvezta rezultata
   
    # print("Tables in database:", tables)

    
   

   
except mysql.connector.Error as err:
    print("Error:", err)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS PROJEKTAS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    PAVADINIMAS VARCHAR(255) NOT NULL)""")

cur.execute("""INSERT IGNORE INTO PROJEKTAS (PAVADINIMAS) VALUES
('Izola'),
('Registrų Centras'),
('Kaunas')""")

cur.execute("""CREATE TABLE IF NOT EXISTS SKYRIUS (
    PAVADINIMAS VARCHAR(255) PRIMARY KEY,
    VADOVAS_ASMENSKODAS VARCHAR(255))
""")

cur.execute("""INSERT IGNORE INTO SKYRIUS (PAVADINIMAS, VADOVAS_ASMENSKODAS) VALUES
('Java', '48509141175'),
('Testavimo', '38804172782'),
('C#', '38904172782')""")

cur.execute("""CREATE TABLE IF NOT EXISTS DEPARTAMENTAS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    PAVADINIMAS VARCHAR(255) NOT NULL,
    SKYRIUS_PAVADINIMAS VARCHAR(255),
    FOREIGN KEY (SKYRIUS_PAVADINIMAS) REFERENCES SKYRIUS(PAVADINIMAS)
)""")

cur.execute("""INSERT IGNORE DEPARTAMENTAS (PAVADINIMAS, SKYRIUS_PAVADINIMAS) VALUES
('IT', 'Java'),
('QA', 'Testavimo'),
('Development', 'C#')""")

cur.execute("""CREATE TABLE IF NOT EXISTS DARBUOTOJAS (
    ASMENSKODAS CHAR(11) PRIMARY KEY,
    VARDAS VARCHAR(255) NOT NULL,
    PAVARDE VARCHAR(255) NOT NULL,
    DIRBANUO DATE NOT NULL,
    GIMIMOMETAI DATE NOT NULL,
    PAREIGOS VARCHAR(255),
    SKYRIUS_PAVADINIMAS VARCHAR(255),
    PROJEKTAS_ID INT,
    DEPARTAMENTAS_ID INt,
    FOREIGN KEY (SKYRIUS_PAVADINIMAS) REFERENCES SKYRIUS(PAVADINIMAS),
    FOREIGN KEY (PROJEKTAS_ID) REFERENCES PROJEKTAS(ID),
    FOREIGN KEY (DEPARTAMENTAS_ID) REFERENCES DEPARTAMENTAS(ID))
""")

query = """INSERT IGNORE INTO DARBUOTOJAS 
    (ASMENSKODAS, VARDAS, PAVARDE, DIRBANUO, GIMIMOMETAI, PAREIGOS, SKYRIUS_PAVADINIMAS, PROJEKTAS_ID, DEPARTAMENTAS_ID) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

data = [
    ('38101122335', 'Petras', 'Petraitis', '2009-10-30', '1981-01-11', 'Testuotojas', 'Testavimo', 1, 2),
    ('38010101234', 'Jonas', 'Jonaitis', '2007-05-30', '1980-10-10', 'Programuotojas', 'Java', 2, 1),
    ('38103201435', 'Rimas', 'Plekaitis', '2009-10-30', '1981-03-20', 'Programuotojas', 'Java', 3, 1),
    ('48509141175', 'Zita', 'Lietuvaitė', '2012-06-15', '1985-09-14', 'Projektų vadovė', 'Java', 2, 1),
    ('48410121275', 'Jurga', 'Jurgaityte', '2011-02-12', '1984-10-12', 'Programuotoja', 'C#', 1, 3),
    ('38807201234', 'Giedrius', 'Sabutis', '2009-01-21', '1988-07-20', 'Testuotojas', 'Testavimo', 2, 2),
    ('38807291234', 'Regimantas', 'Sabonis', '2013-01-21', '1988-07-29', 'Testuotojas', 'Testavimo', 3, 2),
    ('38609191234', 'Saulius', 'Sabonis', '2013-01-21', '1986-09-19', 'Testuotojas', 'Testavimo', 3, 2),
    ('38109197598', 'Justas', 'Sabonis', '2011-12-17', '1986-09-19', 'Testuotojas', 'Testavimo', 1, 2),
    ('38503142412', 'Jonas', 'Kalnas', '2009-05-11', '1985-03-24', 'Programuotojas', 'Java', 1, 1),
    ('39003142412', 'Stasys', 'Sakalas', '2009-05-11', '1990-03-24', 'Programuotojas', 'Java', 3, 1),
    ('37803142412', 'Povilas', 'Vakalas', '2012-11-11', '1978-03-14', 'Programuotojas', 'C#', 2, 3),
    ('38804172782', 'Deivydas', 'Piliukas', '2011-12-11', '1988-04-17', 'Projektų vadovas', 'Testavimo', 2, 2),
    ('38904172782', 'Kestas', 'Liutas', '2012-12-11', '1989-04-17', 'Projektų vadovas', 'C#', 1, 3),
    ('38901228523', 'Laikinas', 'Veikejas', '2009-01-22', '1989-01-22', None, None, None, None)
]

cur.executemany(query, data)
conn.commit()