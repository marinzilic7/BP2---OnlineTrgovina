from __init__ import Base

from sqlalchemy import *


class Narudzba (Base):
    __tablename__ = "narudzba"
    ID_narudzba = Column(Integer, primary_key = True)
    korisnik_id = Column(Integer, ForeignKey('korisnici.ID_korisnika'))
    proizvod_id = Column(Integer,ForeignKey('proizvod.ID_proizvoda'))
    naziv = Column(String(50))
    ukupni_iznos =Column(Integer)
   