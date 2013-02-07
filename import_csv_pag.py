#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maxwell'

import logging
import urllib
from datetime import datetime, date, time
import re
from bs4 import BeautifulSoup
from sqlalchemy import (create_engine, Column, Integer,
                        String, DateTime,Text, text, Float, ForeignKey, and_)
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import (IntegrityError, OperationalError)

from class_map import *
from util import *
from leitor_anuncio import load_html
import sys



if __name__ == '__main__':
    for param in sys.argv :
        print(param)

#    """
#    FORMAT = "%(asctime)-15s %(message)s"
#    logging.basicConfig(format=FORMAT)
#    logging.warning("Protocol problem: %s", "connection reset", extra="Start Connection")
#    """


    sel = session_cm.query(Url).filter_by(status='1').all()

    sel_blacklist = session.query(BlackList.nome).filter_by(status='1').all()
    str_blacklist= [ k[0]  for k in sel_blacklist ]

    for pg  in sel[0:2]:
        sel_estado = session.query(Estados).filter_by(url_id=pg.estado).all()
        str_regiao = sel_estado and sel_estado[0].regiao

        sel_whitelist = session.query(WhilteList.nome).filter_by(sessao=pg.sessao).all()
        str_whitelist= [ k[0]  for k in sel_whitelist ]
        try:
            print 'Lendo : ',pg.id,' -- ', pg.nome
            f = urllib.urlopen(pg.nome)
            _html = f.read()
        except :
            print 'Servidor não acessivel'
            continue
        try:
            #############################
            # Filtrar Html principal    #
            #############################


            soup = BeautifulSoup(_html)
            for link in soup.find_all('a'):
                link_int = link.get('href','')
                if not check_data(link_int.lower() ,[ '.html','.htm'])[0]:
                    continue
                print '-->', link_int
                try:
                    f_int = urllib.urlopen(link_int)
                    html_int = f_int.read()
                except :
                    continue
                ################################################
                #    Importar HTML ( Anuncio )                 #
                ################################################
                res = load_html(link_int=link_int, html_int=html_int, str_cidade=pg.cidade, str_estado=pg.estado, \
                    str_sessao=pg.sessao, str_regiao=str_regiao, str_whitelist=str_whitelist, \
                    str_blacklist=str_blacklist)
                if res.get('info'):
                    print res.get('info')
            pg.status='3'
            session_cm.add(pg)
            session_cm.commit()
        except :
            raise

    print '--  Final ---'