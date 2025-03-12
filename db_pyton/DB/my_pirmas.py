import mysql.connector 

config = {
    "host": "localhost", # kokiam kompiuteryje veikia. mano_serveris.com
    "user": "editat", # naudotojo vardas
    "password": "SniegasPavasary2025", # koks slaptazodis
    "database": "darbuotojai2" # kokia duomenu baze (koks pavadinimas duomenu bazes)
}

conn = mysql.connector.connect(**config) # greitkelio atidarymas
cur = conn.cursor()


cur.execute("SHOW TABLES") # pakraunam automobili
tables = cur.fetchall() # gaunam automobilio parvezta rezultata
   
print("Tables in database:", tables)


#A. Išrinkite išsamią darbuotojų informaciją, įskaitant EMAIL, SALARY, departamentą, projektą ir kliento duomenis.

# cur.execute("""select darbuotojas.vardas, darbuotojas.pavarde, darbuotojas.pareigos, departamentas.pavadinimas, projektas.pavadinimas,
#              klientas.pavadinimas, darbuotojas.email, darbuotojas.salary from darbuotojas
#             join departamentas on darbuotojas.departamentas_id = departamentas.id
#             join projektas on darbuotojas.projektas_id = projektas.id
#             join klientas on projektas.klientas_id = klientas.id""")
# pateiktis = cur.fetchall()
# for eilute in pateiktis:
#     print(eilute)

# B. Išvardinkite visus projektus su jų pradžios data (START_DATE), pabaigos data (END_DATE) ir atitinkamu kliento pavadinimu.

# cur.execute("""select projektas.pavadinimas, projektas.start_date, projektas.end_date, klientas.pavadinimas from projektas
#             join klientas on projektas.klientas_id = klientas.id""")
# pateiktis = cur.fetchall()
# for eilute in pateiktis:
#     print(eilute)

#C. Suskaičiuokite bendrą darbuotojų skaičių kiekviename skyriuje.

# cur.execute("""select darbuotojas.skyrius_pavadinimas, count(asmenskodas) as darbuotoju_skaicius from darbuotojas
#             group by darbuotojas.skyrius_pavadinimas""")
# pateiktis = cur.fetchall()
# for eilute in pateiktis:
#     print(eilute)

#D. Suraskite didžiausią atlyginimą kiekviename departamente naudojant GROUP BY.

# cur.execute("""select departamentas.pavadinimas, max(salary) as didziausias_atlyginimas from darbuotojas
#             join departamentas on darbuotojas.departamentas_id = departamentas.id
#             group by departamentas.pavadinimas""")
# pateiktis = cur.fetchall()
# for eilute in pateiktis:
#     print(eilute)

#E. Išrinkite darbuotojus, įsidarbinusius nuo '2010-01-01' iki '2012-12-31', kurių atlyginimas viršija 700.

# cur.execute("""select vardas, pavarde, dirbanuo, salary from darbuotojas
#             where dirbanuo between '2010-01-01' and '2012-12-31' and salary > '700' """)
# pateiktis = cur.fetchall()
# for eilute in pateiktis:
#     print(eilute)

# F. Išrinkite departamentų pavadinimus ir jų darbuotojų skaičių, 
# rodant tik tuos departamentus, kuriuose darbuotojų skaičius yra didesnis už 1.

# cur.execute("""select departamentas.pavadinimas, count(asmenskodas) as darbuotoju_skaicius from darbuotojas
#             join departamentas on darbuotojas.departamentas_id = departamentas.id
#             group by departamentas.pavadinimas
#             having darbuotoju_skaicius >1 """)
# pateiktis = cur.fetchall()
# for eilute in pateiktis:
#     print(eilute)

#G. Naudodami LEFT JOIN ir GROUP_CONCAT, išvardinkite visus projektus kartu su priskirtų darbuotojų vardais ir pavardėmis.

# cur.execute("""select projektas.pavadinimas, group_concat(darbuotojas.vardas, darbuotojas.pavarde) from darbuotojas
#             left join projektas on darbuotojas.projektas_id = projektas.id
#             group by projektas.pavadinimas """)
# pateiktis = cur.fetchall()
# for eilute in pateiktis:
#     print(eilute)