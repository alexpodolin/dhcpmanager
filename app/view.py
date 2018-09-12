# -*- coding: utf-8 -*-
# view отвечает за отображение данных ч.з шаблоны

# импортируем наше приложение (переменную) для получения запросов от юзера
# подключим БД для записи
from app import app, db
# render_template - ф-ия котороя занимается обработкой содержимого шаблонов
# Функция flash() — полезный способ показать сообщение пользователю
# request для обработки значений из формы (вставка)
from flask import render_template, redirect, request, url_for, flash
# подключим модели
from models import NetIpv4, HostsAllow, ReservedIpv4, User
# импорт форм
from forms import AddNetIpv4, AddAllowedHost, AddReservedIp, LoginForm
# информация о сетевых интерфейсах
import netifaces
# подключим необходимые функции
from custom_func import ssh_to_dhcp, create_subnet, create_hosts_allow, create_reserved_ip
# логин пользователя
from flask_login import current_user, login_user, logout_user, login_required
# для обработки @login_required
from werkzeug.urls import url_parse


# обращаемся к экземпляру класса flask и методу route
@app.route('/', methods=['GET', 'POST'])
def login() -> 'html':
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()    
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is None or not user.check_password(form.password.data):
            flash('Неверный логин или пароль'.format(
            form.username.data, form.remember_me.data))
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/index', methods=['POST', 'GET'])
@login_required
def index() -> 'html':    
    # добавление в БД значений из формы
    if request.method == 'POST':
        # переменные в полях формы берутся из form.py
        interface = request.form['server_int']
        subnet_ipv4 = request.form['subnet']
        netmask = request.form['netmask']
        default_gw = request.form['gw']
        broadcast = request.form['broadcast']
        ip_range_start = request.form['ip_start']
        ip_range_end = request.form['ip_end']
        dns_sfx = request.form['dns_sfx']
        dns_srv_01 = request.form['dns_prm']
        dns_srv_02 = request.form['dns_sec']
        failover_peer = request.form['failover_peer']
        opt_242 = request.form['vlan_num']
        
        try:
            # имя_столбца_в_БД(как в model.py) = имя_переменной 
            add_subnet = NetIpv4(interface=interface, subnet_ipv4=subnet_ipv4, \
                                 netmask=netmask, default_gw=default_gw, \
                                 broadcast=broadcast, \
                                 ip_range_start=ip_range_start, \
                                 ip_range_end=ip_range_end, dns_suffix=dns_sfx, \
                                 dns_srv_01=dns_srv_01, dns_srv_02=dns_srv_02, \
                                 failover_peer=failover_peer, opt_242=opt_242)            
            db.session.add(add_subnet)
            db.session.commit()
            # соединимся с сервером 
            # создадим dhcpd конфиг при добавлении новой записи в БД
            ssh_to_dhcp()
            create_subnet()
            
        except:
            print('Добавление сети завершилось неудачей')    
        # после выполнения вернемся на нашу страницу
        return redirect( url_for('index') )    
    # форма добавления подсетей для dhcp сервера
    form=AddNetIpv4()
    # html тэг <option> с динамическим выбором
    form.server_int.choices = [(server_int, server_int) for server_int in netifaces.interfaces()]
    form.process()    
    # отображение содержимого таблицы БД
    items=NetIpv4.query.all()
    return render_template('index.html', items=items, form=form)

@app.route('/hosts_allow', methods=['POST', 'GET'])
@login_required
def hosts_allow() -> 'html':
    '''
    #если необходимо вывести определенные столбцы
    items = HostsAllow.query.with_entities(HostsAllow.id, \
                                            HostsAllow.hostname, \
                                            HostsAllow.mac_addr)                                        
    return render_template('hosts_allow.html', items=items)
    ''' 
    if request.method == 'POST':
        hostname = request.form['hostname']
        mac_addr = request.form['mac_addr']
        
        try:
            # имя_переменной = имя_столбца_в_БД
            host_allow = HostsAllow(hostname=hostname, mac_addr=mac_addr)
            db.session.add(host_allow)
            db.session.commit()
            
            ssh_to_dhcp()            
            create_hosts_allow()
            
        except:
            print('Добавление хоста завершилось неудачей')            
        return redirect( url_for('hosts_allow') )
        
    # форма добавления хоста в список разрешенных хостов
    form = AddAllowedHost()    
    # вывод из таблицы списка разрешенных хостов
    items=HostsAllow.query.all()
    return render_template('hosts_allow.html', items=items, form=form)

@app.route('/reserved_ip', methods=['POST', 'GET'])
@login_required
def reserved_ip() -> 'html':
        
    if request.method == 'POST':
        hostname = request.form['hostname']
        ip_addr = request.form['ip_addr']
        mac_addr = request.form['mac_addr']
        
        try:
            reserved_ip = ReservedIpv4(hostname=hostname, mac_addr=mac_addr, \
                                  res_ipv4=ip_addr)
            db.session.add(reserved_ip)
            db.session.commit()
            
            ssh_to_dhcp()            
            create_reserved_ip()
            
        except:
            print('Добавление ip адреса завершилось неудачей')            
        return redirect( url_for('reserved_ip') )
    
    # форма добавления хоста в список разрешенных хостов
    form = AddReservedIp()
    # вывод из таблицы списка зарезервированных ip
    items=ReservedIpv4.query.all()
    return render_template('reserved_ip.html', items=items, form=form)

# админка
@app.route('/admin', methods=['POST', 'GET'])
@login_required
def admin() ->'html':
    return redirect(url_for('admin'))

# страница 404
@app.errorhandler(404)
@login_required
def page_not_found(e) -> 'html':
    return render_template('404.html'), 404
