from sqlalchemy import create_engine, Column, Integer, String,select, or_, Date, DateTime, func, delete
from PROJEKTAS_DARBUOTOJAI.KITA.klases import Darbuotojas
from PROJEKTAS_DARBUOTOJAI.KITA.sesija import sukurti_sesija
import datetime
from PROJEKTAS_DARBUOTOJAI.KITA.klases import DarbuotojasProjektas

Session = sukurti_sesija()

def sukurti_nauja_darbuotoja():
            while True:
                i_vardas = input("Iveskite darbuotojo varda: ").strip()
                if i_vardas:
                    break
                print("Darbuotojo vardas privalomas")

            while True:
                i_pavarde = input("Iveskite darbuotojo pavarde: ").strip()
                if i_pavarde:
                    break
                print("Darbuotojo pavarde privaloma.")

            while True:
                i_gimimo_data = input("Iveskite darbuotojo gimimo data formatu yyyy-mm-dd: ").strip()
                if not i_gimimo_data:
                    print("Darbuotojo gimimo data privaloma.")
                    continue
                try:
                    konvertuota_gimimo_data = datetime.datetime.strptime(i_gimimo_data, '%Y-%m-%d')
                    break
                except ValueError:
                    print("Neteisingai ivesta data.Veskite data formatu: yyyy-mm-dd: ")

            while True:
                i_pareigos = input("Iveskite darbuotojo pareigas: ").strip()
                if i_pareigos:
                    break
                print("Darbuotojo pareigos privalomos.")
            
            while True:
                i_atlyginimas = input("Iveskite darbuotojo atlyginima: ").strip()
                if i_atlyginimas.isdigit():
                    i_atlyginimas = int(i_atlyginimas)
                    break
                print("Darbuotojo atlyginimas privalomas ir turi buti skaicius.")
                
            naujas_darbuotojas = Darbuotojas(vardas=i_vardas,pavarde=i_pavarde,gimimo_data=konvertuota_gimimo_data.date(),pareigos=i_pareigos,atlyginimas=i_atlyginimas)
            return naujas_darbuotojas

def prideti_darbuotoja(pridedamas_darbuotojas):
    with Session() as session:
        session.add(pridedamas_darbuotojas)
        session.commit()
      
def perziureti_darbuotojus():
    with Session() as session:
        stmt = select(Darbuotojas)
        darbuotojai = session.execute(stmt).scalars().all()
    if darbuotojai == []:
        print("Nera ivestu darbuotoju.")
        return
    for darbuotojas in darbuotojai:
        print (darbuotojas)

def paieskos_pasirinktis():
    while True:
        pasirinktis = input("""Pasirinkite buda kaip norite ieskoti darbuotojo, ivesdami numeri:
        1.Ieskoti pagal darbuotojo ID
        2. Ieskoti pagal darbuotojo varda
        3. Ieskoti pagal darbuotojo pavarde
                                :""")
        if not pasirinktis.isdigit():
            print("Ivedete ne skaiciu arba nieko neivedete.")
            continue
        
        pasirinktis = int(pasirinktis)

        if pasirinktis <1 or pasirinktis > 3:
            print("Tokios pasirinkties nera. Bandykita dar karta.")
            continue
        
        elif pasirinktis == 1:
            try:
                ieskomas_id = int(input("Iveskite ieskomo darbuotojo ID: "))
                rastas_darbuotojas = (ieskoti_darbuotojo_id(ieskomas_id))
                if rastas_darbuotojas is None:
                    print("Darbuotojas nerastas duomenu bazeje.")
                return rastas_darbuotojas
            except ValueError:
                print("Nieko neivedete arba ivedete ne skaiciu.")

        elif pasirinktis == 2:
            try:
                ieskomas_vardas = input("Iveskite varda: ")
                if ieskomas_vardas == "":
                    raise ValueError
                rastas_darbuotojas = (ieskoti_darbuotojo_vardas(ieskomas_vardas))
                if rastas_darbuotojas is None:
                    print("Darbuotojas nerastas duomenu bazeje.")
                return rastas_darbuotojas
            except ValueError:
                print("Nieko neivedete.")
            
        elif pasirinktis == 3:
            try:
                ieskoma_pavarde = input("Iveskite pavarde: ")
                if ieskoma_pavarde == "":
                    raise ValueError
                rastas_darbuotojas = (ieskoti_darbuotojo_pavarde(ieskoma_pavarde))
                if rastas_darbuotojas is None:
                    print("Darbuotojas nerastas duomenu bazeje.")
                return rastas_darbuotojas
            except ValueError:
                print("Nieko neivedete.")

def ieskoti_darbuotojo_vardas(ieskoti_vardo):
    with Session() as session:
        stmt = select(Darbuotojas).filter_by(vardas = ieskoti_vardo)
        rastas_darbuotojas = session.execute(stmt).scalar_one_or_none()
        return rastas_darbuotojas

def ieskoti_darbuotojo_pavarde(ieskoti_pavardes):
    with Session() as session:
        stmt = select(Darbuotojas).filter_by(pavarde = ieskoti_pavardes)
        rastas_darbuotojas = session.execute(stmt).scalar_one_or_none()
        return rastas_darbuotojas
    
def ieskoti_darbuotojo_id(ieskoti_id):
    with Session() as session:
        rastas_darbuotojas = session.get(Darbuotojas,ieskoti_id)
        return rastas_darbuotojas
        
def atnaujinamos_info_pasirinktis(atnaujinamas_darbuotuojas):
    while True:
        pasirinktis = input("""Pasirinkite kokia informacija norite atnaujinti, ivesdami numeri.
        1. Atnaujinti pareigas
        2. Atnaujinti atlyginima
                                :""")
        if not pasirinktis.isdigit() or pasirinktis not in ['1','2']:
            print("Pasirinkote neegzistuojanti operacijos numeri. Bandykite dar karta.")
            continue

        if pasirinktis == '1':
            naujos_pareigos = input("Iveskite naujas pareigas: ")
            atnaujinti_pareigas(atnaujinamas_darbuotuojas,naujos_pareigos)   
            break

        elif pasirinktis == '2':
            naujas_atlyginimas = int(input("Iveskite nauja atlyginima: "))
            atnaujinti_atlyginima(atnaujinamas_darbuotuojas,naujas_atlyginimas)
            break

def atnaujinti_pareigas(atnaujinamas_darbuotojas,naujos_pareigos):
    with Session() as session:
        atnaujinamas_darbuotojas.pareigos = naujos_pareigos
        session.add(atnaujinamas_darbuotojas)
        session.commit()

def atnaujinti_atlyginima(atnaujinamas_darbuotojas,naujas_atlyginimas):
    with Session() as session:
        atnaujinamas_darbuotojas.atlyginimas = naujas_atlyginimas
        session.add(atnaujinamas_darbuotojas)
        session.commit()

def istrinti_darbuotoja(norimas_istrinti):
    with Session() as session:
        session.execute(delete(DarbuotojasProjektas).where(DarbuotojasProjektas.darbuotojas_id == norimas_istrinti.id))
        session.delete(norimas_istrinti)
        session.commit()