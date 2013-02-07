# -*- encoding: utf-8 -*-

__author__ = 'Maxwell da Silva Oliveira <maxwbh@gmail.com>'


from hashlib import sha224,md5
from datetime import datetime
import re

EMAIL_ARG =(('<div>','<DIV >', '< DIV aling=\'left\' >', '< DIV aling=\'justfield\' >', '< DIV aling="left" >', '< DIV aling="justfield" >'),
            ('<p>','<P >', '< P aling=\'left\' >', '< P aling=\'justfield\' >', '< P aling="left" >', '< P aling="justfield" >'),)







def chave():
    _a= datetime.now().strftime("%f%Y-%m-%d,%H:%M:%S")
    _c = md5("%sNobody inspects "%_a)
    _v=_c.hexdigest()
    return _v[0:31]
    #return sha224("Nobody inspects %s"%a).hexdigest()[0:31]

def RemoveRepetidosLista(lista):
    t = []
    [ t.append(item) for item in lista if not t.count(item) ]
    return t

def get_phone(data):
    d1 = data
    triplets = re.findall(r"\b(?=((?:\w+(?:\W+|$)){3}))", d1)
    #triplets += re.sub(r"[^0-9 ]",'',d1).split(' ')
    for i in triplets:
        aux = re.sub(r"[^0-9]",'',i)
        if len(aux) == 10:
            return '%3s-%3s-%4s'%(aux[0:3],aux[3:6],aux[6:10])

    return ''


def get_tags(data):

    d1 = re.sub(r"[^A-Za-z0-9 ]",'',data).split(' ')
    d1 = RemoveRepetidosLista(d1)

    return ','.join(n for n in d1)


def check_data(data,keywords=[] ):
    if keywords:
        for k in keywords:
            if k in data:
                return (True,k)
    return (False,)

def scran(data):
    pass

class c():
    pass