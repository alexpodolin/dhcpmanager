# -*- coding: utf-8 -*-
# view отвечает за отображение данных ч.з шаблоны

# импортируем наше приложение (переменную) для получения запросов от юзера
from app import app
# render_template - ф-ия котороя занимается обработкой содержимого шаблонов
from flask import render_template
# подключим модели
from models import NetIpv4, HostsAllow, ReservedIpv4
# импорт форм
from forms import AddAllowedHost
# для обработки значений из формы (вставка)
from flask import request
# подключим БД для записи
from app import db
# для редиректа
from flask import redirect, url_for

# обращаемся к экземпляру класса flask и методу route
@app.route('/', methods=['GET', 'POST'])
def index() -> 'html':
    # обработка формы      
#    choose_interface = request.args.get('choose_interface')
#    subnet = request.args.get('subnet')
#    netmask = request.args.get('netmask')
#    gw = request.args.get('gw')
#    broadcast = request.args.get('broadcast')
#    ip_start = request.args.get('ip_start')
#    ip_end = request.args.get('ip_end')
#    failover_peer = request.args.get('failover_peer')
#    opt_242 = request.args.get('opt_242')    
    # отображение содержимого таблицы БД
    items=NetIpv4.query.all()
    return render_template('index.html', items=items)

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
	
@app.route('/reserved_ip', methods=['GET', 'POST'])
def reserved_ip() -> 'html':
    items=ReservedIpv4.query.all()
    return render_template('reserved_ip.html', items=items)
