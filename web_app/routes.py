from flask import render_template, Blueprint, redirect, url_for, request, flash
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from web_app.models import *
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
import datetime
import json

routes = Blueprint('routes', __name__)

path('/search-rooms',csrf_exempt(routes.search_rooms), name="search_rooms")
  
def search_rooms(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        if search_str == "":
            return 2
        if Room.query.filter_by(number=search_str):
            return 1
        else:
            return 0
      
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
        if current_user.is_authenticated:
            return redirect(url_for('routes.main'))
        return render_template('login.html')

@routes.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.login'))

@routes.route('/main', methods=['GET'])
def main():
    return render_template('main.html')




@routes.route('/zadat_uklizeci', methods=['GET', 'POST'])
def zadat_uklizeci():
    if request.method == 'POST':
        if request.form.get('login') and request.form.get('password'):
            if User.query.filter_by(login = request.form.get('login')).first():
                flash("Uživatel s tímto loginem už existuje.")
            else:
                d = User(
                    login = request.form.get('login'),
                    unhashed_password = request.form.get('password'),
                    name = request.form.get('name') if request.form.get('name') else '',
                    surname = request.form.get('surname') if request.form.get('surname') else '',
                    isAdmin = True if request.form.get('admin') else False,
                )
                db.session.add(d)
                db.session.commit()
                flash("Úspěšně vytvořeno.")
                return redirect(url_for('routes.zadat_uklizeci'))
        else:
            flash("Musíte zadat login a heslo.")
        
        return redirect(url_for('routes.zadat_uklizeci'))
    else:
        return render_template('zadat_uklizeci.html')

@routes.route('/uklizeci', methods=['GET'])
def uklizeci():
    context = {
        "users" : User.query.all()
    }
    return render_template('uklizeci.html', **context)




@routes.route('/zadat_zavadu', methods=['GET', 'POST'])
def zadat_zavadu():
    rooms = Room.query.all()
    numbers = []  
    for r in rooms:
       numbers.append(r.number)
    context = {
        "rooms": numbers
    }
    if request.method == 'POST':
        if request.form.get('number') and request.form.get('description'):
            if not Room.query.filter_by(number = request.form.get('number')).first():
                flash("Pokoj s tímto číslem neexistuje")
            else:
                d = Fault(
                    room = Room.query.filter_by(number = request.form.get('number')).first(),
                    description = request.form.get('description'),
                    date = datetime.datetime.strptime(request.form.get('date'), "%Y-%m-%d") if request.form.get('date') else datetime.datetime.now() ,
                    completed = None,
                )
                db.session.add(d)
                db.session.commit()
                flash("Úspěšně vytvořeno.")
                return redirect(url_for('routes.zadat_zavadu'))
        else:
            flash("Musíte zadat číslo pokoje a popis závady.")
        
        return redirect(url_for('routes.zadat_zavadu'))
    else:
        return render_template('zadat_zavadu.html',**context)

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
    rooms = Room.query.all()
    numbers = []  
    for r in rooms:
       numbers.append(r.number)
    context = {
        "rooms": numbers
    }
    if request.method == 'POST':
        if request.form.get('number') and request.form.get('description'):
            if not Room.query.filter_by(number = request.form.get('number')).first():
                flash("Pokoj s tímto číslem neexistuje")
            else:
                d = Discovery(
                    room = Room.query.filter_by(number = request.form.get('number')).first(),
                    description = request.form.get('description'),
                    date = datetime.datetime.strptime(request.form.get('date'), "%Y-%m-%d") if request.form.get('date') else datetime.datetime.now() ,
                )
                db.session.add(d)
                db.session.commit()
                flash("Úspěšně vytvořeno.")
                return redirect(url_for('routes.zadat_nalez'))
        else:
            flash("Musíte zadat číslo pokoje a popis nálezu.")
        
        return redirect(url_for('routes.zadat_nalez'))
    else:
        return render_template('zadat_nalez.html',**context)



@routes.route('/zadat_uklid', methods=['GET', 'POST'])
def zadat_uklid():
    
    rooms = Room.query.all()
    numbers = []  
    for r in rooms:
       numbers.append(r.number)
    context = {
        "rooms": numbers
    }
    if request.method == 'POST':
        if request.form.get('number') and request.form.get('type') and request.form.get('date'):
            if not Room.query.filter_by(number = request.form.get('number')).first():
                flash("Pokoj s tímto číslem neexistuje")
            else:
                d = Cleanup(
                    room = Room.query.filter_by(number = request.form.get('number')).first(),
                    c_type = CleanupType(int(request.form.get('type'))),
                    to_be_completed = datetime.datetime.strptime(request.form.get('date'), "%Y-%m-%dT%H:%M") if request.form.get('date') else datetime.datetime.now() ,
                )
                db.session.add(d)
                db.session.commit()
                flash("Úspěšně vytvořeno.")
                return redirect(url_for('routes.zadat_uklid'))
        else:
            flash("Musíte zadat číslo pokoje, datum a typ úklidu.")
        
        return redirect(url_for('routes.zadat_uklid'))
    else:
        return render_template('zadat_uklid.html', **context)
    

@routes.route('/uklidy', methods=['GET'])
def uklidy():
    context = {
        "uklidy": Cleanup.query.order_by(Cleanup.to_be_completed.asc()).all(),
        "enum" : CleanupType.__members__
    }
    return render_template('uklidy.html', **context)

