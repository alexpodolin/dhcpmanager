# -*- coding: utf-8 -*-

'''
ч.б не записывать все настройки в качестве аргументов при запуске 
приложения в метод run()
мы вынесем их в отдельный файл с отдельным класом
'''
class Configuration(object):
    # подробный вывод
    DEBUG = True
    # подключили БД
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://manager:x3H47AV5@192.168.160.131/dhcpd_new'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://manager:password@192.168.160.131/dhcpd'
    # не отслеживать изменения объектов
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # для flask admin
    SECRET_KEY = 'secret key'
