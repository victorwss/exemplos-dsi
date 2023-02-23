from flask import Flask

app = Flask(__name__)

# https://localhost:5000/<n1>/<op>/<n2>
# Nesse formato, n1 e n2 são valores numéricos e op é mais, menos, mult, div e mod

@app.route("/xxxx/<n1>/<op>/<n2>")
def calcular(n1, op, n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
    except:
        return "Erro", 404
    try:
        if op == "mais":  return str(n1 + n2)
        if op == "menos": return str(n1 - n2)
        if op == "mult":  return str(n1 * n2)
        if op == "div":   return str(n1 / n2)
        if op == "mod":   return str(n1 % n2)
        return "Erro", 404
    except:
        return "Erro", 422

# Vinicius Camargo Mota Morici
@app.route("/<n1>/<op>/<n2>", methods=["GET"])
def calcular2(n1, op, n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
    except:
        return "Erro", 404
    try:
        if op == 'mais':
            resultado = n1 + n2
            return str(resultado)
        if op == 'menos':
            resultado = n1 - n2
            return str(resultado)
        if op == 'mult':
            resultado = n1 * n2
            return str(resultado)
        if op == 'div':
            resultado = n1 / n2
            return str(resultado)
        if op == 'modulo':
            resultado = n1 % n2
            return str(resultado)
        return "Erro", 404
    except:
        return "Erro", 422

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)