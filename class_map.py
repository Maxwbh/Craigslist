# -*- encoding: utf-8 -*-

__author__ = 'Maxwell da Silva Oliveira <maxwell@msbrasil.inf.br>'

from sqlalchemy import (create_engine, Column, Integer,
                        String, DateTime,Text, text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from ConfigParser import RawConfigParser


Base = declarative_base()

class Url(Base):
    __tablename__ = 'url'

    id = Column('id',Integer, primary_key=True)
    nome = Column('nome',String(100))
    sessao = Column('sessao',String(110))
    cidade = Column('cidade',String(110))
    estado = Column('estado',String(110))
    status = Column('status',String(1))
    white_list = Column('white_list',String(110))
    black_list = Column('black_list',String(110))
    start_date = Column('start_date',DateTime)
    end_date = Column('end_date',DateTime)
    last_access= Column('last_access',DateTime)
    customer_id = Column('userid',Integer, ForeignKey('customers.id'))


    customers_url = relationship('Usuario', backref=backref('customerUrl', order_by=id))


class BlackList(Base):
    __tablename__ = 'blacklist'

    id = Column('id',Integer, primary_key=True)
    nome = Column('nome',String(100))
    #status = Column('status',String(1))

class WhilteList(Base):
    __tablename__ = 'sessoes_whitelist'

    id = Column('id',Integer, primary_key=True)
    nome = Column('nome',String(100))
    sessao = Column('sessao', String(110))
    status = Column('status',String(1))


class Regiao(Base):
    __tablename__ = 'regiao'
    id = Column('id',Integer, primary_key=True)
    k = Column('k',String(32))
    nome = Column('nome',String(100))
    url_id = Column('url_id',String(110))

class Estados(Base):
    __tablename__ = 'estados'
    id = Column('id',Integer, primary_key=True)
    #k = Column('k',String(32))
    nome = Column('nome',String(100))
    #url_id = Column('url_id',String(110))
    regiao = Column('regiao',String(110))


class Anuncios(Base):
    __tablename__ = 'anuncios'
    id = Column('id',Integer, primary_key=True)
    #k = Column('k',String(32))
    nome = Column('nome',String(100))
    customer_id = Column('customer_id',Integer)
    url = Column('url',String(255))
    html = Column('html',Text)
    tags = Column('tags',Text)
    cidade = Column('cidade',String(110))
    estado = Column('estado',String(110))
    regiao = Column('regiao',String(110))
    sessao = Column('sessao',String(110))
    emails_type = Column('emails_type',Integer)
    has_phone = Column('has_phone',Integer)
    post_date = Column('post_date', DateTime, default=text('NOW()'))
    insert_date = Column('insert_date', DateTime, default=text('NOW()'))
    access_date= Column('access_date', DateTime, default=text('NOW()'))
    status= Column('status',String(1), default='1')
    site = Column('site',String(110))
    newsletters_id = Column('newsletters_id',Integer)

    #email = relationship("AnunciosEmails", order_by="AnunciosEmails.id", backref="anuncios")
    #phone = relationship("AnunciosTelefones", order_by="AnunciosTelefones.id", backref="anuncios")



class AnunciosEmails(Base):
    __tablename__ = 'anuncios_emails'
    id = Column('id',Integer, primary_key=True)
    #k = Column('k',String(32))
    nome = Column('nome',String(100))
    #url_id = Column('url_id',String(110))
    tipo = Column('tipo',String(110))
    #anuncio= Column('anuncio',String(110))
    regiao = Column('regiao',String(110))
    insert_date = Column('insert_date', DateTime, default=text('NOW()'))
    send_date = Column('send_date', DateTime, default=text('NOW()'))
    send_key = Column('send_key',String(110))
    anuncios_id = Column('anuncios_id',Integer, ForeignKey('anuncios.id'))

    anuncios_em = relationship('Anuncios', backref=backref('anuncioEM', order_by=id))


class AnunciosTelefones(Base):
    __tablename__ = 'anuncios_telefones'
    id = Column('id',Integer, primary_key=True)
    #k = Column('k',String(32))
    nome = Column('nome',String(100))
    #url_id = Column('url_id',String(110))
    #anuncio= Column('anuncio',String(110))
    insert_date = Column('insert_date', DateTime, default=text('NOW()'))
    anuncio_id = Column('anuncios_id',Integer, ForeignKey('anuncios.id'))

    anuncios_ph = relationship('Anuncios', backref=backref('anuncioPH', order_by=id))

class Smtp(Base):
    __tablename__='smtp'
    id = Column('id',Integer, primary_key=True)
    usuarios_id = Column('usuarios_id',Integer)
    usuario =Column('usuario',String(100))
    senha=Column('senha',String(30))
    porta =Column('porta',String(4))
    host =Column('host',String(250))
    nome =Column('nome',String(250))
    seguro =Column('seguro',Integer)
    status =Column('status',Integer)
    dta_proximo_envio=Column('dta_proximo_envio', DateTime, default=text('NOW()'))
    limite_envio=Column('limite_envio',Integer)
    qtde_enviada=Column('qtde_enviada',Integer)
    qtde_max_envio=Column('qtde_max_envio',Integer)
    qtde_seg_envio=Column('qtde_seg_envio',Integer)

class Usuario(Base):
    __tablename__='customers'
    id = Column('id',Integer, primary_key=True)
    nome = Column('first_name',String(100))
    ac_crawler = Column('ac_crawler',Integer)
    ac_sender = Column('ac_sender',Integer)

class NewsLetters(Base):
    __tablename__ = 'newsletters'
    id = Column('id',Integer, primary_key=True)
    titulo = Column('titulo',String(100))
    texto = Column('texto',Text)
    status = Column('status',Integer)
    usuarios_id = Column('usuarios_id',Integer)


config = RawConfigParser()
config.read('emailtool.cfg')
str_cfg = (config.get('DataBase', 'conn'),config.get('DataBase', 'user'),config.get('DataBase', 'pwd'),
           config.get('DataBase', 'iphost'),config.get('DataBase', 'port'),config.get('DataBase', 'base') )
str_conn = '%s://%s:%s@%s:%s/%s?charset=utf8'
try:
    num_instancias = int(config.get('Instancias', 'ntotal'))
except:
    num_instancias= 10

engine = create_engine(str_conn%str_cfg,pool_recycle=3800,echo_pool=True )

Base.metadata.create_all(engine)

session = Session(engine)
session_cm = Session(engine)

