
from sqlalchemy import (Sequence)

from basetest import *

Column(Integer, Sequence('sec_modm'), primary_key=True)


class Modalidadm(Base):
    __tablename__ = 'modalidadm'
    id = Column(String(20), Sequence('sec_modm'), primary_key=True)
    modalidad = Column(String, nullable=False)
    cedula_lt = Column(String(20), ForeignKey('masterteacher.cedula'))

    def __repr__(self):
        return "<modalidad(modalidad='%s')>" % self.modalidad


Base.metadata.create_all(engine)