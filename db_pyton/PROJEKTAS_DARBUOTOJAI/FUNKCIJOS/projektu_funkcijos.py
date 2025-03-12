from sqlalchemy import create_engine, Column, Integer, String,select, or_, Date, DateTime, func
from PROJEKTAS_DARBUOTOJAI.KITA.klases import Projektas
from PROJEKTAS_DARBUOTOJAI.KITA.klases import DarbuotojasProjektas
from PROJEKTAS_DARBUOTOJAI.KITA.sesija import sukurti_sesija

Session = sukurti_sesija()

def sukurti_nauja_projekta():
    try:
        p_pavadinimas = input("Iveskite projekto pavadinima: ")
        if p_pavadinimas == "":
            raise ValueError
            return
        p_aprasymas = input("Iveskite projekto aprasyma: ")
        if p_aprasymas == "":
            raise ValueError
            return
        naujas_projektas = Projektas(pavadinimas=p_pavadinimas,aprasymas=p_aprasymas)
        return naujas_projektas
    except ValueError:
        print("Projekto pavadinimas ir aprasymas privalomas. Kurkite is naujo")

def prideti_projekta(pridedamas_projektas):
    with Session() as session:
        session.add(pridedamas_projektas)
        session.commit()

def ieskoti_projekto(ieskomas_pavadinimas):
    with Session() as session:
        stmt = select(Projektas).filter_by(pavadinimas = ieskomas_pavadinimas)
        rastas_projektas = session.execute(stmt).scalar_one_or_none()
        if rastas_projektas is None:
            print("Tokio projekto nera")
            return
        return rastas_projektas

def priskirti_darbuotoja_projektui(projektas,priskiriamas_darbuotojas,darbuotojo_role):
    with Session() as session:
        session.add(DarbuotojasProjektas(darbuotojas = priskiriamas_darbuotojas, projektas = projektas, role_projekte = darbuotojo_role))
        session.commit()

    