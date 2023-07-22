from __init__ import Base

from sqlalchemy import *

class Kategorija (Base):
    __tablename__ = "kategorija"
    ID_kategorija = Column(Integer, primary_key = True)
    naziv = Column(String(50))
    
   