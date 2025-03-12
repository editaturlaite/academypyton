from sqlalchemy import create_engine, Column, Integer, String,select, or_, Date, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker,relationship
from sqlalchemy.sql import func
 
engine = create_engine("mysql://editat:SniegasPavasary2025@localhost/projektas_darbuotojai")

class Base(DeclarativeBase):
    pass
 
class Darbuotojas(Base):
    __tablename__ = 'darbuotojas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column(String(50), nullable=False)
    pavarde = Column(String(50),nullable=False)
    gimimo_data = Column(Date)
    pareigos = Column(String(40), nullable=False)
    atlyginimas = Column(Integer)
    pradzios_data = Column(DateTime, default=func.current_timestamp())
    departamentas_id = Column(Integer,ForeignKey('departamentas.id',ondelete="SET NULL"),nullable=True)

    departamentas = relationship('Departamentas', back_populates='darbuotojai',foreign_keys=[departamentas_id])
    darbuotojo_projektai = relationship('DarbuotojasProjektas',back_populates='darbuotojas')


    def __init__(self,vardas,pavarde,gimimo_data,pareigos,atlyginimas,departamentas_id = None):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas
        self.departamentas_id = departamentas_id
         

    def __str__(self):
        return f"Vardas: {self.vardas} | Pavarde: {self.pavarde} | Gimimo data: {self.gimimo_data} | Pareigos: {self.pareigos} | Atlyginimas: {self.atlyginimas} | Dirba nuo: {self.pradzios_data} | Departamentas: {self.departamentas_id}"
    
    # def __repr__(self):
    #     return f"Vardas: {self.vardas} Pavarde: {self.pavarde} Gimimo data: {self.gimimo_data} Pareigos: {self.pareigos} Atlyginimas: {self.atlyginimas} Dirba nuo: {self.pradzios_data}"

class Projektas(Base):
    __tablename__ = 'projektas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pavadinimas = Column(String(50), nullable=False)
    aprasymas = Column(String(200),nullable=False)

    darbuotojo_projektai = relationship('DarbuotojasProjektas', back_populates='projektas')

    def __init__(self,pavadinimas,aprasymas):
        self.pavadinimas = pavadinimas
        self.aprasymas = aprasymas

    def __str__(self):
        return f"Pavadinimas: {self.pavadinimas} | Aprasymas: {self.aprasymas}"

class DarbuotojasProjektas(Base):
    __tablename__ = 'darbuotojas_projektas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    darbuotojas_id = Column(Integer, ForeignKey('darbuotojas.id'),nullable=False)
    projektas_id = Column(Integer, ForeignKey('projektas.id'),nullable=False)
    role_projekte = Column(String(50))
    darbuotojas = relationship('Darbuotojas', back_populates='darbuotojo_projektai')
    projektas = relationship('Projektas', back_populates='darbuotojo_projektai')
        

class Departamentas(Base):
    __tablename__ = 'departamentas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pavadinimas= Column(String(50), nullable=False)
    vadovas_id= Column(Integer, ForeignKey('darbuotojas.id',ondelete="SET NULL"),nullable=True)

    darbuotojai = relationship('Darbuotojas', back_populates='departamentas',foreign_keys=[Darbuotojas.departamentas_id])
    
    def __init__(self, pavadinimas,vadovas_id = None):
        self.pavadinimas = pavadinimas
        self.vadovas_id = vadovas_id

    def __str__(self):
        return f"Departamento pavadinimas: {self.pavadinimas} | Departamento vadovo ID: {self.vadovas_id}"





