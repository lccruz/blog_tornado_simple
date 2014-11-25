# -*- coding:utf-8 -*-

import os.path

from wtforms.fields import TextField
from wtforms.fields import HiddenField
from wtforms.fields import TextAreaField
from wtforms.validators import *
from wtforms_tornado import Form

from util import MultiValueDict

class BaseForm(Form):
  def __init__(self, handler=None, obj=None, prefix='', formdata=None, **kwargs):
    if handler:
      formdata = MultiValueDict()
      for name in handler.request.arguments.keys():
        formdata.setlist(name, handler.get_arguments(name))
    Form.__init__(self, formdata, obj=obj, prefix=prefix, **kwargs)


class FormTag(BaseForm):
    id = HiddenField('id',)
    nome = TextField(u'Nome da Tag', validators=[Required()])


class FormPost(BaseForm):
    id = HiddenField('id',)
    titulo = TextField(u'Titulo', validators=[Required()])
    conteudo = TextAreaField(u'Conteudo', validators=[Required()])
