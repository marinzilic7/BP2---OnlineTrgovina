from __init__ import Base

from sqlalchemy import *


class Proizvod (Base):
    __tablename__ = "proizvod"
    ID_proizvoda = Column(Integer, primary_key = True)
    ID_kategorija = Column(Integer,ForeignKey('kategorija.ID_kategorija'))
    naziv = Column(String(50))
    opis =Column(String(50))
    cijena =Column(Integer)
    