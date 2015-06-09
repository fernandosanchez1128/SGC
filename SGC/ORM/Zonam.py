from sqlalchemy import (Sequence)
from basetest import *

Column(Integer, Sequence('sec_zonam'), primary_key=True)


class Zonam(Base):
    __tablename__ = 'zonam'
    id = Column(Integer, Sequence('sec_zonam'), primary_key=True)
    zona = Column(String, nullable=False)
    cedula_lt = Column(String(20), ForeignKey('masterteacher.cedula'))

    def __repr__(self):
        return "<zona(zona='%s')>" % self.zona


Base.metadata.create_all(engine)
