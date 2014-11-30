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

def delete_arquivo(arquivonome, local=True):
    try:
        if not local:
            arquivonome = 'static/upload/%s' % (arquivonome)
        os.remove(arquivonome)
        return True
    except:
        return False

def read_arquivo(arquivonome):
    try:
        filename = 'static/upload/%s' % (arquivonome)
        arquivo = open(filename,'rb')
        return arquivo.read()
    except:
        return False

def rename_arquivo(arquivonome, new_name):
    try:
        filename = 'static/upload/%s' % (arquivonome)
        filename_new = 'static/upload/%s.jpg' % (new_name)
        os.rename(filename, filename_new)
        return True
    except:
        return False

