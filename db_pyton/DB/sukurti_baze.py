import mysql.connector 
import datetime

config = config = {
    "host": "localhost", # kokiam kompiuteryje veikia. mano_serveris.com
    "user": "editat", # naudotojo vardas
    "password": "SniegasPavasary2025", # koks slaptazodis
    "database": "nauja_baze" # kokia duomenu baze (koks pavadinimas duomenu bazes)
}
# Connect to MySQL
try:
    conn = mysql.connector.connect(**config) # greitkelio atidarymas
    cur = conn.cursor() # sukuriam automobili
    # cur.execute("SHOW TABLES") # pakraunam automobili
    # tables = cur.fetchall() # gaunam automobilio parvezta rezultata
    # print("Tables in database:", tables)  
except mysql.connector.Error as err:
    print("Error:", err)

# 1. Sukurkite naudotojų lentelę su stulpeliais (id,name,last_name)

# cur.execute("""create table if not exists Naudotojai(ID integer not null,
#             Vardas char(30) not null, Pavarde char(30) not null)""")

# # # 2. Pridėkite naują stulpelį į šią lentelę pavadinimu age

# cur.execute("""alter table naudotojai add amzius integer""")

# # 3. Pridėkite stulpelį gimimo data (datetime)

# cur.execute("""alter table naudotojai add gimimo_data date not null""")

# # 4. Ištrinkite stulpelį gimimo data

# cur.execute("""alter table naudotojai drop gimimo_data""")

# # 5. SUKURTA PRADZIOJ????

# # cur.execute("""alter table naudotojai add primary key (id)""")

# # 6. Sukurkite antrą lentelę automobilis kuri turėtų pagaminimo datetime
# # su Default reikšme dabartinė data (su bent trejais stulpeliais ir primary key (viskas vienoje užklausoje, be alter))

# cur.execute("""create table if not exists automobilis(ID integer auto_increment primary key, marke char (30)not null,
#             modelis char(30) not null,kebulo_tipas char(30) not null,
#              pagaminimo_data datetime not null default current_timestamp, spalva char(25))""")

# 7. •Sukurkite one to many ryšį, kad naudotojas galėtų turėti daug automobilių, tai pasieksite sukurdami foreign key apribojimą.

cur.execute("""alter table automobilis add naudotojai_ID integer, add foreign key (naudotojai_ID) references naudotojai (ID)""")

# # 8. •Sukurkite indeksą ant 2 pasirinktų stulpelių (galima viena komanda arba dvejomis)

# # cur.execute("""create index indeksas_vardas on naudotojai(vardas)""")
# # cur.execute("""create index indeksas_modelis on automobilis(modelis)""")

# # one to meny

# class Author(Base):
#     __tablename__ = 'authors' # vadinkite jeigu dirbate su mysql mazosiomis raidemis
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, nullable=False)
 
#     books = relationship('Book', back_populates='author')
 
# class Book(Base):
#     __tablename__ = 'books'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String, nullable=False)
 
#     author_id = Column(Integer, ForeignKey('authors.id')) # naudojam lenteles pavadinima
 
#     author = relationship('Author', back_populates='books') # cia naudojam klases pavadinima
 
 
#     publisher_associations = relationship('BookPublisher', back_populates='book')
 
#     def __repr__(self):
#         return f"{self.title} {self.author_id}"
 
# # with Session() as session:
# #     author = Author(name="Justas Kvederis")
 
# #     for title in ["Python", "Python 2", "How to survive Python"]:
# #         author.books.append(Book(title=title))
       
# #     session.add(author)
# #     session.commit()
 
# with Session() as session:
#     author = session.execute(select(Author).filter_by(name="Justas Kvederis")).scalar_one_or_none()
#     print(author.name)
#     print(author.books)
#     print(author.books[0].author.name)
 

#  many su many

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select
from sqlalchemy.orm import relationship, sessionmaker, DeclarativeBase
 
class Base(DeclarativeBase):
    pass
 
class BookPublisher(Base): # lentele jungianti knygas ir leidejus
    __tablename__ = 'book_publisher'
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    publisher_id = Column(Integer, ForeignKey('publishers.id'), primary_key=True)
 
    extra_info = Column(String)  # Additional field
 
    book = relationship('Book', back_populates='publisher_associations')
    publisher = relationship('Publisher', back_populates='book_associations')
 
class Author(Base):
    __tablename__ = 'authors' # vadinkite jeigu dirbate su mysql mazosiomis raidemis
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
 
    books = relationship('Book', back_populates='author')
 
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
 
    author_id = Column(Integer, ForeignKey('authors.id')) # naudojam lenteles pavadinima
 
    author = relationship('Author', back_populates='books') # cia naudojam klases pavadinima
 
 
    publisher_associations = relationship('BookPublisher', back_populates='book')
 
    def __repr__(self):
        return f"{self.title} {self.author_id}"
 
class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
 
    book_associations = relationship('BookPublisher', back_populates='publisher')
 
engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
 
def add_author_with_books(author_name, book_titles):
    with Session() as session:
        author = Author(name=author_name)
 
        for title in book_titles:
            author.books.append(Book(title=title))
 
        session.add(author)
        session.commit()
 
def add_publisher(publisher_name):
    with Session() as session:
        session.add(Publisher(name=publisher_name))
        session.commit()
 
def associate_book_with_publisher(book_title, publisher_name, extra_info=None):
    with Session() as session:
        book = session.execute(select(Book).filter_by(title=book_title)).scalar_one_or_none()
        publisher = session.execute(select(Publisher).filter_by(name=publisher_name)).scalar_one_or_none()
 
        if book and publisher:
            session.add(BookPublisher(book=book, publisher=publisher, extra_info=extra_info))
            session.commit()
 
def get_books_by_author(author_name):
    with Session() as session:
        author = session.execute(select(Author).filter_by(name=author_name)).scalar_one_or_none()
        return [book.title for book in author.books] if author else []
 
def get_publishers_by_book(book_title):
    with Session() as session:
        book = session.execute(select(Book).filter_by(title=book_title)).scalar_one_or_none()
        if book:
            return [(assoc.publisher.name, assoc.extra_info) for assoc in book.publisher_associations]
        return []
 
# add_author_with_books('George Orwell', ['1984', 'Animal Farm']) # pridesime autoriu su jo knygomis
 
# add_publisher('Penguin Books') # pridesime publisheri
 
# associate_book_with_publisher('1984', 'Penguin Books', 'First Edition') # pridesime rysi tarp knygos ir leidejo
 
# with Session() as session:
#     author = Author(name="Justas Kvederis")
 
#     for title in ["Python", "Python 2", "How to survive Python"]:
#         author.books.append(Book(title=title))
       
#     session.add(author)
#     session.commit()
 
# with Session() as session:
#     author = session.execute(select(Author).filter_by(name="Justas Kvederis")).scalar_one_or_none()
#     print(author.name)
#     print(author.books)
#     print(author.books[0].author.name)
 
# print(get_books_by_author('George Orwell'))  # Output: ['1984', 'Animal Farm']
# print(get_publishers_by_book('1984'))        # Output: [('Penguin Books', 'First Edition')]

# -----------------------------------------------------------
# --------------------------------------------------------------
# https://github.com/Qudevis/AIU4_Databases
# ------------------------------------------------------
# -------------------------------------------------------








