from sqlalchemy import create_engine, Column, Integer, String,select, or_
from sqlalchemy.orm import DeclarativeBase, sessionmaker
 
engine = create_engine("mysql://editat:SniegasPavasary2025@localhost/alchemija") #engine = create_engine("sqlite:///foo.db")
 
# Base = DeclarativeBase()
class Base(DeclarativeBase):
    pass
 
class Person(Base):
    __tablename__ = 'People'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    age = Column(Integer)
 
class Car(Base):
    __tablename__ = 'Cars'
    id = Column(Integer, primary_key=True, autoincrement=True)
    make = Column(String(50), nullable=False)
    model = Column(String(50))
    year = Column(Integer)
 
Base.metadata.create_all(engine)

with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
    gautas_zmogus = session.get(Person,1) # gauname objekta pagal primary key
    gautas_zmogus.speak()
    print(gautas_zmogus)

    # with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
#     gautas_zmogus = session.get(Person,1) # gauname objekta pagal primary key
#     gautas_zmogus.speak()
#     print(gautas_zmogus)
 
with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
    query = select(Person).filter_by(name="Justas" ) # gauname objektus
    people = session.execute(query).scalars().all()
    print(people)
 
    for person in people:
        person.speak()
 
# ---------------------------------------------------------------

# with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
#     gautas_zmogus = session.get(Person,1) # gauname objekta pagal primary key
#     gautas_zmogus.speak()
#     print(gautas_zmogus)
 
with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
    query = select(Person).filter_by(name="Justas" ) # gauname objektus
    people = session.execute(query).scalars().all()
    print(people)
 
    for person in people:
        person.speak()
 
with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
    query = select(Person).where(
        or_
        (Person.age > 26,
         Person.name == "Justas")) # yra or salyga, jeigu norime panaudoti or, reikia ji importuoti ir prirasyti
    query2 = select(Person).where(
     Person.age > 26,
    Person.name == "Justas")
    people = session.execute(query).scalars().all()
    print(people)
 
    for person in people:
        person.speak()
 
# jeigu galima Justai, viska nukopink nuo pradziu iki pabaigos 
 
from sqlalchemy import create_engine, Column, Integer, String, select, or_
 
# aha, man neaisku, labai greitai, nespeju susiziureti
 
from sqlalchemy import create_engine, Column, Integer, String, select, or_ # create engine (tai is esmes panasu i connection, kur naudojom pries tai)
from sqlalchemy.orm import DeclarativeBase, sessionmaker # pagrindine klase, is kurios privales paveldeti visos jusu naujos klases
 
engine = create_engine("mysql://Justas:Code2024.@localhost/aiu4") # prisijungimas, prie duomenu bazes - duomenu baze://vardas:slaptazodis@adresas duomenu bazes ir tada / ir schemos pavadinimas
class Base(DeclarativeBase):
    pass # laukelius, kuriuos tures visa jusu duomenu baze
# daznai mes norime tuetu visose lentelese siuos duomenis (kada sukurtas irasas (CreatedOn) - CreatedBy - kas sukure | Deleted - Ar istringas True/False ModifiedOn ir ModifiedBy
 
class Person(Base): # privalo paveldeti base ir kai paveldi, jos yra priskiriamos tarsi buti dalimi Base
    __tablename__ = 'people' # pavadinimas duomenų bazėje, kaip šita lentele atrodys
    id = Column(Integer, primary_key=True, autoincrement=True) # nauja stulpeli duomenu bazeje, kuris bus primary key ir bus autoincrement
    name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    age = Column(Integer)
 
    def __init__(self, name,last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age
 
    def __str__(self):
        return f"{self.name} {self.last_name}"
    def __repr__(self):
        return self.name
    def speak(self):
        print(f"{self.name} sneka")
 
class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, autoincrement=True)
    make = Column(String(50), nullable=False)
    model = Column(String(50))
    year = Column(Integer)
 
Base.metadata.create_all(engine)
 
session_maker = sessionmaker(engine)
 
# with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
#     # zmogus = Person(name="Justas",last_name="Kvederis",age=25)
#     zmogus = Person("Antanas","Antanaitis",30)
#     session.add(zmogus) # idedam nauja zmogu
#     session.commit()
 
# with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
#     gautas_zmogus = session.get(Person,1) # gauname objekta pagal primary key
#     gautas_zmogus.speak()
#     print(gautas_zmogus)
 
# with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
#     query = select(Person).filter_by(name="Justas" ) # gauname objektus
#     people = session.execute(query).scalars().all() # scalar_one - jeigu vienas
#     print(people)
 
#     for person in people:
#         person.speak()
 
# with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
#     query = select(Person).where(
#         or_
#         (Person.age > 26,
#          Person.name == "Justas")) # yra or salyga, jeigu norime panaudoti or, reikia ji importuoti ir prirasyti
   
#     query2 = select(Person).where(
#      Person.age > 26,
#      Person.name == "Justas") # pagal nutylejima yra and
 
#     people = session.execute(query2).scalars().all()
#     print(people)
 
#     for person in people:
#         person.speak()
 
with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
    gautas_zmogus = session.get(Person,1) # gauname objekta pagal primary key
    gautas_zmogus.name = "Naujas"
    session.commit()
    print(gautas_zmogus)
 
 from sqlalchemy import Table, Column, Integer, ForeignKey

from sqlalchemy.orm import relationship, declarative_base
 
Base = declarative_base()
 
# Simple many-to-many table (NO extra fields)

worker_project_table = Table(

    "worker_project",

    Base.metadata,

    Column("worker_id", Integer, ForeignKey("workers.id"), primary_key=True),

    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),

)
 
class Worker(Base):

    __tablename__ = "workers"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
 
    # Using secondary table (No extra fields allowed)

    projects = relationship("Project", secondary=worker_project_table, back_populates="workers")
 
class Project(Base):

    __tablename__ = "projects"
 
    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
 
    workers = relationship("Worker", secondary=worker_project_table, back_populates="projects")
 