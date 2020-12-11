from flask import render_template, Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def login():
    return render_template('login.html')

@routes.route('/main', methods=['GET'])
def routes():
    return render_template('main.html')

@routes.route('/zadat_pobyt', methods=['GET'])
def zadat_pobyt():
    return render_template('zadat_pobyt.html')

@routes.route('/zadat_uklid', methods=['GET'])
def zadat_uklid():
    return render_template('zadat_uklid.html')

@routes.route('/zadat_zavadu', methods=['GET'])
def zadat_zavadu():
    return render_template('zadat_zavadu.html')

@routes.route('/pobyty', methods=['GET'])
def pobyty():
    return render_template('pobyty.html')

@routes.route('/uklidy', methods=['GET'])
def uklidy():
    return render_template('uklidy.html')

@routes.route('/uklizeci', methods=['GET'])
def uklizeci():
    return render_template('uklizeci.html')