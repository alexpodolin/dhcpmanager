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
# подключим админку
from flask_admin import Admin
# русификация админки
from flask_babelex import Babel
'''
переменная для приложения на flask
вызвали конструктор класса flask и передали ей параметр __name__
__name__ это имя текущего файла (app.py)
отталкиваясь от имени файла (пути) ищем остальные файлы
по сути мы создали приложение
'''
app = Flask(__name__)
# русификация админки
babel = Babel(app)

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

### ADMIN ###
# имопртируем модели
from flask_admin.contrib.sqla import ModelView
from models import NetIpv4, HostsAllow, ReservedIpv4
# подключим админку
admin = Admin(app)
admin.add_view(ModelView(NetIpv4, db.session, 'Доступные подсети'))
admin.add_view(ModelView(HostsAllow, db.session, 'Разрешенные хосты'))
admin.add_view(ModelView(ReservedIpv4, db.session, 'Зарезервированные ip'))

# русификация админки
@babel.localeselector
def get_locale():
        return 'ru'
