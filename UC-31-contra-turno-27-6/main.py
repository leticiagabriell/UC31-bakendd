from flask import flask,render_template,request

app = Flask(_name_)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form.get('nome')
    email = request.form.get('email')

    return "{} e {}".format(nome,email)

if __name__=='_main_':
    app.run(debug=True)
