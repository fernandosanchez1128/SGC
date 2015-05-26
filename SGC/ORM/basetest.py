from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, ForeignKeyConstraint, Float
from sqlalchemy import Table, Text

#engine = create_engine('postgresql://fersanq:fersanq@pgsql/fersanq', echo=True)
#engine = create_engine('postgresql://fernando:fernando1128@localhost/SGC', echo=True)
engine = create_engine('postgresql://brayanrod:bryan1112@localhost/sgc', echo=True)
#engine = create_engine('postgresql://braymrr:braymrr@pgsql/braymrr', echo=True)
#engine = create_engine('postgresql://fernando:fernando1128@localhost/SGC', echo=True)
#engine = create_engine('postgresql://nelson:nelsonalejo@localhost/sgc', echo=True)
Base = declarative_base()
