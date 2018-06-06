# -*- coding: utf-8 -*-
# файл в котором хранятся описания моделей 

'''
в консоли сервера
# python3.4    
>>> import models
>>> from app import db
>>> db.create_all()
БД должна быть создана и прописаны GRANT`ы
'''

# импортируем созданную БД
from app import db
'''
класс котоый отвечает за хранение инф. о настройках конфигурации
dhcpd сервера. Он наследует свойства от класса Model SQLAlchemy
'''
class NetIpv4(db.Model):
    # таблица настроек которые раздает dhcp сервер
    id = db.Column(db.SmallInteger(), primary_key=True, autoincrement=True)
    interface = db.Column(db.VARCHAR(15), nullable=False)
    subnet_ipv4 = db.Column(db.VARCHAR(15), nullable=False)
    netmask = db.Column(db.VARCHAR(15), nullable=False)
    default_gw = db.Column(db.VARCHAR(15), nullable=False)
    broadcast = db.Column(db.VARCHAR(15), nullable=False)
    ip_range_start = db.Column(db.VARCHAR(15), nullable=False)
    ip_range_end = db.Column(db.VARCHAR(15), nullable=False)
    failover_peer = db.Column(db.VARCHAR(20), nullable=False, \
                              server_default='nr-dhcpd-failover')
    opt_242 = db.Column(db.VARCHAR(150), nullable=True)
	 
    # мы определили свойства класса (свойства таблицы) выше, теперь определим
    # конструктор класса
    # def __init__(self, interface, subnet_ipv4, netmask, default_gw, broadcast, ip_range_start, ip_range_end, failover_peer, opt_242):
    def __init__(self, *args, **kwargs):
        # * позиционные аргументы в любом количестве (список)
        # ** именованные аргументы в любом количестве(словарь)
        # вызвали конструктор класса Model, это предок класса NetIpv4        
        super(NetIpv4, self).__init__(*args, **kwargs)        
        '''
        self.interface = interface
        self.subnet_ipv4 = subnet_ipv4
        self.netmask = netmask
        self.default_gw = default_gw
        self.broadcast = broadcast
        self.ip_range_start = ip_range_start
        self.ip_range_end = ip_range_end
        self.failover_peer = failover_peer
        self.opt_242 = opt_242
        '''
    # вызывается встроенной функцией repr; возвращает "сырые" данные, 
    # использующиеся для внутреннего представления в python.
    # метод формат подставляет в {} данные
    def __repr__(self):
        return '<NetIpv4 id: {}, interface: {}, subnet_ipv4: {}, netmask: {}, \
                          default_gw: {}, broadcast: {}, ip_range_start: {}, \
                          ip_range_end: {}, failover_peer: {}, opt_242: {} >' \
                          .format(self.id, self.interface, self.subnet_ipv4, \
                                  self.netmask, self.default_gw, \
                                  self.broadcast, self.ip_range_start, \
                                  self.ip_range_end, self.failover_peer, \
                                  self.opt_242)

class HostsAllow(db.Model):
    # список хостов, которые получают настройки по dhcp сервера
    id = db.Column(db.SmallInteger(), primary_key=True, autoincrement=True)
    hostname = db.Column(db.VARCHAR(32), nullable=False)
    mac_addr = db.Column(db.VARCHAR(18), nullable=False, unique=True)
    
    def __init__(self, *args, **kwargs):
        super(HostsAllow, self).__init__(*args, **kwargs)
        
    def __repr__(self):
        return'<HostsAllow id: {}, hostname: {}, mac_addr: {}>' \
        .format(self.id, self.hostname, self.mac_addr)
        
class ReservedIpv4(db.Model):
    # список хостов, для которых зарезервированы ip адреса
    id = db.Column(db.SmallInteger(), primary_key=True, autoincrement=True)
    hostname = db.Column(db.VARCHAR(32), nullable=False)
    mac_addr = db.Column(db.VARCHAR(18), nullable=False, unique=True)
    reserved_ipv4 = db.Column(db.VARCHAR(15), nullable=False, unique=True)
    
    def __init__(self, *args, **kwargs):
        super(ReservedIpv4, self).__init__(*args, **kwargs)
        
    def __repr__(self):
        return'<ReservedIpv4 id: {}, hostname: {}, mac_addr: {} reserved_ipv4: {}>' \
        .format(self.id, self.hostname, self.mac_addr, self.reserved_ipv4)                        