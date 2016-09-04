#!/usr/bin/env python
''' Funciones auxiliares'''

from datetime import datetime
import hashlib

def generate_id():
    ''' Genera un identificador a partir de la fecha/hora
        return Un identificador hexadecimal'''
    tmstmp = str(datetime.utcnow())
    digest = md5.new()
    digest.update(tmstmp)
    ident = str(digest.hexdigest())
    return ident

