
def sukurti_sesija():
    from sqlalchemy import create_engine 
    from sqlalchemy.orm import sessionmaker
    engine = create_engine("mysql://editat:SniegasPavasary2025@localhost/projektas_darbuotojai")
    Session = sessionmaker(engine)
    return Session
