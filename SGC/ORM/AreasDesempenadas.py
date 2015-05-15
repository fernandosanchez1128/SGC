from sqlalchemy import (Sequence)
from basetest import *

Column(Integer, Sequence('sec_areas'), primary_key=True)


class AreasDesempenadas(Base):
    __tablename__ = 'areas_desempenadas'
    id = Column(Integer, Sequence('sec_areas'), primary_key=True)
    area = Column(String, nullable=False)
    cedula_lt = Column(String(20), ForeignKey('leaderteacher.cedula'))

    def __repr__(self):
        return "<Area(area='%s')>" % self.area


Base.metadata.create_all(engine)
