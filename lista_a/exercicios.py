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
    def contar_ocorrencias(lista, alvo):
    contador = 0

   
    for item in lista:
        
            contador = contador + 1  

    return contador



numeros = [10, 20, 30, 20, 50, 20]

resultado1 = contar_ocorrencias(numeros, 20)
print("O número 20 aparece:", resultado1, "vezes")  

resultado2 = contar_ocorrencias(numeros, 99)
print("O número 99 aparece:", resultado2, "vezes") 


def primeiro_maior_que(lista, limite):
    """Posicao do primeiro elemento maior que limite, ou -1."""
    def primeiro_maior(lista, limite):
   
    for i in range(len(lista)):
       
        if lista[i] > limite:
            return i  
            

    return -1


numeros = [10, 20, 50, 30, 80]

resultado1 = primeiro_maior(numeros, 25)
print("Posição:", resultado1)  

resultado2 = primeiro_maior(numeros, 100)
print("Posição:", resultado2)  

def busca_binaria_primeira(lista, alvo):
    """(Desafio) Lista JA ORDENADA, o alvo pode repetir.
    Devolve a PRIMEIRA posicao do alvo, ou -1. Sem percorrer tudo."""
   def primeira_posicao(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    posicao_encontrada = -1

    while inicio <= fim:
    
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            
            posicao_encontrada = meio
            
            fim = meio - 1

        elif lista[meio] < alvo:
            
            inicio = meio + 1
            
        else:
            
            fim = meio - 1

    return posicao_encontrada


numeros = [10, 20, 20, 20, 30, 40, 50]

resultado1 = primeira_posicao(numeros, 20)
print("Primeira posição do 20:", resultado1)  
resultado2 
print("Primeira posição do 99:", resultado2) 

# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    """(soma_dos_pares, operacoes). Conte 1 por elemento examinado."""
   def somar_pares_e_contar_operacoes(lista):
    soma_dos_pares = 0
    operacoes = 0

    for numero in lista:
        
        operacoes = operacoes + 1

        
        if numero % 2 == 0:
            soma_dos_pares = soma_dos_pares + numero

    return (soma_dos_pares, operacoes)

numeros = [1, 2, 3, 4, 5, 6]
resultado = somar_pares_e_contar_operacoes(numeros)

print("Resultado (soma dos pares, operacoes):", resultado)

def maior_contando(lista):
    
"""(maior, comparacoes). Lista nao vazia.
    Conte 1 comparacao por elemento a partir do segundo."""
    def maior_e_comparacoes(lista):
    
    maior = lista[0]
    comparacoes = 0

    for i in range(1, len(lista)):
        
        comparacoes = comparacoes + 1

        
        if lista[i] > maior:
            maior = lista[i]

    return (maior, comparacoes)

numeros = [10, 50, 20, 80, 30]
resultado = maior_e_comparacoes(numeros)

print("Resultado (maior, comparacoes):", resultado)


def tem_soma_contando(lista, alvo):
    """(True/False, comparacoes). Existem dois elementos que somam alvo?
    Conte 1 por par comparado. Pare assim que achar."""
   def tem_soma_alvo(lista, alvo):
    comparacoes = 0
    
    
    for i in range(len(lista)):
    
        for j in range(i + 1, len(lista)):
            
        
            comparacoes = comparacoes + 1
            
           
            if lista[i] + lista[j] == alvo:
                
                return (True, comparacoes)

    return (False, comparacoes)

numeros = [2, 7, 11, 15]

resultado1 = tem_soma_alvo(numeros, 9)
print("Resultado 1:", resultado1)

resultado2 = tem_soma_alvo(numeros, 26)
print("Resultado 2:", resultado2)

resultado3 = tem_soma_alvo(numeros, 100)
print("Resultado 3:", resultado3)



def ordenada_contando(lista):
    """(Desafio) (True/False, comparacoes). A lista esta em ordem crescente?
    Conte 1 por par de vizinhos comparado. Pare no primeiro fora de ordem."""
    def esta_ordenada(lista):
    comparacoes = 0

    for i in range(len(lista) - 1):
        
        comparacoes = comparacoes + 1

        
        if lista[i] > lista[i + 1]:
            
            return (False, comparacoes)

   
    return (True, comparacoes)

lista1 = [10, 20, 30, 40]
print("Exemplo 1:", esta_ordenada(lista1))

lista2 = [50, 10, 20, 30]
print("Exemplo 2:", esta_ordenada(lista2))

lista3 = [10, 20, 40, 30]
print("Exemplo 3:", esta_ordenada(lista3))



# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    """Inverte a PROPRIA lista recebida. NAO cria lista nova e NAO devolve nada."""
    def inverter_lista(lista):
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        
        temp = lista[inicio]
        lista[inicio] = lista[fim]
        lista[fim] = temp

       
        inicio = inicio + 1
        fim = fim - 1


numeros = [1, 2, 3, 4, 5]


inverter_lista(numeros)


print(numeros)  

def eh_palindromo(lista):
    """True se a lista e igual lida de tras para frente."""
    def eh_palindromo(lista):
    inicio = 0
    fim = len(lista) - 1

   
    while inicio < fim:
        
        if lista[inicio] != lista[fim]:
            return False
        
       
        inicio = inicio + 1
        fim = fim - 1

    return True

lista1 = [1, 2, 3, 2, 1]
print(eh_palindromo(lista1)) 

lista2 = [1, 2, 3, 4, 5]
print(eh_palindromo(lista2))  


lista3 = ["a", "r", "a", "r", "a"]
print(eh_palindromo(lista3))  

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
