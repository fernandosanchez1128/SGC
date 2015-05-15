from sqlalchemy import (Sequence)

from basetest import *

Column(Integer, Sequence('sec_mod'), primary_key=True)


class Modalidad(Base):
    __tablename__ = 'modalidad'
    id = Column(String(20), Sequence('sec_mod'), primary_key=True)
    modalidad = Column(String, nullable=False)
    cedula_lt = Column(String(20), ForeignKey('leaderteacher.cedula'))

    def __repr__(self):
        return "<modalidad(modalidad='%s')>" % self.modalidad


Base.metadata.create_all(engine)
