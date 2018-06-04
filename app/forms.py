# -*- coding: utf-8 -*-

from wtforms import Form, validators, StringField

# соотношение м.ж моделями и формами
class AddAllowedHost(Form):
    # в кач-ве аргумента передаем метку label для поля
    hostname = StringField('Имя устройства:',
                           [validators.InputRequired()], 
                           render_kw={"placeholder": "имя устройства",
                                      "maxlength": 20})
    mac_addr = StringField ('mac адрес:',
                            [validators.InputRequired()],
                            render_kw={"placeholder": "mac адрес устройства",
                                       "maxlength": 17,
                                       "size": 17})