from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
   return render_template('index.html')
    

@app.route('/pizzaria/<sabor>')
def pizzaria(sabor):

    if sabor == 'calabresa':
        return render_template('calabresa.html',nome='Pizza de Calabresa',imagem='calabresa.jpg')

    elif sabor == 'margherita':
        return render_template('margherita.html',nome='Pizza Margherita', imagem='margherita.jpg')

    elif sabor == 'frango':
        return render_template('frango.html',nome='Pizza de Frango',imagem='frango.jpg')

    else:
        return 'Sabor não disponível'

if __name__ == '__main__':
    app.run(debug=True)
