# -*- encoding: utf-8 -*-

__author__ = 'Maxwell'

from datetime import datetime, date, time
import re
from bs4 import BeautifulSoup
from sqlalchemy.exc import (IntegrityError, OperationalError)

from class_map import *
from util import *



def load_html(urlid,link_int, html_int, str_cidade, str_estado, str_sessao, str_regiao, source, str_whitelist=[],\
              str_blacklist=[],dat_start = None, dat_end = None, customer_id=None,contador=0,contador_bk=0):


    ###########################
    # Leitura do anuncio      #
    ###########################
    soup_int = BeautifulSoup(html_int)
    texto = ''
    if source == 'craigslist.':
        texto = soup_int
    elif source == 'ebayclassifieds.com':
        texto = soup_int.find('div', id="ad-details")
        if 'but no ads' in soup_int.text:
            return {'info':'Ebay nao retornou classificados para esta selecao'}

    elif source == 'backpage.com':
        _texto = soup_int.find('div')
        for i in _texto:
            if i.get('class')=='postingBody':
                texto = i

    if not texto :
        texto = soup_int.text
    else:
        texto = texto.text

    #########################
    # White List            #
    #########################
    if str_whitelist:
        in_white_list = check_data(texto ,str_whitelist)
        if not in_white_list[0]:
            return {'info':'Html nao incluso na Withe List '}


    #########################
    # Black List            #
    #########################
    if str_blacklist:
        in_blak_list = check_data(texto ,str_blacklist)
        if in_blak_list [0]:
            return {'info':'Html em Black List (%s)'%in_blak_list[1]}

    #######################
    # Tratar anuncio p/   #
    #    Insercao         #
    ############################
    # Não esta na Black List   #
    # Esta na White List ou [] #
    ############################


    if source == 'craigslist.':
        try:
            try:
                time_sec = soup_int.find('time').text
            except:
                time_sec = soup_int.find('date').text
            try:
                body_sec = soup_int.find('section', id="postingbody")
                body_texto = body_sec.text
            except:
                body_sec = soup_int.find('section', id="userbody")
                body_texto = body_sec.text
            email = soup_int.find('span',id='replytext')
            email = email.find_next("a").text
            if not email or not '@' in email:
                tipo_mail = -1
                email = ''
            elif ('.craigslist.') in email:
                tipo_mail = 0
            else:
                tipo_mail = 1

            titulo = soup_int.find_all('title')[0].text
            titulo_id = re.sub(r"[^A-Za-z0-9]",'_',titulo).replace('__','_')
            phone = get_phone(body_texto )
            tags = get_tags(body_texto )
            time_sec = datetime.strptime(time_sec[:19], "%Y-%m-%d, %I:%M%p")
        except:

            return {'info':'Crgl - Erro na identificacao dos elementos do HTML'}

    elif source == 'ebayclassifieds.com':
        try:

            _time_sec = soup_int.find('div',id='ad-details').find_all('span')
            time_sec  = datetime.strptime('01/01/1500', "%m/%d/%Y")
            for i in _time_sec:
                try:
                    time_sec = datetime.strptime(i.text, "%m/%d/%y")
                    break
                except:
                    pass
            body_texto = texto
            email = ''
            tipo_mail = -1
            # Titulo da pagina
            titulo = soup_int.find_all('title')[0].text[:99]
            # Titulo do Anuncio
            #titulo = soup_int.find_all('h1',id='ad-title')[0].text

            titulo_id = re.sub(r"[^A-Za-z0-9]",'_',titulo).replace('__','_')
            phone = get_phone(body_texto )
            tags = get_tags(body_texto )
        except :
            return {'info':'eBay - Erro na identificacao dos elementos do HTML'}
            #raise
    elif source == 'backpage.com':
        try:

            _time_sec = soup_int.find('div',id='postingTitle').find_all('div')
            time_sec  = datetime.strptime('01/01/1500', "%m/%d/%Y")
            for i in _time_sec:
                try:
                    time_sec = datetime.strptime(i.text, "%m/%d/%y")
                    break
                except:
                    pass

            body_texto = texto
            email = ''
            tipo_mail = -1
            # Titulo da pagina
            titulo = soup_int.find_all('title')[0].text[:99]
            # Titulo do Anuncio
            #titulo = soup_int.find_all('h1',id='ad-title')[0].text

            titulo_id = re.sub(r"[^A-Za-z0-9]",'_',titulo).replace('__','_')
            phone = get_phone(body_texto )
            tags = get_tags(body_texto )
        except :
            return {'info':'Bck - Erro na identificacao dos elementos do HTML'}
            #raise



    try:
        post_dat = time_sec.strftime("%Y-%m-%d, %H:%M:00")
        if not dat_start:
            dat_start =  date(1500,01,01)
            #datetime.strptime('01/01/1500', "%m/%d/%Y")
        if not dat_end:
            dat_end = date(2500,01,01)
            #datetime.strptime('01/01/2500', "%m/%d/%Y")
        #print 'date: %s até %s (%s)'%(dat_start,dat_end,time_sec.date())
        if time_sec.date() >= dat_start and time_sec.date() <=dat_end:
            sel_anuncio = session_cm.query(Anuncios).filter_by(url=link_int).all()

            if not sel_anuncio :
                try:
                    _html = str(soup_int.encode('utf-8','xmlcharrefreplace'))
                except:
                    _html = '<html></html>'
                __Ins =  ' -- Ins Anuncio -- '
                AN =Anuncios(
                    #k=chave(),
                    nome = titulo,
                    #url_id = urlid,
                    url = link_int,
                    html =_html ,
                    #soup_int.encode('utf-8','xmlcharrefreplace'),
                    tags = tags,
                    cidade = str_cidade,
                    estado = str_estado,
                    regiao = str_regiao,
                    sessao = str_sessao,
                    has_phone = phone and 1 or 0,
                    emails_type = tipo_mail,
                    post_date = post_dat,
                    status = '1',
                    customer_id = customer_id,
                    site = link_int[:99]
                )

                if email:
                    __Ins +=  ' ** EMAIL *(%s)* %s '%(email, tipo_mail)
                    __Ins +=  tipo_mail == 0  and 'CRAIGSLIST'  or 'EXTERNAL'
                    AN.anuncioEM=[AnunciosEmails(
                        #k=chave(),
                        nome = email,
                        #url_id = re.sub(r"[^A-Za-z0-9]",'_',email).replace('__','_'),
                        tipo = tipo_mail == 0  and 'CRAIGSLIST'  or 'EXTERNAL',
                        #anuncio= titulo_id,
                        regiao = str_regiao)]
                if phone:
                    __Ins +=  ' ## Phone ## '
                    AN.anuncioPH=[AnunciosTelefones(
                                    #k=chave(),
                                    nome = phone,
                                    #url_id = re.sub(r"[^A-Za-z0-9]",'_',phone).replace('__','_'),
                                    #anuncio= titulo_id
                                    )]
                session_cm.add(AN)
                session_cm.commit()
                return {'info':'Dados Gravado %s'%__Ins}
        else:
            return {'info':'Fora da Data'}
    except:
        session_cm.rollback()
        return {'info':'Nao foi possivel gravar dados no banco de dados'}
        pass
    return {}
