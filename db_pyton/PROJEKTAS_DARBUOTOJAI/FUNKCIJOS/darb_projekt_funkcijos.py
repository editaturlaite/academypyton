from PROJEKTAS_DARBUOTOJAI.KITA.sesija import sukurti_sesija

Session = sukurti_sesija()
          
def perziureti_projektus (perziurimas_darbuotojas):

    with Session() as session:
        session.add(perziurimas_darbuotojas)

        print(f"""Darbuotojas: {perziurimas_darbuotojas.vardas} {perziurimas_darbuotojas.pavarde}
Priskirti projektai:""")
        
        if not perziurimas_darbuotojas.darbuotojo_projektai:
            print("Darbuotojas neturi priskirtu projektu")
            return

        for projektas in perziurimas_darbuotojas.darbuotojo_projektai:
            print(projektas.projektas.pavadinimas)

