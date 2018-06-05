# -*- coding: utf-8 -*-
# view отвечает за отображение данных ч.з шаблоны

# импортируем наше приложение (переменную) для получения запросов от юзера
from app import app
# render_template - ф-ия котороя занимается обработкой содержимого шаблонов
from flask import render_template
# подключим модели
from models import NetIpv4, HostsAllow, ReservedIpv4
# импорт форм
from forms import AddNetIpv4, AddAllowedHost, AddReservedIp
# для обработки значений из формы (вставка)
from flask import request
# подключим БД для записи
from app import db
# для редиректа
from flask import redirect, url_for

# обращаемся к экземпляру класса flask и методу route
@app.route('/', methods=['POST', 'GET'])
def index() -> 'html':    
    # форма добавления подсетей для dhcp сервера
    form=AddNetIpv4()   
    # отображение содержимого таблицы БД
    items=NetIpv4.query.all()
    return render_template('index.html', items=items, form=form)

@app.route('/hosts_allow', methods=['POST', 'GET'])
def hosts_allow() -> 'html':
    '''
    #если необходимо вывести определенные столбцы
    items = HostsAllow.query.with_entities(HostsAllow.id, \
                                            HostsAllow.hostname, \
                                            HostsAllow.mac_addr)
                                        
    return render_template('hosts_allow.html', items=items)
    '''
    # добавление значений из формы
    if request.method == 'POST':
        hostname = request.form['hostname']
        mac_addr = request.form['mac_addr']
        
        try:
            # имя_переменной = имя_столбца_в_БД
            host_allow = HostsAllow(hostname=hostname, mac_addr=mac_addr)
            db.session.add(host_allow)
            db.session.commit()
        except:
            print('Добавление хоста завершилось неудачей')            
        return redirect( url_for('hosts_allow') )
        
    # форма добавления хоста в список разрешенных хостов
    form = AddAllowedHost()    
    # вывод из таблицы списка разрешенных хостов
    items=HostsAllow.query.all()
    return render_template('hosts_allow.html', items=items, form=form)
	
@app.route('/reserved_ip', methods=['POST', 'GET'])
def reserved_ip() -> 'html':
    if request.method == 'POST':
        hostname = request.form['hostname']
        ip_addr = request.form['ip_addr']
        mac_addr = request.form['mac_addr']
        
        try:
            reserved_ip = ReservedIpv4(hostname=hostname, mac_addr=mac_addr, \
                                  reserved_ipv4=ip_addr)
            db.session.add(reserved_ip)
            db.session.commit()
        except:
            print('Добавление ip адреса завершилось неудачей')            
        return redirect( url_for('reserved_ip') )
    
    # форма добавления хоста в список разрешенных хостов
    form = AddReservedIp()
    # вывод из таблицы списка зарезервированных ip
    items=ReservedIpv4.query.all()
    return render_template('reserved_ip.html', items=items, form=form)
