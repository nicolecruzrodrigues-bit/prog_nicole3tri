"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    """Quantos numeros da lista sao menores que zero."""
   numeros = [10, -3, 5, -1, 0, -8, 7]

quantidade_negativos = 0

for numero in numeros:
    if numero < 0:
        
        quantidade_negativos = quantidade_negativos + 1

print("numeros menores que zero é:", quantidade_negativos)



def media(lista):
    """Media dos numeros. Lista vazia devolve 0."""
    def media_dos_numeros(lista):
    
    if len(lista) == 0:
        return 0

    soma = 0

    for numero in lista:
        soma = soma + numero

    quantidade = len(lista)

    media = soma / quantidade

    return media


numeros = [10, 20, 30]
resultado = media_dos_numeros(numeros)
print("A média é:", resultado)  

vazia = []
resultado_vazio = media_dos_numeros(vazia)
print("A média da lista vazia é:", resultado_vazio)  


def sem_o_maior(lista):
    """Lista NOVA sem o maior valor. Se o maior repete, tira so o primeiro."""
   def remover_primeiro_maior(lista):
   
    if len(lista) == 0:
        return []

    nova_lista = []
    for item in lista:
        nova_lista.append(item)

    maior = nova_lista[0]
    for numero in nova_lista:
        if numero > maior:
            maior = numero

    nova_lista.remove(maior)

    return nova_lista


numeros = [10, 30, 20, 30, 5]
resultado = remover_primeiro_maior(numeros)

print("Lista original:", numeros)
print("Nova lista:", resultado)


outra_lista = [5, 1, 9, 2]
print("Resultado 2:", remover_primeiro_maior(outra_lista))


def acumulada(lista):
    """Lista NOVA onde cada posicao e a soma de tudo ate ali.
    acumulada([1, 2, 3]) -> [1, 3, 6]"""
    def acumulada(lista):
    nova_lista = []
    soma_atual = 0

    for numero in lista:
        
        soma_atual = soma_atual + numero

        
        nova_lista.append(soma_atual)

    return nova_lista


numeros = [1, 2, 3]
resultado = acumulada(numeros)
print("Resultado:", resultado)  

outros_numeros = [2, 5, 10, 1]
print("Resultado 2:", acumulada(outros_numeros))  


def achata(lista_de_listas):
    """(Desafio) Junta as sublistas numa lista so.
    achata([[1, 2], [3]]) -> [1, 2, 3]"""
    def achata(lista_de_listas):
    nova_lista = []

    for sublista in lista_de_listas:
       
        for elemento in sublista:
            
            nova_lista.append(elemento)

    return nova_lista


dados = [[1, 2], [3]]
resultado = achata(dados)
print("Resultado:", resultado)  

outros_dados = [[10, 20], [30, 40, 50], [60]]
print("Resultado 2:", achata(outros_dados))  


# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    """ULTIMA posicao do alvo, ou -1."""
   def ultima_posicao(lista, alvo):
    posicao_encontrada = -1
    
    
    for i in range(len(lista)):
        
        if lista[i] == alvo:
            
            posicao_encontrada = i
            
    return posicao_encontrada


numeros = [10, 20, 30, 20, 50]


resultado1 = ultima_posicao(numeros, 20)
print("Última posição do 20:", resultado1)  

resultado2 = ultima_posicao(numeros, 99)
print("Última posição do 99:", resultado2)  


def conta_ocorrencias(lista, alvo):
    """Quantas vezes o alvo aparece."""
    pass


def primeiro_maior_que(lista, limite):
    """Posicao do primeiro elemento maior que limite, ou -1."""
    pass


def busca_binaria_primeira(lista, alvo):
    """(Desafio) Lista JA ORDENADA, o alvo pode repetir.
    Devolve a PRIMEIRA posicao do alvo, ou -1. Sem percorrer tudo."""
    pass


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    """(soma_dos_pares, operacoes). Conte 1 por elemento examinado."""
    pass


def maior_contando(lista):
    """(maior, comparacoes). Lista nao vazia.
    Conte 1 comparacao por elemento a partir do segundo."""
    pass


def tem_soma_contando(lista, alvo):
    """(True/False, comparacoes). Existem dois elementos que somam alvo?
    Conte 1 por par comparado. Pare assim que achar."""
    pass


def ordenada_contando(lista):
    """(Desafio) (True/False, comparacoes). A lista esta em ordem crescente?
    Conte 1 por par de vizinhos comparado. Pare no primeiro fora de ordem."""
    pass


# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    """Inverte a PROPRIA lista recebida. NAO cria lista nova e NAO devolve nada."""
    pass


def eh_palindromo(lista):
    """True se a lista e igual lida de tras para frente."""
    pass


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Devolve (i, j) das posicoes cujos valores somam alvo,
    ou (-1, -1). Sem laco dentro de laco."""
    pass


def soma_maxima_janela(lista, k):
    """Maior soma de k elementos seguidos.
    soma_maxima_janela([1, 2, 3, 4], 2) -> 7"""
    pass


def parenteses_balanceados(texto):
    """(Desafio) True se os ( ) e [ ] do texto abrem e fecham na ordem certa."""
    pass
