# -*- coding: utf-8 -*-
# соотношение м.у моделями и формами
from wtforms import Form, validators, SelectField, StringField

# информация о сетевых интерфейсах
import netifaces

# форма настройки конифгурации подсети
class AddNetIpv4(Form):  
#    def get_interface_name():        
#        interface_list = netifaces.interfaces()
#        return interface_list    
    
    server_int = SelectField('Выберите сетвой интерфейс:', choices=netifaces.interfaces() )
        

#    server_int = StringField('Введите сетевой интерфейс:',
#                          [validators.InputRequired()], 
#                          render_kw={"placeholder": "server interface",
#                                     "maxlength": 10,
#                                     "size": 10})         
            
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
    failover_peer = StringField('Failover peer:',
                            [validators.InputRequired()],
                            render_kw={"placeholder": "Failover peer",
                                       "pattern": "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
                                       "maxlength": 15,
                                       "size": 15,
                                       "value": "nr-dhcpd-failover"})
    opt_242 = StringField('Опция 242:',
                          [validators.InputRequired()],
                          render_kw={"placeholder": "Option 242",
                                     "size": 150,
                                     "value": "MCIPADD=10.16.233.30,MCPORT=1719,TLSSRVR=10.16.233.23,HTTPSRVR=10.16.233.23,L2Q=1,L2QVLAN=XXX,VLANTEST=0"})

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
                                      "maxlength": 15})
    mac_addr = StringField('mac адрес:',
                           [validators.InputRequired()],
                           render_kw={"placeholder": "mac адрес устройства",
                                       "maxlength": 17,
                                       "size": 17})
