from sqlalchemy import (Sequence)

from basetest import *


Column(Integer, Sequence('sec_gradosm'), primary_key=True)


class GradosDesempenadosm(Base):
    __tablename__ = 'gradosm'
    id = Column(Integer, Sequence('sec_gradosm'), primary_key=True)
    grados = Column(String, nullable=False)
    cedula_lt = Column(String(20), ForeignKey('masterteacher.cedula'))

    def __repr__(self):
        return "<grados(grados='%s')>" % self.grados


Base.metadata.create_all(engine)
