# -*- coding: utf-8 -*-

import md5
import os

def convert_md5(password):
    """Converte o password para md5
    """
    password = md5.md5(password).hexdigest()
    return password

def save_arquivo(arquivoconteudo, arquivonome):
    try:
        filename = 'static/upload/%s' % (arquivonome)
        arquivo = open(filename,'w')
        arquivo.write(arquivoconteudo)
        arquivo.close()
        return filename
    except:
        return False

def delete_arquivo(arquivonome):
    try:
        os.remove(arquivonome)
        return True
    except:
        return False
