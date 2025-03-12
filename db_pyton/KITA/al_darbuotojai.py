from sqlalchemy import create_engine, Column, Integer, String,select, or_, Date, DateTime, func
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import datetime
 
engine = create_engine("mysql://editat:SniegasPavasary2025@localhost/al_darbuotojai")

class Base(DeclarativeBase):
    pass
 
class Darbuotojas(Base):
    __tablename__ = 'darbuotojai'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column(String(50), nullable=False)
    pavarde = Column(String(50),nullable=False)
    gimimo_data = Column(Date)
    pareigos = Column(String(40), nullable=False)
    atlyginimas = Column(Integer)
    dirba_nuo = Column(DateTime, default=func.current_timestamp())

    def __init__(self,vardas,pavarde,gimimo_data,pareigos,atlyginimas,dirba_nuo):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas
        self.dirba_nuo = dirba_nuo     

    def __str__(self):
        return f"{self.vardas} {self.pavarde} {self.gimimo_data} {self.pareigos} {self.atlyginimas} {self.dirba_nuo}"
    
    def __repr__(self):
        return f"{self.vardas} {self.pavarde} {self.gimimo_data} {self.pareigos} {self.atlyginimas} {self.dirba_nuo}"
    

Base.metadata.create_all(engine)

Session = sessionmaker(engine)

def ivesti_darbuotoja(pridedamas_darbuotojas):
    with Session() as session:
        session.add(pridedamas_darbuotojas)
        session.commit()

def perziureti_darbuotojus():
    with Session() as session:
        stmt = select(Darbuotojas)
        darbuotojai = session.execute(stmt).scalars().all()
    return darbuotojai

def atnaujinti_darbuotojo_varda(ieskomas_vardas,naujas_vardas):
    with Session() as session:
        stmt = select(Darbuotojas).filter_by(vardas = ieskomas_vardas)
        rastas_darbuotojas = session.execute(stmt).scalar_one()
        if rastas_darbuotojas:
            rastas_darbuotojas.vardas = naujas_vardas
            session.commit()
        
def atnaujinti_darbuotojo_pareigas(ieskomas_vardas,naujos_pareigos):
    with Session() as session:
        stmt = select(Darbuotojas).filter_by(vardas = ieskomas_vardas)
        rastas_darbuotojas = session.execute(stmt).scalar_one()
        if rastas_darbuotojas:
            rastas_darbuotojas.pareigos = naujos_pareigos
            session.commit()

def istrinti_darbuotoja(norimas_istrinti):
    with Session() as session:
        stmt = select(Darbuotojas).filter_by(vardas = norimas_istrinti)
        istrinamas_darbuotojas = session.execute(stmt).scalar_one()
        session.delete(istrinamas_darbuotojas)
        session.commit()


# i_vardas = input("Iveskite darbuotojo varda: ")
# i_pavarde = input("Iveskite darbuotojo pavarde: ")
# i_gimimo_data = input("Iveskite darbuotojo gimomo data formatu yyyy-mm-dd: ")
# konvertuota_gimimo_data = datetime.datetime.strptime(i_gimimo_data, '%Y-%m-%d')
# i_pareigos = input("Iveskite darbuotojo pareigas: ")
# i_atlyginimas = int(input("Iveskite darbuotojo atlyginima: "))

# naujas_darbuotojas=Darbuotojas(vardas=i_vardas,pavarde=i_pavarde,gimimo_data=konvertuota_gimimo_data.date(),pareigos=i_pareigos,atlyginimas=i_atlyginimas)

# ivesti_darbuotoja(naujas_darbuotojas)

# print(perziureti_darbuotojus())

# ieskomas_darbuotojas = input("Iveskite darbuotojo varda, kurio varda norite atnaujinti: ")
# naujas_vardas = input("Iveskite nauja varda: ")
# naujos_pareigos = input("Iveskite naujas pareigas: ")

# atnaujinti_darbuotojo_varda(ieskomas_darbuotojas,naujas_vardas)

# atnaujinti_darbuotojo_pareigas(ieskomas_darbuotojas, naujos_pareigos)

# norimas_istrinti_darbuotojas = input("Iveskite darbuotojo varda, kuri norite istrinti: ")
# istrinti_darbuotoja(norimas_istrinti_darbuotojas)



    