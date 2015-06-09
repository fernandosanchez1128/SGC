from sqlalchemy import (Sequence)
from basetest import *

Column(Integer, Sequence('sec_zona'), primary_key=True)


class Zona(Base):
    __tablename__ = 'zona'
    id = Column(Integer, Sequence('sec_zona'), primary_key=True)
    zona = Column(String, nullable=False)
    cedula_lt = Column(String(20), ForeignKey('leaderteacher.cedula'))

    def __repr__(self):
        return "<zona(zona='%s')>" % self.zona


Base.metadata.create_all(engine)
