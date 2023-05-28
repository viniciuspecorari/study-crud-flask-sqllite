from flask import Flask, render_template, request
import requests

# Iniciando o flask
app = Flask(__name__, template_folder='templates')

# Criar 1º pagina do site. Precisa criar as rotas
# Rota = URL do site ou do caminho
# Função = O que você quer exibir na página
# Template 

# Página inicial
@app.route("/")
def homepage():
    return render_template("homepage.html")

# Página de contatos
@app.route("/contatos")
def contatos():
        return render_template("contatos.html")


# # Página de usuários com parâmetro
# @app.route("/usuarios/<nome_usuario>")
# def usuarios(nome_usuario):
#         return render_template("usuarios.html", nome_usuario=nome_usuario)

# Página de usuários sem parâmetro
@app.route("/usuarios")
def usuarios():
        return render_template("usuarios.html")

# Página form - BuscaCEP
@app.route("/buscacep", methods=['GET', 'POST'])
def buscacep():
    if request.method == 'POST':
        # Recuperando a variavel CEP
        varCEP = request.form['cep']

        print('CEP:', varCEP)

        try:
            # Realizando requisição para o ViaCEP
            responseCEP = requests.get(
                'https://viacep.com.br/ws/'+str(varCEP)+'/json/')

            # Verificando o status code da requisição
            if responseCEP.status_code == 200:
                JSONCep = responseCEP.json()
                varCEP = JSONCep["cep"]
                logradouro = JSONCep["logradouro"]
                complemento = JSONCep["complemento"]
                bairro = JSONCep["bairro"]
                cidade = JSONCep["localidade"]
                estado = JSONCep["uf"]
                ibge = JSONCep["ibge"]        
                return render_template("buscacep.html", varCEP=varCEP, logradouro=logradouro, bairro=bairro, cidade=cidade, estado=estado)  
        except:
            return render_template("buscacep.html")
        
    
    return render_template("buscacep.html")


# Colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)