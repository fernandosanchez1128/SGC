from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, Text

#engine = create_engine('postgresql://braymrr:braymrr@pgsql/braymrr', echo=True)
engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
Base = declarative_base()
