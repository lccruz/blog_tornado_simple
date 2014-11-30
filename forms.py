# -*- coding:utf-8 -*-

import os.path

from wtforms.fields import TextField
from wtforms.fields import HiddenField
from wtforms.fields import TextAreaField
from wtforms.fields import SelectMultipleField
from wtforms.fields import FileField
from wtforms.validators import Required
from wtforms.validators import ValidationError
from wtforms_tornado import Form

from util import MultiValueDict
from settings import FACTORY

def monta_tags():
    dao_tag = FACTORY.getTagDao()
    tags = []
    for tag in dao_tag.get_all():
        tag = (str(tag.id), tag.nome)
        tags.append(tag)
    return tags

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
    imagem = FileField(u'Imagem',)
    arquivo = FileField(u'Arquivo',)
    tags = SelectMultipleField(u'Tags', choices= monta_tags())

    def validate_imagem(form, extension):
        if extension in ['.jpg']:
            return True
