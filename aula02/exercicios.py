"""Aula 02 - Listas em Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def remove_negativos(lista):
   def remove_negativos(lista):
    resultado = []
    for i in lista:
        if i >= 0:
            resultado.append(i)
    return resultado


minha_lista = [10, -5, 3, -1, 0, 7, -8]
print(remove_negativos(minha_lista))


def inverte(lista):
    def inverter_lista(lista):
    nova = []
    tamanho = len(lista)
    while tamanho > 0:
        tamanho = tamanho - 1
        nova.append(lista[tamanho])
    return nova

numeros = [1, 2, 3, 4, 5]
resultado = inverter_lista(numeros)
print(resultado)


def busca_binaria(lista, alvo):
    def buscar_posicao(lista, alvo):
    posicao = 0
    for item in lista:
        if item == alvo:
            return posicao
        posicao = posicao + 1
    return -1

numeros = [10, 20, 30, 40, 50]
print(buscar_posicao(numeros, 30))
print(buscar_posicao(numeros, 99))


def intercala(lista_a, lista_b):
    """Devolve uma lista nova alternando os elementos das duas.
    As duas listas tem o mesmo tamanho."""
    pass


def remove_repetidos(lista):
    """(Desafio) Devolve uma lista nova sem repetidos,
    mantendo a ordem da primeira aparicao."""
    pass
