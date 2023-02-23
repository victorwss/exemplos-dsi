def contador(frase):
    palavras = frase.split(" ")
    resposta = {}
    for p in palavras:
        if p in resposta:
            resposta[p] += 1
        else:
            resposta[p] = 1
    return resposta

def contador2(string):
    palavras = string.split()
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

print(contador2('esse exercício é um exercício fácil ou difícil'))
print(contador2('o doce perguntou ao doce qual é o doce mais doce e o doce respondeu ao doce que o doce mais doce é o doce de batata doce'))