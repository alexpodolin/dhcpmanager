class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://manager:password@localhost/dhcpd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False