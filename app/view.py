# -*- coding: utf-8 -*-
# view отвечает за отображение данных ч.з шаблоны

# импортируем наше приложение (переменную) для получения запросов от юзера
from app import app

# render_template - ф-ия котороя занимается обработкой содержимого шаблонов
from flask import render_template

# обращаемся к экземпляру класса flask и методу route
@app.route('/')
def index() -> 'html':
    return render_template('index.html')

@app.route('/hosts_allow')
def hosts_allow() -> 'html':
	return render_template('hosts_allow.html')
	
@app.route('/reserved_ip')
def reserved_ip() -> 'html':
	return render_template('reserved_ip.html')
