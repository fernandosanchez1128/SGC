from sqlalchemy import (Sequence)

from basetest import *

Column(Integer, Sequence('sec_nivelesm'), primary_key=True)


class Nivelesm(Base):
    __tablename__ = 'nivelesm'
    id = Column(Integer, Sequence('sec_nivelesm'), primary_key=True)
    niveles = Column(String, nullable=False)
    cedula_lt = Column(String(20), ForeignKey('masterteacher.cedula'))

    def __repr__(self):
        return "<niveles(niveles='%s')>" % self.niveles


Base.metadata.create_all(engine)
