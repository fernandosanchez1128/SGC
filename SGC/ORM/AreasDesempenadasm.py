from sqlalchemy import (Sequence)
from basetest import *

Column(Integer, Sequence('sec_areasm'), primary_key=True)


class AreasDesempenadasm(Base):
    __tablename__ = 'areas_desempenadasm'
    id = Column(Integer, Sequence('sec_areasm'), primary_key=True)
    area = Column(String, nullable=False)
    cedula_lt = Column(String(20), ForeignKey('masterteacher.cedula'))

    def __repr__(self):
        return "<Area(area='%s')>" % self.area


Base.metadata.create_all(engine)
