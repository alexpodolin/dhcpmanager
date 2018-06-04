<<<<<<< HEAD
# -*- coding: utf-8 -*-
# в этом файле описываем возмождность управления миграциями

# импортируем manager
from app import manager

# импортируем все из main (БД, модели)
from main import *

if __name__ =='__main__':
    manager.run()
    
    
# =============================================================================
# Инициализируем БД из консоли python
# (C:\ProgramData\Anaconda3) C:\Users\podolin\Documents\GitHub\dhcpmanager\app>python manage.py db init
# 
# После добавления модели
# (C:\ProgramData\Anaconda3) C:\Users\podolin\Documents\GitHub\dhcpmanager\app>python manage.py db migrate
# 
# Для приминения изминений
# (C:\ProgramData\Anaconda3) C:\Users\podolin\Documents\GitHub\dhcpmanager\app>python manage.py db upgrade
    
# (C:\ProgramData\Anaconda3) C:\Users\podolin\Documents\GitHub\dhcpmanager\app>python manage.py db --help
# =============================================================================
=======
# -*- coding: utf-8 -*-
# в этом файле описываем возмождность управления миграциями

# импортируем manager
from app import manager

# импортируем все из main (БД, модели)
from main import *

if __name__ =='__main__':
    manager.run()
    
    
# =============================================================================
# Инициализируем БД из консоли python
# (C:\ProgramData\Anaconda3) C:\Users\podolin\Documents\GitHub\dhcpmanager\app>python manage.py db init
# 
# После добавления модели
# (C:\ProgramData\Anaconda3) C:\Users\podolin\Documents\GitHub\dhcpmanager\app>python manage.py db migrate
# 
# Для приминения изминений
# (C:\ProgramData\Anaconda3) C:\Users\podolin\Documents\GitHub\dhcpmanager\app>python manage.py db upgrade
# =============================================================================
>>>>>>> b112296601b74f2f2e19e829e30ebf99975e475f
