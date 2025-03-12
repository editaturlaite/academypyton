from PROJEKTAS_DARBUOTOJAI.FUNKCIJOS.darbuotoju_funkcijos import prideti_darbuotoja, sukurti_nauja_darbuotoja, perziureti_darbuotojus,paieskos_pasirinktis,atnaujinamos_info_pasirinktis, istrinti_darbuotoja
from PROJEKTAS_DARBUOTOJAI.FUNKCIJOS.departamento_funkcijos import prideti_departamenta, sukurti_nauja_departamenta
from PROJEKTAS_DARBUOTOJAI.FUNKCIJOS.projektu_funkcijos import prideti_projekta, sukurti_nauja_projekta,ieskoti_projekto,priskirti_darbuotoja_projektui
from PROJEKTAS_DARBUOTOJAI.KITA.sesija import sukurti_sesija
from PROJEKTAS_DARBUOTOJAI.FUNKCIJOS.darb_projekt_funkcijos import perziureti_projektus
from PROJEKTAS_DARBUOTOJAI.FUNKCIJOS.departamento_funkcijos import departamento_paieska, perziureti_departamento_darbuotojus,ieskoti_departamento, priskirti_darbuotoja_departamentui,gauti_vadova_is_id

Session = sukurti_sesija()

def pagrindinis_meniu():
    try:
        pasirinktis =input("""Pasirinkite norima operacija ivesdami jos numeri:
                            1.Pridėti naują darbuotoją
                            2.Atvaizduoti visų darbuotojų sąrašą
                            3.Ieškoti darbuotojo
                            4.Atnaujinti darbuotojo informaciją
                            5.Ištrinti darbuotoją
                            6.Pridėti naują projektą
                            7.Priskirti darbuotoją projektui
                            8.Peržiūrėti darbuotojo projektus
                            9.Sukurti naują departamentą
                            10.Priskirti darbuotoją departamentui
                            11.Peržiūrėti departamento darbuotojus
                            12.Išeiti iš programos """)
        if not pasirinktis.isdigit():
            raise ValueError (f"Nieko neivedete arba ivedete ne skaiciu, bandykite dar karta.")
        
        pasirinktis = int(pasirinktis)

        if pasirinktis <1 or pasirinktis >12:
            raise ValueError (f"Tokio pasirinkimo nera, bandykite dar karta.")
        
        programos_pasirinkimas(pasirinktis)
        
    except ValueError as klaida:
        print(klaida)

def programos_pasirinkimas(pasirinkta_programa):
    try:

        match(pasirinkta_programa):
            case 1:
                print("Prideti nauja darbuotoja.")
                prideti_darbuotoja(sukurti_nauja_darbuotoja())
                print("Naujas darbuotojas sekmingai pridetas.")
            case 2:
                print("Visu darbuotoju sąrasas.")
                print(perziureti_darbuotojus())
            case 3:
                ieskomas_darbuotojas = paieskos_pasirinktis()
                if ieskomas_darbuotojas is None:
                    return
                print(f"Darbuotojo informacija:\n {ieskomas_darbuotojas}")
            case 4:
                print("Norint atnaujinti informacija. ")
                atnaujinamas_darbuotojas = paieskos_pasirinktis()
                if atnaujinamas_darbuotojas is None:
                    return
                atnaujinamos_info_pasirinktis(atnaujinamas_darbuotojas)
                print("Duomenys atnaujinti.")
            case 5:
                print("Norint istrinti darbuotojo informacija.")
                trinamas_darbuotojas = paieskos_pasirinktis()
                istrinti_darbuotoja(trinamas_darbuotojas)
                print("Duomenys istrinti.")
            case 6:
                print("Pridėti naują projektą.")
                naujas_projektas = sukurti_nauja_projekta()
                prideti_projekta(naujas_projektas)
                print("Projektas pridetas.")
            case 7:
                ieskomas_projektas = input("Iveskite pavadinima projekto, kuriam norite priskirti darbuotoja.: ")
                rastas_projektas = ieskoti_projekto(ieskomas_projektas)
                if rastas_projektas is None:
                    return
                print("Darbuotojo priskiriamo projektui paieska:")
                priskiriamas_darbuotojas = paieskos_pasirinktis()
                if priskiriamas_darbuotojas is None:
                    return
                darbuotojo_role = input("Nurodykite darbuotojo role projekte jei reikia, kitu atveju spauskite enter")
                priskirti_darbuotoja_projektui(rastas_projektas,priskiriamas_darbuotojas,darbuotojo_role)
                print("Projektas sekmingai priskirtas.")
            case 8:
                print("Peržiūrėti darbuotojo projektus.")
                ieskomas_darbuotojas = paieskos_pasirinktis()
                if ieskomas_darbuotojas is None:
                    return
                perziureti_projektus(ieskomas_darbuotojas)

            case 9:
                print("Sukurti naują departamentą.")
                naujas_departamentas = sukurti_nauja_departamenta()
                if naujas_departamentas is None:
                    return
                prideti_departamenta(naujas_departamentas)
                darbuotojas = gauti_vadova_is_id(naujas_departamentas)
                if darbuotojas is not None:
                    priskirti_darbuotoja_departamentui(naujas_departamentas,darbuotojas)
                print("Departamentas sukurtas.")

            case 10:
                print("Priskirti darbuotoją departamentui.")
                ieskomas_departamentas = input("Iveskite pavadinima departamento, kuriam norite priskirti darbuotoja.: ")
                rastas_departamentas = ieskoti_departamento(ieskomas_departamentas)
                if rastas_departamentas is None:
                    return
                print("Darbuotojo priskiriamo departamentui paieska:")
                priskiriamas_darbuotojas = paieskos_pasirinktis()
                if priskiriamas_darbuotojas is None:
                    return
                priskirti_darbuotoja_departamentui(rastas_departamentas,priskiriamas_darbuotojas)
                print("Departamentas sekmingai priskirtas.")
            case 11:
                perziurimas_departamentas = departamento_paieska()
                if perziurimas_departamentas is None:
                    print("Departamentas nerastas.")
                    return
                departamento_darbuotojai = perziureti_departamento_darbuotojus(perziurimas_departamentas)
                if departamento_darbuotojai is None:
                    print("Departamentas neturi priskirtu darbuotoju.")
                    return
            case 12:
                print("Programa baigta")
                exit()

    except Exception as klaida:
        print(f"Klaida: {klaida}")
