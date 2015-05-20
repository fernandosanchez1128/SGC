from sqlalchemy import (Sequence)

from basetest import *

Column(Integer, Sequence('sec_etnoeducacion'), primary_key=True)
class Etnoeducacion(Base):
	__tablename__ = 'etnoeducacion'
	id = Column(Integer,Sequence('sec_etnoeducacion'),primary_key=True)
	etnoeducacion = Column(String, nullable=False)
	cedula_lt = Column(String(20), ForeignKey('leaderteacher.cedula'))
	
	def __repr__(self):
		return "<etnoeducacion(etnoeducacion='%s')>" % self.etnoeducacion
	
Base.metadata.create_all(engine)
