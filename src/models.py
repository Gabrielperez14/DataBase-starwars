import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key = True) 
    favorito = relationship("Favorito", backref="usuario")
    name = Column(String(30), nullable = False)
    email = Column(String(40), nullable = False, unique = True)
    contraseña = Column(String(15), nullable = False, unique = True)
    


class Favorito(Base):
    __tablename__= "favorito"
    id = Column(Integer, primary_key = True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship("Usuario", backref = "favorito")
    persona = relationship("persona")
    vehiculo = relationship("vehiculo")
    planeta = relationship("planeta")
    persona_id = Column(Integer, ForeignKey("persona.id"))
    planeta_id = Column(Integer, ForeignKey("planeta.id"))
    vehiculo_id = Column(Integer,ForeignKey("vehiculo.id"))

class Persona(Base):
    __tablename__ = "persona"
    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False,)
    eye_color = Column(String(10))
    hair_color = Column(String(10))
    gender = Column(String(6))
    birth_year = Column(Integer)



class Vehiculo(Base):
    __tablename__= "vehiculo"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    model = Column(String(50))
    passenger = Column(Integer)
    manufacturer = Column(String(30))
    crew = Column(Integer)


class Planeta(Base):
    __tablename__= "planeta"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    population = Column(Integer)
    climate = Column(String(20))
    gravity = Column(Integer)
    rotation_period = Column(Integer)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')