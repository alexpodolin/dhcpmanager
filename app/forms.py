# -*- coding: utf-8 -*-

# соотношение м.у моделями и формами
from wtforms import Form, validators, SelectField, StringField, \
                    PasswordField, BooleanField, SubmitField
                    
from flask_wtf import FlaskForm
# проверка корректности введенных значений
from wtforms.validators import DataRequired

# информация о сетевых интерфейсах
import netifaces

# форма настройки конифгурации подсети
class AddNetIpv4(Form):    
    # html тэг <option> с динамическим выбором
    server_int = SelectField('Выберите сетевой интерфейс:', choices=netifaces.interfaces() )
    subnet = StringField('Адрес подсети:',
                          [validators.InputRequired()], 
                          render_kw={"placeholder": "subnet ip",
                                     "pattern": "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
                                     "maxlength": 15,
                                     "size": 15})
    netmask = StringField('Маска подсети:',
                          [validators.InputRequired()], 
                          render_kw={"placeholder": "subnet mask",
                                     "pattern": "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
                                     "maxlength": 15,
                                     "size": 15})
    gw = StringField('Шлюз по умолчанию:',
                     [validators.InputRequired()], 
                     render_kw={"placeholder": "default gateway",
                                "pattern": "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
                                "maxlength": 15,
                                "size": 15})
    broadcast = StringField('Широковещательный адрес:',
                            [validators.InputRequired()],
                            render_kw={"placeholder": "broadcast address",
                                       "pattern": "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
                                       "maxlength": 15,
                                       "size": 15})
    ip_start = StringField('Начальный адрес диапазона:',
                           [validators.InputRequired()],
                           render_kw={"placeholder": "start ip",
                                      "pattern": "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
                                      "maxlength": 15,
                                      "size": 15})
    ip_end = StringField('Конечный адрес диапазона:',
                            [validators.InputRequired()],
                            render_kw={"placeholder": "end ip",
                                       "pattern": "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
                                       "maxlength": 15,
                                       "size": 15})
    dns_sfx = StringField('Доменное имя (dns суффикс):',
                            [validators.InputRequired()],
                            render_kw={"maxlength": 30,
                                       "size": 30,
                                       "value": "nr.local"})
    dns_prm = StringField('Dns сервер основной:',
                            [validators.InputRequired()],
                            render_kw={"maxlength": 15,
                                       "size": 15,
                                       "value": "192.168.156.93"})
    dns_sec = StringField('Dns сервер резервный:',
                            [validators.InputRequired()],
                            render_kw={"maxlength": 15,
                                       "size": 15,
                                       "value": "192.168.156.94"})    
    failover_peer = StringField('Failover peer:',
                            [validators.InputRequired()],
                            render_kw={"placeholder": "Failover peer",
                                       "value": "nr-dhcpd-failover"})
    
    opt_242 = StringField('Опция 242:',
                          [validators.InputRequired()],
                          render_kw={"placeholder": "Option 242",
                                     "size": 150,
                                     "value": "MCIPADD=10.16.233.30,MCPORT=1719,TLSSRVR=10.16.233.23,HTTPSRVR=10.16.233.23,L2Q=1,L2QVLAN=XXX,VLANTEST=0"})
    
    '''
    vlan_num = StringField('Номер vlan:',
                          [validators.InputRequired()],
                          render_kw={"placeholder": "Номер vlan для option 242",
                                     "size": 4})
    '''
# форма добавления хоста
class AddAllowedHost(Form):
    # в кач-ве аргумента передаем метку label для поля
    hostname = StringField('Имя устройства:',
                           [validators.InputRequired()], 
                           render_kw={"placeholder": "имя устройства",
                                      "maxlength": 20})
    mac_addr = StringField('mac адрес:',
                           [validators.InputRequired()],
                           render_kw={"placeholder": "mac адрес устройства",
                                      "maxlength": 17,
                                      "size": 17})
# форма резервирования ip адреса
class AddReservedIp(Form):
    hostname = StringField('Имя устройства:',
                           [validators.InputRequired()], 
                           render_kw={"placeholder": "имя устройства",
                                      "maxlength": 20})
    ip_addr = StringField('ip адрес:',
                          [validators.InputRequired()], 
                          render_kw={"placeholder": "ip адрес устройства",
                                     "pattern": "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
                                     "maxlength": 15})
    mac_addr = StringField('mac адрес:',
                           [validators.InputRequired()],
                           render_kw={"placeholder": "mac адрес устройства",
                                      "maxlength": 18,
                                      "size": 18})

# форма авторизации
class LoginForm(FlaskForm):
    username = StringField('Имя пользователя:', 
                           validators=[DataRequired()],
                           render_kw={"placeholder": "Введите логин"})
    password = PasswordField('Пароль:', 
                             validators=[DataRequired()],
                             render_kw={"placeholder": "Введите пароль"})
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')