from flask import render_template, Blueprint

from web_app.models import *

routes = Blueprint('routes', __name__)

@routes.route('/')
def login():
    return render_template('login.html')

@routes.route('/main', methods=['GET'])
def main():
    return render_template('main.html')

@routes.route('/zadat_pobyt', methods=['GET'])
def zadat_pobyt():
    return render_template('zadat_pobyt.html')


@routes.route('/zadat_zavadu', methods=['GET'])
def zadat_zavadu():
    return render_template('zadat_zavadu.html')

@routes.route('/pobyty', methods=['GET'])
def pobyty():
    return render_template('pobyty.html')

@routes.route('/zadat_uklizeci', methods=['GET'])
def zadat_uklizeci():
    return render_template('zadat_uklizeci.html')

@routes.route('/uklizeci', methods=['GET'])
def uklizeci():
    return render_template('uklizeci.html')

@routes.route('/zadat_uklid', methods=['GET'])
def zadat_uklid():
    return render_template('zadat_uklid.html')

@routes.route('/zavady', methods=['GET'])
def zavady():
    context = {
        "zavady": Fault.query.order_by(Fault.id.desc()).all()
    }
    return render_template('zavady.html', **context)

@routes.route('/nalezy', methods=['GET'])
def nalezy():
    context = {
        "nalezy": Discovery.query.order_by(Discovery.id.desc()).all()
    }
    return render_template('nalezy.html', **context)

@routes.route('/zadat_nalez', methods=['GET'])
def zadat_nalez():
    return render_template('zadat_nalez.html')

@routes.route('/uklidy', methods=['GET'])
def uklidy():
    context = {
        "uklidy": Cleanup.query.order_by(Cleanup.to_be_completed.desc()).all()
    }
    return render_template('uklidy.html', **context)

