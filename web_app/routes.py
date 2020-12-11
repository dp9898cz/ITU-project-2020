from Flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def login():
    return render_template('login.html')

@main.route('/main', methods=['GET'])
def main():
    return render_template('main.html')

@main.route('/zadat_pobyt', methods=['GET'])
def zadat_pobyt():
    return render_template('zadat_pobyt.html')

@main.route('/zadat_uklid', methods=['GET'])
def zadat_uklid():
    return render_template('zadat_uklid.html')

@main.route('/zadat_zavadu', methods=['GET'])
def zadat_zavadu():
    return render_template('zadat_zavadu.html')

@main.route('/pobyty', methods=['GET'])
def pobyty():
    return render_template('pobyty.html')

@main.route('/uklidy', methods=['GET'])
def uklidy():
    return render_template('uklidy.html')

@main.route('/uklizeci', methods=['GET'])
def uklizeci():
    return render_template('uklizeci.html')