from flask import render_template, Blueprint, redirect, url_for, request, flash

from web_app.models import *
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

routes = Blueprint('routes', __name__)

@routes.route('/',  methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #check if the login is already used
        user = None
        if request.form.get('login') and request.form.get('password'):
            if User.query.filter_by(login=request.form.get('login')).first():
                user = User.query.filter_by(login=request.form.get('login')).first()
                if check_password_hash(user.password, request.form.get('password')):
                    #login
                    login_user(user)
                    return redirect(url_for('routes.main'))
        flash('Špatně zadané údaje')
        return render_template('login.html')        
    else:
        return render_template('login.html')

@routes.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

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
    context = {
        "users" : User.query.all()
    }
    return render_template('uklizeci.html', **context)

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

@routes.route('/zadat_nalez', methods=['POST', 'GET'])
def zadat_nalez():
    if request.method == 'POST':
        if request.form.get('number') and request.form.get('description'):
            pass
        else:
            flash("Musíte zadat číslo pokoje a popis nálezu.")
            return redirect(url_for('routes.zadat_nalez'))
    else:
        return render_template('zadat_nalez.html')

@routes.route('/uklidy', methods=['GET'])
def uklidy():
    context = {
        "uklidy": Cleanup.query.order_by(Cleanup.to_be_completed.desc()).all()
    }
    return render_template('uklidy.html', **context)

