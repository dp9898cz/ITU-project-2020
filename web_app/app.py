from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html')

@app.route('/zadat_pobyt', methods=['GET'])
def zadat_pobyt():
    return render_template('zadat_pobyt.html')

@app.route('/zadat_uklid', methods=['GET'])
def zadat_uklid():
    return render_template('zadat_uklid.html')

@app.route('/zadat_zavadu', methods=['GET'])
def zadat_zavadu():
    return render_template('zadat_zavadu.html')

@app.route('/zavady', methods=['GET'])
def zavady():
    return render_template('zavady.html')

@app.route('/pobyty', methods=['GET'])
def pobyty():
    return render_template('pobyty.html')

@app.route('/nalezy', methods=['GET'])
def nalezy():
    return render_template('nalezy.html')

@app.route('/zadat_nalez', methods=['GET'])
def zadat_nalez():
    return render_template('zadat_nalez.html')

@app.route('/uklidy', methods=['GET'])
def uklidy():
    return render_template('uklidy.html')

@app.route('/uklizeci', methods=['GET'])
def uklizeci():
    return render_template('uklizeci.html')