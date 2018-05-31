from app import db

class Net_ipv4(db.Model):
    id = db.Column(db.SmallInteger(5), primary_key=True, autoincrement=True)
	interface = db.Column(db.Varchar(15), nullable=True)
	subnet_ipv4 = db.Column(db.Integer(15), nullable=True)
	netmask = db.Column(db.Integer(15), nullable=True)
	default_gw = db.Column(db.Integer(15), nullable=True)
	broadcast = db.Column(db.Integer(15), nullable=True)
	ip_range_start = db.Column(db.Integer(15), nullable=True)
	ip_range_end = db.Column(db.Integer(15), nullable=True)
	failover_peer = db.Column(db.Varchar(20), nullable=True, default='nr-dhcpd-failover')
	opt_242 = db.Column(db.Varchar(150), nullable=False)
	 
	# создадим конструктор класса
	#def __init__(self, interface, subnet_ipv4, netmask, default_gw, broadcast, ip_range_start, ip_range_end, failover_peer, opt_242):
	def __init__(self, *args, **kwargs):
		'''
	    self.interface = interface
		self.subnet_ipv4 = subnet_ipv4
		self.netmask = netmask
		self.default_gw = default_gw
		self.broadcast = broadcast
		self.ip_range_start = ip_range_start
		self.ip_range_end = ip_range_end
		self.failover_peer = failover_peer
		self.opt_242 = opt_242		
		'''
	    super(Net_ipv4, self).__init__(*args, **kwargs)
		
	def __repr__(self):
	    return '<Net_ipv4 id: {}, interface: {}, subnet_ipv4: {}, netmask: {}, default_gw: {}, broadcast: {}, ip_range_start: {}, ip_range_end: {}, failover_peer: {}, opt_242: {} >'.format(self.id, self.interface, self.subnet_ipv4, self.netmask, self.default_gw, self.broadcast, self.ip_range_start, self.ip_range_end, self.failover_peer, self.opt_242)
		
		