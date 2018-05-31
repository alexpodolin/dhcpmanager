# -*- coding: utf-8 -*-

# подключим flask
from flask import Flask
# импортируем в  наше приложение класс Configuration для его использования
from config import Configuration
# подключили SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# подключим возможность миграции
from flask_migrate import Migrate, MigrateCommand
# водключим возможность управления миграциями
from flask_script import Manager

'''
переменная для приложения на flask
вызвали конструктор класса flask и передали ей параметр __name__
__name__ это имя текущего файла (app.py)
отталкиваясь от имени файла (пути) ищем остальные файлы
по сути мы создали приложение
'''
app = Flask(__name__)

'''
метод from_object передает в словарь config из объекта object(Configuration)
наполняет свойствами т.е. настройками приложения
узнать методы и свойства объекта можно из консоли с помощью метода dir()
написав там
from flask import Flask
app = Flask(__name__)
dir(app)
dir - Возвращает имена [переменных], доступные в локальной области,
либо атрибуты указанного объекта (модуля, функции, строки, списка, словаря…)
в алфавитном порядке.
'''
app.config.from_object(Configuration)

# создали экземпляр класса SQLAlchemy
db = SQLAlchemy(app)

# возможность миграции и использования команд для миграции
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

