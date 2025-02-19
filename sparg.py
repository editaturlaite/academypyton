def prideti_knyga(knygos):
    pavadinimas = input("Įveskite knygos pavadinimą: ").capitalize()
    autorius = input("Įveskite knygos autorių: ").title()
    while True:
        try:
            metai = int(input("Įveskite knygos leidimo metus: "))
            break
        except ValueError:
            print("Klaida: Metai turi būti sveikasis skaičius.")
    zanras = input("Įveskite knygos žanrą: ").lower()
    leidykla = input("Įveskite leidyklą: ").capitalize()
    knygos.append({"pavadinimas": pavadinimas, "autorius": autorius, "metai": metai, "zanras": zanras, "leidykla": leidykla})
    print("Knyga sėkmingai pridėta!")
 
def atvaizduoti_knygas(knygos):
    if not knygos:
        print("Knygų sąrašas tuščias.")
    else:
        indeksas = 1
        for knyga in knygos:
            print(f"{indeksas}. Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}, Metai: {knyga['metai']}, Žanras: {knyga['zanras']}, Leidykla: {knyga['leidykla']}")
            indeksas += 1
 
def ieskoti_knygos(knygos):
    paieska = input("Įveskite ieškomos knygos pavadinimą arba autorių): ")
    rasti = [knyga for knyga in knygos if paieska.lower() in knyga['pavadinimas'].lower() or paieska.lower() in knyga['autorius'].lower()]
    if not rasti:
        print("Knygos nerasta.")
    else:
        for knyga in rasti:
            print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}, Metai: {knyga['metai']}, Žanras: {knyga['zanras']}, Leidykla: {knyga['leidykla']}")
 
def istrinti_knyga(knygos):
    identifikatorius = input("Įveskite knygos numerį arba pavadinimą, kurią norite ištrinti: ")
    try:
        # Bandome interpretuoti įvestį kaip numerį
        numeris = int(identifikatorius) - 1
        if 0 <= numeris < len(knygos):
            istrinta_knyga = knygos.pop(numeris)
            print(f"Knyga '{istrinta_knyga['pavadinimas']}' sėkmingai ištrinta!")
        else:
            print("Klaida: Neteisingas knygos numeris.")
    except ValueError:
        # Jei įvestis nėra numeris, bandome ieškoti pagal pavadinimą
        for knyga in knygos:
            if knyga['pavadinimas'].lower() == identifikatorius.lower():
                knygos.remove(knyga)
                print(f"Knyga '{knyga['pavadinimas']}' sėkmingai ištrinta!")
                return
        print("Klaida: Knyga su tokiu pavadinimu nerasta.")
 
def pagrindinis_meniu():
    knygos = [{
        "pavadinimas": "Rasputinas",
        "autorius": "Edvard Radzinsky",
        "metai": 2011,
        "zanras": "romanas",
        "leidykla": "Alma litera"},
              {
        "pavadinimas": "Sidro namų taisyklės",
        "autorius": "John Irving",
        "metai": 2007,
        "zanras": "romanas",
        "leidykla": "Alma litera"}
    ]
    while True:
        print("\nPagrindinis meniu:")
        print("1. Pridėti naują knygą")
        print("2. Atvaizduoti visų knygų sąrašą")
        print("3. Ieškoti knygos")
        print("4. Ištrinti knygą")
        print("5. Išeiti iš programos")
        pasirinkimas = input("Pasirinkite veiksmą (1-5): ")
        if pasirinkimas == "1":
            prideti_knyga(knygos)
        elif pasirinkimas == "2":
            atvaizduoti_knygas(knygos)
        elif pasirinkimas == "3":
            ieskoti_knygos(knygos)
        elif pasirinkimas == "4":
            istrinti_knyga(knygos)
        elif pasirinkimas == "5":
            print("Programa baigta.")
            break
        else:
            print("Klaida: Neteisingas pasirinkimas. Bandykite dar kartą.")
 
pagrindinis_meniu()
 