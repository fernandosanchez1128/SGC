__author__ = 'family'

from sqlalchemy import (Date)


#engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
#engine = create_engine('postgresql://braymrr:braymrr@pgsql/braymrr', echo=True)
#engine = create_engine('sqlite:///usuario.db', echo=True)
#Base = declarative_base()


from basetest import *


class Asignacion (Base):
    __tablename__ = 'asignacion'

    id_curso = Column(Integer, primary_key=True)
    id_cohorte = Column(Integer, primary_key=True)
    id_actividad =  Column(Integer, primary_key=True)
    __table_args__ = (ForeignKeyConstraint([id_curso, id_cohorte, id_actividad], ['cohorte.id_curso', 'cohorte.id_cohorte', 'actividades.id_actividad']), {})
    fecha_hora  = Column (Date)
    
    


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
asg = Asignacion(id_curso =122, id_cohorte = 1,  id_actividad= 14)

session.add(asg)
session.commit()
