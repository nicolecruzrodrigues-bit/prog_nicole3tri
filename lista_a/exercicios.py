"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

# ---------- Bloco 1: Operações Básicas ----------

def conta_negativos(lista):
    """Quantos numeros da lista sao menores que zero."""
    quantidade_negativos = 0
    for n in lista:
        if n < 0:
            quantidade_negativos += 1
    return quantidade_negativos


def media(lista):
    """Media dos numeros. Lista vazia devolve 0."""
    if len(lista) == 0:
        return 0
    soma = 0
    for numero in lista:
        soma += numero
    return soma / len(lista)


def sem_o_maior(lista):
    """Lista NOVA sem o maior valor. Se o maior repete, tira so o primeiro."""
    if len(lista) == 0:
        return []

    nova_lista = list(lista)
    maior = nova_lista[0]
    for numero in nova_lista:
        if numero > maior:
            maior = numero

    nova_lista.remove(maior)
    return nova_lista


def acumulada(lista):
    """Lista NOVA onde cada posicao e a soma de tudo ate ali.
    acumulada([1, 2, 3]) -> [1, 3, 6]"""
    nova_lista = []
    soma_atual = 0
    for numero in lista:
        soma_atual += numero
        nova_lista.append(soma_atual)
    return nova_lista


def achata(lista_de_listas):
    """(Desafio) Junta as sublistas numa lista so.
    achata([[1, 2], [3]]) -> [1, 2, 3]"""
    nova_lista = []
    for sublista in lista_de_listas:
        for elemento in sublista:
            nova_lista.append(elemento)
    return nova_lista


# ---------- Bloco 2: Busca ----------

def busca_ultima(lista, alvo):
    """ULTIMA posicao do alvo, ou -1."""
    posicao_encontrada = -1
    for i in range(len(lista)):
        if lista[i] == alvo:
            posicao_encontrada = i
    return posicao_encontrada


def conta_ocorrencias(lista, alvo):
    """Quantas vezes o alvo aparece."""
    contador = 0
    for item in lista:
        if item == alvo:  # Correção: verificação de igualdade necessária
            contador += 1
    return contador


def primeiro_maior_que(lista, limite):
    """Posicao do primeiro elemento maior que limite, ou -1."""
    for i in range(len(lista)):
        if lista[i] > limite:
            return i
    return -1


def busca_binaria_primeira(lista, alvo):
    """(Desafio) Lista JA ORDENADA, o alvo pode repetir.
    Devolve a PRIMEIRA posicao do alvo, ou -1. Sem percorrer tudo."""
    inicio = 0
    fim = len(lista) - 1
    posicao_encontrada = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            posicao_encontrada = meio
            fim = meio - 1  # Continua buscando à esquerda
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return posicao_encontrada


# ---------- Bloco 3: Custo ----------

def soma_pares_contando(lista):
    """(soma_dos_pares, operacoes). Conte 1 por elemento examinado."""
    soma_dos_pares = 0
    operacoes = 0
    for numero in lista:
        operacoes += 1
        if numero % 2 == 0:
            soma_dos_pares += numero
    return (soma_dos_pares, operacoes)


def maior_contando(lista):
    """(maior, comparacoes). Lista nao vazia.
    Conte 1 comparacao por elemento a partir do segundo."""
    maior = lista[0]
    comparacoes = 0
    for i in range(1, len(lista)):
        comparacoes += 1
        if lista[i] > maior:
            maior = lista[i]
    return (maior, comparacoes)


def tem_soma_contando(lista, alvo):
    """(True/False, comparacoes). Existem dois elementos que somam alvo?
    Conte 1 por par comparado. Pare assim que achar."""
    comparacoes = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            comparacoes += 1
            if lista[i] + lista[j] == alvo:
                return (True, comparacoes)
    return (False, comparacoes)


def ordenada_contando(lista):
    """(Desafio) (True/False, comparacoes). A lista esta em ordem crescente?
    Conte 1 por par de vizinhos comparado. Pare no primeiro fora de ordem."""
    comparacoes = 0
    for i in range(len(lista) - 1):
        comparacoes += 1
        if lista[i] > lista[i + 1]:
            return (False, comparacoes)
    return (True, comparacoes)


# ---------- Bloco 4: Padrões ----------

def inverte_no_lugar(lista):
    """Inverte a PROPRIA lista recebida. NAO cria lista nova e NAO devolve nada."""
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1


def eh_palindromo(lista):
    """True se a lista e igual lida de tras para frente."""
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        if lista[inicio] != lista[fim]:
            return False
        inicio += 1
        fim -= 1
    return True


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Devolve (i, j) das posicoes cujos valores somam alvo,
    ou (-1, -1). Sem laco dentro de laco."""
    i = 0
    j = len(lista) - 1
    while i < j:
        soma = lista[i] + lista[j]
        if soma == alvo:
            return (i, j)
        elif soma < alvo:
            i += 1
        else:
            j -= 1
    return (-1, -1)


def soma_maxima_janela(lista, k):
    """Maior soma de k elementos seguidos.
    soma_maxima_janela([1, 2, 3, 4], 2) -> 7"""
    if len(lista) < k or k <= 0:
        return 0

    soma_atual = sum(lista[:k])
    soma_maxima = soma_atual

    for i in range(k, len(lista)):
        soma_atual = soma_atual + lista[i] - lista[i - k]
        if soma_atual > soma_maxima:
            soma_maxima = soma_atual

    return soma_maxima


def parenteses_balanceados(texto):
    """(Desafio) True se os ( ) e [ ] do texto abrem e fecham na ordem certa."""
    pilha = []
    for caractere in texto:
        if caractere in "([":
            pilha.append(caractere)
        elif caractere == ")":
            if not pilha or pilha[-1] != "(":
                return False
            pilha.pop()
        elif caractere == "]":
            if not pilha or pilha[-1] != "[":
                return False
            pilha.pop()

    return len(pilha) == 0
