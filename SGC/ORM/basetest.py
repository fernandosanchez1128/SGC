from sqlalchemy import create_engine, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, ForeignKeyConstraint, Float
from sqlalchemy import Table, Text, func


#engine = create_engine('postgresql://juand:juand@localhost/juand_prueba', echo=True)
#engine = create_engine('postgresql://brayanrod:bryan1112@localhost/sgc', echo=True)
#engine = create_engine('postgresql://braymrr:braymrr@pgsql/braymrr', echo=True)
#engine = create_engine('postgresql://fernando:fernando1128@localhost/SGC', echo=True)
engine = create_engine('postgresql://nelson:nelsonalejo@localhost/sgc', echo=True)
#engine = create_engine('postgresql://fxfrchauzwmjex:DP52ExJELmuLLIMcwyFJ5FH5Qd@ec2-184-73-253-4.compute-1.amazonaws.com/d8fi4ua8fs70la', echo=True)
Base = declarative_base()
