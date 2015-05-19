__author__ = 'family'

<<<<<<< HEAD
from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, ForeignKeyConstraint, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime
=======
from sqlalchemy import (Date)

>>>>>>> 81892d87ecac2088b2b50a11582419716208781d

#engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
#engine = create_engine('postgresql://braymrr:braymrr@pgsql/braymrr', echo=True)
#engine = create_engine('sqlite:///usuario.db', echo=True)
#Base = declarative_base()


from basetest import *


class Asignacion (Base):
    __tablename__ = 'asignacion'

<<<<<<< HEAD
    id_curso = Column(Integer, index=True, primary_key=True)
    id_cohorte = Column(Integer, index=True, primary_key=True)
    id_actividad =  Column(Integer, index=True, primary_key=True)
    fecha_hora  = Column (DateTime)
    __table_args__ = (ForeignKeyConstraint([id_curso, id_cohorte],['cohorte.id_curso','cohorte.id_cohorte']),{})
    __table_args__ = (ForeignKeyConstraint([id_actividad, id_curso],['actividades.id_actividad','actividades.id_curso']),{})
=======
    id_curso = Column(Integer, primary_key=True)
    id_cohorte = Column(Integer, primary_key=True)
    id_actividad =  Column(Integer, primary_key=True)
    __table_args__ = (ForeignKeyConstraint([id_curso, id_cohorte, id_actividad], ['cohorte.id_curso', 'cohorte.id_cohorte', 'actividades.id_actividad']), {})
    fecha_hora  = Column (Date)
>>>>>>> 81892d87ecac2088b2b50a11582419716208781d
    
    


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
asg = Asignacion(id_curso =122, id_cohorte = 1,  id_actividad= 14)

session.add(asg)
session.commit()
