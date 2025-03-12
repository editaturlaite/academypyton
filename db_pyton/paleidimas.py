from PROJEKTAS_DARBUOTOJAI.KITA.sesija import sukurti_sesija
from PROJEKTAS_DARBUOTOJAI.KITA.klases import Darbuotojas
from PROJEKTAS_DARBUOTOJAI.KITA.meniu import pagrindinis_meniu
from PROJEKTAS_DARBUOTOJAI.KITA.klases import Base, engine
# Base.metadata.create_all(engine)

# Session = sukurti_sesija()

# with Session() as session:
#     darbuotojai = [
#         Darbuotojas("Jonas", "Jankauskas", "1990-01-15", "Administratorius", 1500),
#         Darbuotojas("Asta", "Stankevičienė", "1985-07-22", "Buhalterė", 1800),
#         Darbuotojas("Edvinas", "Petraitis", "1992-04-10", "IT specialistas", 2000),
#         Darbuotojas("Tomas", "Kazlauskas", "1988-12-05", "Projektų vadovas", 2500)
#     ]
#     session.add_all(darbuotojai)
#     session.commit()

while True:
    pagrindinis_meniu()
  


