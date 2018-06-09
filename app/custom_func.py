# -*- coding: utf-8 -*-

# для создания конфига
import shutil
import subprocess
import os
# импортируем модели
from models import ReservedIpv4

def create_reserved_ip_conf_file():    
    # где лежит конфиг
    conf_dir = '/etc/dhcp/conf.d' 
    # имя конф. файла
    conf_path = os.path.join(conf_dir, 'reserved_addr.conf')
    # имя бэкап файла конфига
    conf_path_bkp = os.path.join(conf_dir, 'reserved_addr.conf.bkp')
    # созадим дир. для конифга если не создана
    if not os.path.exists(conf_dir): 
        os.makedirs(conf_dir)
    # Сделаем бэкап файла конфига
    shutil.copy2(conf_path, conf_path_bkp)
    # запрос select
    items = ReservedIpv4.query.all()    
    # формируем конфиг
    with open(conf_path, 'w+') as result:
        for item in items:
            result.write('host ' + item.hostname + ' {' + '\n')
            result.write('    hardware ethernet ' + item.reserved_ipv4 + ';' + '\n')
            result.write('    fixed-address ' + item.mac_addr + ';' + '\n')
            result.write('}' + '\n\n')
        result.close()    
    # Перезапустим dhcp сервис
    retcode = subprocess.call('/usr/bin/systemctl restart dhcpd', shell=True)    
    # Если сервис перезапущен успешно, то завершим работу и удалим .bkp файл
    # если нет, то будем использовать старый конфиг
    if retcode == 0:
        os.remove(conf_path_bkp)
    else:
        shutil.copy2(conf_path_bkp, conf_path)
        subprocess.call('/usr/bin/systemctl restart dhcpd', shell=True)
        os.remove(conf_path_bkp)
