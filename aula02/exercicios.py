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
    
    def alternar_listas(lista1, lista2):
    nova_lista = []
    i = 0
    while i < len(lista1):
        nova_lista.append(lista1[i])
        nova_lista.append(lista2[i])
        i = i + 1
    return nova_lista

l1 = [1, 3, 5]
l2 = [2, 4, 6]
print(alternar_listas(l1, l2))

def remove_repetidos(lista):
    def remover_repetidos(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

numeros = [1, 2, 2, 3, 4, 1, 5, 3]
print(remover_repetidos(numeros))