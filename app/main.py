# -*- coding: utf-8 -*-
# main -это точке входа для приложения, т.е отсюда мы его запускаем

# из app.py импортируем экземпляр класса flask (app) который мы будем исп-ть
from app import app
# импортируем view.py
import view
# подключили БД
from app import db

# точка входа
if __name__ == '__main__':
    # метод run  экземпляра класса flask
    app.run()
