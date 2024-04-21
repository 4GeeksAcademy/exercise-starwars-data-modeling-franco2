import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table  
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favoritos_usuario = Table('favoritos_usuario',
                          Base.metadata,
                          Column('usuario_id', Integer, ForeignKey('usuario.id')),
                          Column('favorito_id', Integer, ForeignKey('favorito.id'))
                         )

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    usuario = Column(String(250))
    contraseña = Column(String(250))
    nombre = Column(String(250), nullable=False)
    favoritos = relationship("Favorito", secondary=favoritos_usuario, back_populates="usuarios")

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    tipo = Column(String(50)) 
    id_starwars = Column(Integer) 
    usuarios = relationship("Usuario", secondary=favoritos_usuario, back_populates="favoritos")

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    clima = Column(String(250))
    terreno = Column(String(250))
    favoritos = relationship("Favorito", back_populates="planetas")

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    especie = Column(String(250))
    genero = Column(String(250))
    favoritos = relationship("Favorito", back_populates="personajes")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

