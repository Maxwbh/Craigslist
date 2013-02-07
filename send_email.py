# -*- encoding: utf-8 -*-
__author__ = 'Maxwell da Silva Oliveira <maxwbh@gmail.com>'



import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep
import logging
import urllib
from datetime import datetime,timedelta, date, time
import re
from bs4 import BeautifulSoup
from sqlalchemy import (create_engine, Column, Integer,
                        String, DateTime,Text, text, Float, ForeignKey, and_,or_)
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import (IntegrityError, OperationalError)

from class_map import *
from util import *

if __name__ == "__main__":
    # """Executes if the script is run as main script (for testing purposes)"""

    random.seed()
    email_titulo=["RES:(%s) - %s","%s %s","RES : %s (%s)","res:%s(%s)"]
    email_stil =["""<style type="text/css" media="screen">
                        table{
                            background-color: #AABB%2d;
                            empty-cells:hide;
                        }
                        td.cell{
                            background-color: white;
                        }
                    </style>
            ""","""<style type="text/css" media="screen">
                        table{
                            background-color: white;
                            empty-cells:hide;
                        }
                        td.cell{
                            background-color: #AABB%2d;
                        }
                    </style>
            ""","""<style type="text/css" media="screen">
                        table{
                            background-color: white;
                            empty-cells:hide;
                        }
                        td.cell{
                            background-color: #00BB%2d;
                        }
                    </style>
            """, """<style type="text/css" media="screen">
                        td.cell{
                            background-color: #AA00%2d;
                        }
                    </style>  """, """<style type="text/css" media="screen">
                        td.cell{
                            background-color: #BB00%2d;
                        }
                    </style>  """]

    email_table = ["""
            <table style="border: blue 1px solid;">
                <tr><td class="cell">%s</td><td class="cell">%s</td></tr>
            </table>""","""
            <table style="border: blue 1px solid;">
                <tr><td class="cell">%s</td></tr><tr><td class="cell">%s</td></tr>
            </table>""","""
            <table style="border: blue 1px solid;">
                <tr><td class="cell">%s<br>%s</td></tr>
            </table>""","""
            <table>
                <tr><td class="cell"><p>%s<br>%s</p></td></tr>
            </table>""","""<p>%s<br>%s</p> """
    ]
    email_content = """
            <head>
              <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
              <title>%s</title> """+ email_stil[random.randint(0,4)] + """
            </head>
            <body>
                <div>
                    %s
                </div>
                <div> """+email_table[random.randint(0,4)]  +"""
                </div>
            </body>
    """

    _TO = 'gsantos@webinnovative.com'
    wait  = 0
    #logging.basicConfig()
    #
    # logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    while wait  < 5:
        dt_serv = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        print '-------------------------'
        sel_smtp_ = session.query( Smtp ).filter( or_(Smtp.dta_proximo_envio <= dt_serv ,Smtp.dta_proximo_envio == None),or_(Smtp.qtde_enviada <= Smtp.limite_envio,Smtp.limite_envio==0),Smtp.status == 1).order_by(Smtp.dta_proximo_envio).all()
        print '-------------------------'
        # or_(Smtp.qtde_enviada <= Smtp.limite_envio,Smtp.limite_envio==0),    ---> Quantidade Maxima por dia
        for sel_smtp in sel_smtp_:
            sel_news =session.query( NewsLetters ).filter_by(usuarios_id = sel_smtp.usuarios_id).all()
            if not sel_news:
                print 'Volta....'
                break

            wait = 0
            PASSWORD = sel_smtp.senha
            FROM =sel_smtp.usuario
            HOST= sel_smtp.nome
            PORT= '%s'%sel_smtp.porta
            SSL =sel_smtp.seguro == 1
            try:
                print '==== FROM :',FROM

                server = smtplib.SMTP(host=HOST,port=PORT)
                print 'Login..'

                # Print debugging output when testing
                server.set_debuglevel(0)

                if SSL:
                    print 'SSL....'
                    server.starttls()
                    print 'Start'
                    server.login(FROM,PASSWORD)
                    print 'Login...'
                else:
                    print 'Login...'
                    server.login(FROM,PASSWORD)
                print 'xxxxx'
                """
                Sql p/ restringir localidade de envio
                SELECT * FROM emailtooltest.regioes where CURRENT_TIME()> inicio and CURRENT_TIME()< fim;
                """
                sel_anuncio = session.query( Anuncios).filter_by( status=1, newsletters_id = None).limit(sel_smtp.qtde_max_envio).all()
                print '----'
                qtdEnvio = min(sel_smtp.qtde_max_envio,len(sel_anuncio) )
                print 'zz ',qtdEnvio
                for i in range(0,qtdEnvio):
                    print 'i ',i
                    sel_to_mail_ = session.query( AnunciosEmails ).filter_by(anuncios_id = sel_anuncio[i].id).all()
                    body_id = random.randint(0,len(sel_news)-1)

                    for sel_to_mail in sel_to_mail_:

                        cor = random.randint(0,99)
                        tm = datetime.now().strftime("%Y-%m-%d, %H:%M:%S, %f")
                        body = '<br>'*random.randint(0,2)+sel_news[body_id].texto+'<br>'*random.randint(0,9)
                        TO = '"%s" <%s>'%(sel_to_mail.nome,_TO)
                        _chave = chave()

                        body_email = email_content %(sel_anuncio[i].nome,cor , body, tm,_chave )

                        SUBJECT = sel_news[body_id].titulo

                        #email_titulo[random.randint(0,len(email_titulo)-1)] \
                        #          %(sel_anuncio[i].nome, _chave)

                        BODY=body_email

                        #'With this function we send out our html email '

                        # Create message container - the correct MIME type is multipart/alternative here!
                        MESSAGE = MIMEMultipart('alternative')
                        MESSAGE['To'] = TO
                        MESSAGE['From'] = FROM
                        MESSAGE['subject'] = SUBJECT
                        MESSAGE['Message-ID']= _chave
                        print '----Aqui 1'
                        MESSAGE.preamble =BeautifulSoup(BODY).text.encode('ascii','xmlcharrefreplace')
                        print '----Aqui 2'
                        # Record the MIME type text/html.
                        HTML_BODY = MIMEText(BODY, 'html')
                        print '----Aqui 3'
                        # Attach parts into message container.
                        # According to RFC 2046, the last part of a multipart message, in this case
                        # the HTML message, is best and preferred.
                        MESSAGE.attach(HTML_BODY)
                        print '----Aqui 4'
                        print '--# Send ...'
                        server.sendmail(FROM, [TO], MESSAGE.as_string())
                        print 'Foi...'
                        print 'Grava Campos...'
                        sel_to_mail.send_key = _chave
                        sel_to_mail.send_date = datetime.now()
                        session.add(sel_to_mail)
                        sel_anuncio[i].newsletters_id = sel_news[body_id].id
                        sel_smtp.qtde_enviada = sel_smtp.qtde_enviada+1
                        sel_smtp.dta_proximo_envio = datetime.now() + timedelta(seconds=sel_smtp.qtde_seg_envio)
                        if sel_smtp.qtde_enviada == sel_smtp.limite_envio:
                            print '## proximo Dia ###'
                            sel_smtp.dta_proximo_envio = datetime.strptime(datetime.now().strftime('%d%m%Y'),'%d%m%Y') + timedelta(Days=1)
                            sel_smtp.qtde_enviada = 0
                        session.commit()
                    print 'Enviado e Gravado'
                    sel_anuncio[i].status = 0
                    session.add(sel_anuncio[i])
                    session.add(sel_smtp)
                session.commit()
                server.quit()
            except Exception as inst:
                #x = inst.args[0].values()[0]
                #print 'Type x', type(x)
                #print 'Erro:',x
                #                sel_smtp.status = 4
                #                session.add(sel_smtp)
                #                session.commit()
                raise

    else:
        print 'Aguardando....'
        sleep(.30)
        wait += 1
    print 'Foi....'



