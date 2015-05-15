from sqlalchemy import (Sequence)

from basetest import *


Column(Integer, Sequence('sec_grados'), primary_key=True)


class GradosDesempenados(Base):
    __tablename__ = 'grados'
    id = Column(Integer, Sequence('sec_grados'), primary_key=True)
    grados = Column(String, nullable=False)
    cedula_lt = Column(String(20), ForeignKey('leaderteacher.cedula'))

    def __repr__(self):
        return "<grados(grados='%s')>" % self.grados


Base.metadata.create_all(engine)
