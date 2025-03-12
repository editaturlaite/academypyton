import pickle

failo_pavadinimas = "balansas.picle"

try:
    with open(failo_pavadinimas, "rb") as failas:
        duomenys = pickle.load(failas)
        print("Failo turinys:", duomenys)
except (EOFError, FileNotFoundError):
    print("Failas tuščias arba nerastas!")