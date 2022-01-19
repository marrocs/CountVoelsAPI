'''Usando Python + Flask, escreva o código de uma API com a seguinte rota:

[POST] /vowel_count

Recebe um JSON contendo strings e devolve um JSON contendo cada string como chave e o número de vogais como valor.

Ex: [POST] /vowel_count

Requisição: ["batman", "robin", "coringa"]

Resposta: {"batman": 2, "robin": 2, "coringa": 3}

Fique à vontade pra consultar a documentação de Python e Flask. Não é necessário fazer o deploy, mas seria legal 
se a API rodasse localmente (insira instruções pra isso em um README). Documentação, qualidade de código, testes, 
tudo conta na avaliação, portanto capriche.'''


palavras = ['pato', 'rato', 'banana', 'xis', 'abacate', 'itaquaquecetuba', 'zz', 0]


def order_array(palavras):
    voels, vs, count = ['a', 'e', 'i', 'o', 'u'], [], 0

    # iterate palavras
    for w in palavras:
        if type(w) is not str:
            raise TypeError('A função só aceita parametros do tipo string. Altere os elementos em "api.txt".')
        else:
            for l in w:
                if l in voels:
                    count += 1  # count voels
            vs.append(count)
            count = 0

    palavras = list(zip(palavras, vs))  # zip lists

    palavras = {x: y for x, y in sorted(palavras, key=lambda x: x[1])}  # order

    return palavras


print(order_array(palavras))
