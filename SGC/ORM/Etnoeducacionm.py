from sqlalchemy import (Sequence)

from basetest import *


Column(Integer, Sequence('sec_etnoeducacionm'), primary_key=True)


class Etnoeducacionm(Base):
    __tablename__ = 'etnoeducacionm'
    id = Column(Integer, Sequence('sec_etnoeducacionm'), primary_key=True)
    etnoeducacion = Column(String, nullable=False)
    cedula_lt = Column(String(20), ForeignKey('masterteacher.cedula'))

    def __repr__(self):
        return "<etnoeducacion(etnoeducacion='%s')>" % self.etnoeducacion


Base.metadata.create_all(engine)
