# -*- coding: utf-8 -*-

import md5


def convert_md5(password):
    """Converte o password para md5
    """
    password = md5.md5(password).hexdigest()
    return password
