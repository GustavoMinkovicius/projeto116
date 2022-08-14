# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Gustavo" # escreva seu nome
    idade = "15" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def home():

    nome = "claudio" # escreva seu nome
    idade = "54" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
@app.route("/mãe")
def home():

    nome = "Valeria" # escreva seu nome
    idade = "56" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do amigo
@app.route("/amigo")
def home():

    nome = "Michel" # escreva seu nome
    idade = "15" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
