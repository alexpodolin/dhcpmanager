# -*- coding: utf-8 -*-
# view отвечает за отображение данных ч.з шаблоны

# импортируем наше приложение (переменную) для получения запросов от юзера
from app import app

# render_template - ф-ия котороя занимается обработкой содержимого шаблонов
from flask import render_template

# подключим модели
from models import NetIpv4, HostsAllow, ReservedIpv4

# обращаемся к экземпляру класса flask и методу route
@app.route('/', methods=['GET', 'POST'])
def index() -> 'html':   
    items=NetIpv4.query.all()
    return render_template('index.html', items=items)


@app.route('/hosts_allow', methods=['GET', 'POST'])
def hosts_allow() -> 'html':

    '''
    #если необходимо вывести определенные столбцы
    items = HostsAllow.query.with_entities(HostsAllow.id, \
                                            HostsAllow.hostname, \
                                            HostsAllow.mac_addr)
                                        
    return render_template('hosts_allow.html', items=items)
    '''
    items=HostsAllow.query.all()
    return render_template('hosts_allow.html', items=items)
	
@app.route('/reserved_ip', methods=['GET', 'POST'])
def reserved_ip() -> 'html':
    items=ReservedIpv4.query.all()
    return render_template('reserved_ip.html', items=items)
