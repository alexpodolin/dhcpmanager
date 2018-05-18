from app import app
from flask import render_template

@app.route('/')
def index() -> 'html':
    return render_template('index.html')

@app.route('/hosts_allow')
def hosts_allow() -> 'html':
	return render_template('hosts_allow.html')
	
@app.route('/reserved_ip')
def reserved_ip() -> 'html':
	return render_template('reserved_ip.html')
