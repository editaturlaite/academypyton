from sqlalchemy import create_engine, Column, Integer, String,select, or_, Date, DateTime, func
from PROJEKTAS_DARBUOTOJAI.KITA.klases import Departamentas
from PROJEKTAS_DARBUOTOJAI.KITA.sesija import sukurti_sesija
from PROJEKTAS_DARBUOTOJAI.FUNKCIJOS.darbuotoju_funkcijos import paieskos_pasirinktis
from PROJEKTAS_DARBUOTOJAI.KITA.klases import Darbuotojas

Session = sukurti_sesija()

def vadovo_priskyrimo_pasirinktis ():
    klaidinga_pasirinktis = True
    while klaidinga_pasirinktis:
        try:
            pasirinktis = input("""Ar norite priskirti vadova departamentui? pasirinkite norima operacija ivesdami jos numeri:
                        1. Priskirti vadova.
                        2. Neskirti vadovo.
                        :""")
            if not pasirinktis.isdigit() or pasirinktis == "":
                raise ValueError (f"Ivedete ne skaiciu arba nieko neivedete")
            
            pasirinktis = int(pasirinktis)

            if pasirinktis <1 or pasirinktis >2:
                print("Tokios operacijos nera.")
                return
            elif pasirinktis == 1: 
                klaidinga_pasirinktis = False
                return True
            elif pasirinktis == 2:
                klaidinga_pasirinktis = False
                return False
            
        except ValueError as klaida:
            print(klaida)

def sukurti_nauja_departamenta():
    try:
        d_pavadinimas = input("Iveskite departamento pavadinima: ")
        if d_pavadinimas == "":
            raise ValueError
        priskirti_vadova = vadovo_priskyrimo_pasirinktis()
        if priskirti_vadova == True:
            print("Raskite darbuotoja kuri norite priskirti departamento vadovu.")
            departamento_vadovas = paieskos_pasirinktis()
            naujas_departamentas = Departamentas(pavadinimas=d_pavadinimas, vadovas_id=departamento_vadovas.id)
            return naujas_departamentas
        elif priskirti_vadova == False:
            naujas_departamentas = Departamentas(pavadinimas=d_pavadinimas)
            return naujas_departamentas
    except ValueError:
        print("Departamento pavadinimas yra privalomas.")
        return


def prideti_departamenta(pridedamas_departamentas):
    with Session() as session:
        session.add(pridedamas_departamentas)
        session.commit()
        session.refresh(pridedamas_departamentas)
        return pridedamas_departamentas

def departamento_paieska():  
    ieskomas_departamentas = input("Iveskite pavadinima departamento kurio darbuotojus norite perziureti:")
    with Session() as session:
        stmt = select(Departamentas).filter_by(pavadinimas = ieskomas_departamentas)
        rastas_departamentas = session.execute(stmt).scalar_one_or_none()
        if rastas_departamentas is None:
            print("Departamentas nerastas.")
            return
        return rastas_departamentas

def perziureti_departamento_darbuotojus (perziurimas_departamentas):
    with Session() as session:
        session.add(perziurimas_departamentas)
        print(f"""Departamentas: {perziurimas_departamentas.pavadinimas}
Departamento darbuotojai:""")
        for darbuotojas in perziurimas_departamentas.darbuotojai:
            print(f"{darbuotojas.vardas} {darbuotojas.pavarde}")

def ieskoti_departamento(ieskomas_pavadinimas):
    with Session() as session:
        stmt = select(Departamentas).filter_by(pavadinimas = ieskomas_pavadinimas)
        rastas_departamentas = session.execute(stmt).scalar_one_or_none()
        if rastas_departamentas is None:
            return
        return rastas_departamentas

def priskirti_darbuotoja_departamentui(priskiriamas_departamentas,priskiriamas_darbuotojas):
    with Session() as session:
       session.add(priskiriamas_darbuotojas)
       priskiriamas_darbuotojas.departamentas = priskiriamas_departamentas
       session.commit()

def gauti_vadova_is_id(pridetas_departamentas):
    with Session() as session:
        vadovas = session.get(Darbuotojas,pridetas_departamentas.vadovas_id)
        return vadovas