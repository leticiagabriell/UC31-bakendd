from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'TESTE'


@app.route("/contato")
def contato():
    return 'Pagina de contato'


@app.route("/usuario")
def usuario():
    usuario = {'nome': 'leticia', 'email': 'leticiagaby19@gmail.com'}
    return render_template('index.html',title='Pagina inicial',usuario=usuario,nome=None)


@app.route('/dados', defaults={"nome": "usuario comum"})
@app.route('/dados/<nome>')
def dados(nome):
    return f'Ola, {nome}!'


@app.route("/semestre/<int:x>")
def semestre(x):
    return 'Estamos no semestre ' + str(x)


@app.route("/pagamento/<float:valor>")
def pagamento(valor):
    return f'Valor do pagamento: R$' + {valor}


@app.route("/soma", defaults={"n1": 0, "n2": 0})
@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    resultado = n1 + n2
    return render_template('soma.html', n1=n1,n2=n2, resultado=resultado)

@app.route("/arearestrita/<int:id>")
def arearestrita(id):
   if id == 1:
       return " Acesso bloqueado (cadeado fechado)"
   else:
       return " Acesso liberado (cadeado aberto)"
   
@app.route("/operacao/<tipo>/<op1>/<op2>")
def operacao(tipo,op1,op2):
   if tipo == "sum":
      resultado = op1 + op2
   elif tipo =="sub":
      resultado = op1 - op2
   elif tipo == "mult":
      resultado = op1 * op2
   elif tipo == "div":
      resultado = op1 / op2
   else:
       
@app.route("/login")
def login():
   return render_template('login.html')


@app.route("/alunos")
def alunos():
   lista_aluno = [
       {'nome':'alice','matricula':'1234567890'},
       {'nome':'Bruno','matricula':'3456776890'},
       {'nome':'clara','matricula':'8765456788'},
       {'nome':'marcos','matricula':'8765456789'},
       {'nome':'valentina','matricula':'67845486790'}
   ]
   return render_template('alunos.html', aluno = alunos=lista_aluno)



#questao1


if __name__ == "__main__":
    app.run(debug=True)
