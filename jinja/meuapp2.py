from flask import flash, Flask, make_response, render_template, redirect, request, session
from dataclasses import dataclass

app = Flask(__name__)

app.secret_key = "Grande segredo secreto que não pode ser revelado a ninguém"

@app.route("/")
@app.route("/bom-dia")
def bom_dia():
    return render_template("oi.html", mensagem = "Bom dia")

@app.route("/boa-tarde")
def boa_tarde():
    return render_template("oi.html", mensagem = "Boa tarde")

@dataclass
class Fruta:
    nome: str
    cor: str

frutas = [
    Fruta("uva", "rosa"),
    Fruta("maçã", "vermelha"),
    Fruta("morango", "vermelha"),
]

@app.route("/nova-fruta")
def nova_fruta():
    usuario_logado = quem_esta_logado()
    if usuario_logado is None:
        return render_template("login.html", erro = "Você deve se logar!"), 302
    return render_template("cadastrar_frutas.html")

@app.route("/frutas")
def listar_frutas():
    usuario_logado = quem_esta_logado()
    if usuario_logado is None:
        return render_template("login.html", erro = "Você deve se logar!"), 302
    return render_template("listar_frutas.html", listagem = frutas)

@app.route("/frutas", methods = ["POST"])
def criar_fruta():
    usuario_logado = quem_esta_logado()
    if usuario_logado is None:
        return render_template("login.html", erro = "Você deve se logar!"), 302
    formulario = request.form
    nova_fruta = Fruta(formulario['nome'], formulario['cor'])
    frutas.append(nova_fruta)
    return redirect("/frutas")

@dataclass
class Usuario:
    login: str
    senha: str

usuarios = [
    Usuario("joao", "1234"),
    Usuario("maria", "4321"),
]

def quem_esta_logado():
    return session.get("usuario_logado", None)

def verificar_login(login, senha):
    for u in usuarios:
        if u.login == login and u.senha == senha:
            return u
    return None

@app.route("/login")
def tela_login():
    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def login():
    login = request.form.get("login", "")
    senha = request.form.get("senha", "")
    usuario_logado = verificar_login(login, senha)
    if usuario_logado is None:
        return render_template("login.html", erro = "Senha errada"), 302
    session["usuario_logado"] = usuario_logado
    return redirect("/frutas")

@app.route("/logout", methods = ["POST"])
def logout():
    session.pop("usuario_logado", None)
    return render_template("login.html", erro = "Tchau")

@app.route("/visitar/<planeta>")
def visitar_planeta(planeta):
    flash(planeta)
    return "OK"

@app.route("/planetas")
def listar_planetas_visitados_recentemente():
    return render_template("planetas.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)