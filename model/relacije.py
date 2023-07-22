
from sqlalchemy.orm import relationship
from korisnici import Korisnik
from narudzba import Narudzba
from kategorija import Kategorija
from proizvod import Proizvod
from kosarica import Kosarica
from __init__ import Base
from __init__  import engine


Korisnik.narudzba = relationship('Narudzba', back_populates='korisnik')
Kategorija.proizvod = relationship('Proizvod', back_populates='kategorija')
Korisnik.kosarica = relationship('Kosarica', back_populates="korisnik")

Base.metadata.bind = engine
Base.metadata.create_all(bind=engine)