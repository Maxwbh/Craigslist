# -*- coding: utf-8 -*-


__author__ = 'Maxwell da Silva Oliveira'
__site__ = 'www.msbrasil.inf.br'
from bs4 import BeautifulSoup
from datetime import datetime, date, time
from time import sleep
from read_html import Get_Url
from class_map import *
from util import *
from leitor_anuncio import  *
from urllib2 import HTTPError

import logging
import re
from sqlalchemy.sql.expression import null

from sqlalchemy import (create_engine, Column, Integer,
                        String, DateTime,Text, text, Float, ForeignKey, and_,func,desc)
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import (IntegrityError, OperationalError)


if __name__ == '__main__':


    #logging.basicConfig()
    #logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    import sys
    instancia = len(sys.argv) >= 2 and int(sys.argv[1])

    __sessao_url = Get_Url()

    try:
        isel = session.query(func.count(Url.id)).filter_by(status='1' ).first()
        if instancia:
            itotal = isel[0]
            iqtd = round(itotal / num_instancias)+1
            ini = int(iqtd * (instancia-1))
            ifim = int((iqtd * instancia)-1)
            if ifim < ini or ifim > itotal:
                ifim = itotal
            if ini<0 :
                ini = 0
            sel =session.query(Url).filter_by(status='1').limit(iqtd).offset(ini).all()

            #isel[ini:ifim]
            print 'Instancias %s - %s até %s' %(instancia,ini,ifim)
        else:
            sel = session.query(Url).filter_by(status='1').all()
        sel = sorted(sel, key=lambda k: k.last_access or datetime(1500,01,01))

    except:
        sel = []


    for pg  in sel:
        try:
            #sel_user = session_cm.query(Usuario).filter_by(id='1').all()

            if pg.customers_url and not pg.customers_url.ac_crawler:
                continue


            str_blacklist = pg.black_list and pg.black_list.split(',')
            str_whitelist = pg.white_list and pg.white_list.split(',')
            dt_start = pg.start_date
            dt_end = pg.end_date

            #sel_estado = session.query(Estados).filter_by(url_id=pg.estado).all()
            str_regiao = pg.cidade #sel_estado and sel_estado[0].regiao or None
            #sel_whitelist = session.query(WhilteList.nome).filter_by(sessao=pg.sessao).all()
            #str_whitelist= [ k[0]  for k in sel_whitelist ]
            try:
                print 'Lendo : ',pg.id,' -- ', pg.nome
                _html = __sessao_url.read(url=pg.nome)
                #f = urllib.urlopen(pg.nome)
                #_html = f.read()
            except:
                raise
            try:
                #############################
                # Filtrar Html principal    #
                #############################


                soup = BeautifulSoup(_html)
                soup_ar = []
                if 'ebayclassifieds.com' in pg.nome:
                    try:
                        soup_ar = soup.find('ol',class_='search-results', id="search-adsense-top")
                        soup_ar1 = soup_ar.find_next_sibling('ol')
                        soup_ar =soup_ar1.find_all('a')
                    except:
                        soup_ar =[]
                else:
                    soup_ar =soup.find_all('a')
                source_type = None
                for link in soup_ar:
                    session_cm.execute('select 1')
                    session_cm.commit()
                    session.execute('select 1')
                    session.commit()

                    link_int = link.get('href','').lower()

                    if 'craigslist.' in pg.nome:
                        source_type = 'craigslist.'
                        if not check_data(link_int ,[ '.html','.htm'])[0]:
                            continue
                    if 'ebayclassifieds.com' in pg.nome:
                        source_type = 'ebayclassifieds.com'
                        if not '/?ad=' in link_int  and '.ebayclassifieds.' in link_int  :
                            continue
                    if 'backpage.com' in pg.nome:
                        source_type = 'backpage.com'
                        continue


                    if not source_type in link_int:
                        continue


                    try:
                        html_int =__sessao_url.read(url=link_int)

                        ################################################
                        #    Importar HTML ( Anuncio )                 #
                        ################################################
                        res= load_html(urlid=pg.id,link_int=link_int, html_int=html_int, str_cidade=pg.cidade, str_estado=pg.estado,
                            str_sessao=pg.sessao, str_regiao=str_regiao, source= source_type,str_whitelist=str_whitelist,
                            str_blacklist=str_blacklist, dat_start = dt_start, dat_end = dt_end, customer_id = pg.customer_id )
                        if res.get('info'):
                            print '-->%s  ** %s **'%( link_int, res.get('info'))
                        else:
                            print '-->%s '%( link_int,)
                    except :
                        pass
                pg.last_access= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                session.add(pg)
                session.commit()
            except :
                raise

        except:
            continue
