# -*- coding: utf-8 -*-

# для ssh соединения с серверами
import paramiko

# для создания конфига
import shutil
import subprocess
import os

# импортируем модели
from models import NetIpv4, HostsAllow, ReservedIpv4

# соединимся с двумя dhcp серверами
def ssh_to_dhcp():
#    srv_list = ['nr-dhcp-01', 'nr-dhcp-02']
    srv_list = ['localhost']
    
    for srv in srv_list:
        # Cоздаем объект ssh класса SSHClient
        ssh = paramiko.SSHClient()
        # Для автоматизации принятия ключа в paramiko
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # подключение 
        ssh.connect(srv, username='podolin', key_filename='/root/.ssh/id_rsa')


# создание конфига списка подсетей
def create_subnet():     
    # где лежит конфиг
    conf_dir = '/etc/dhcp/conf.d' 
    # имя конф. файла
    conf_path = os.path.join(conf_dir, 'subnets.conf')
    # имя бэкап файла конфига
    conf_path_bkp = os.path.join(conf_dir, 'subnets.conf.bkp')
    # созадим директорию для конифга если не создана
    if not os.path.exists(conf_dir): 
        os.makedirs(conf_dir)
    # Сделаем бэкап файла конфига
    shutil.copy2(conf_path, conf_path_bkp)
    # запрос select
    items = NetIpv4.query.all()    
    # формируем конфиг
    with open(conf_path, 'w+') as result:
        for item in items:
            result.write('subnet ' + item.subnet_ipv4 + ' netmask ' + item.netmask + ' {' + '\n')
            result.write('  interface\t\t\t' + '"'+ item.interface + '"' + ';' + '\n')
            result.write('  option routers\t\t' + item.default_gw + ';' + '\n')
            result.write('  option subnet-mask\t\t' + item.netmask + ';' + '\n')
            result.write('  option broadcast-address\t' + item.broadcast + ';' + '\n')
            
            result.write('  option domain-name\t\t' + item.dns_suffix + ';' + '\n')
            result.write('  option domain-name-servers\t' + item.dns_srv_01 + ', ' + item.dns_srv_02 + ';' + '\n')
            
            result.write('  option avaya-242\t\t' + '"' + item.opt_242 + '";' + '\n\n')
            result.write('  pool {' + '\n')
            result.write('    deny\t\tunknown-clients;' + '\n')
            result.write('    range\t\t' + item.ip_range_start + ' ' + item.ip_range_end + ';' + '\n')
            result.write('    failover peer \t"' + item.failover_peer + '";' +'\n')
            result.write('  }' + '\n')
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

# создание конфига списка разрешенных хостов
def create_hosts_allow():     
    conf_dir = '/etc/dhcp/conf.d' 
    conf_path = os.path.join(conf_dir, 'hosts_allow.conf')
    conf_path_bkp = os.path.join(conf_dir, 'hosts_allow.conf.bkp')
    if not os.path.exists(conf_dir): 
        os.makedirs(conf_dir)
    shutil.copy2(conf_path, conf_path_bkp)
    items = HostsAllow.query.all()    
    with open(conf_path, 'w+') as result:
        for item in items:
            result.write('host ' + item.hostname + ' { hardware ethernet ' + item.mac_addr + '; }' + '\n')
        result.close() 
    retcode = subprocess.call('/usr/bin/systemctl restart dhcpd', shell=True) 
    if retcode == 0:
        os.remove(conf_path_bkp)
    else:
        shutil.copy2(conf_path_bkp, conf_path)
        subprocess.call('/usr/bin/systemctl restart dhcpd', shell=True)
        os.remove(conf_path_bkp)
        
# создание конфига резервирования ip адреса
def create_reserved_ip():
    conf_dir = '/etc/dhcp/conf.d' 
    conf_path = os.path.join(conf_dir, 'reserved_addr.conf')
    conf_path_bkp = os.path.join(conf_dir, 'reserved_addr.conf.bkp')
    if not os.path.exists(conf_dir): 
        os.makedirs(conf_dir)
    shutil.copy2(conf_path, conf_path_bkp)
    items = ReservedIpv4.query.all()    
    with open(conf_path, 'w+') as result:
        for item in items:
            result.write('host ' + item.hostname + ' {' + '\n')
            result.write('    hardware ethernet ' + item.reserved_ipv4 + ';' + '\n')
            result.write('    fixed-address ' + item.mac_addr + ';' + '\n')
            result.write('}' + '\n\n')
        result.close()
    retcode = subprocess.call('/usr/bin/systemctl restart dhcpd', shell=True)
    if retcode == 0:
        os.remove(conf_path_bkp)
    else:
        shutil.copy2(conf_path_bkp, conf_path)
        subprocess.call('/usr/bin/systemctl restart dhcpd', shell=True)
        os.remove(conf_path_bkp)
