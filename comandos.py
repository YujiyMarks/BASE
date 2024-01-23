''' # Bibliotecas
import os # importação de biblioteca [ import 'biblioteca' ]
import pandas as pd # importar uma biblioteca com apelido [ import 'biblioteca' as 'apelido' ]
import plotly.express as px
import numpy as np
from numpy.random import default_rng # importar uma função de uma biblioteca [ from 'biblioteca' import 'função' ]
import this 
'''


''' # Variaveis
a = 5 # declaração de váriavel ['nome' = 'valor']
L = ['a',a,2,'2',"3"] # criação de uma váriavel como lista 
ti = 'Ola' # criação de váriavel como string 

# todo texto ou string deve ser acompanhado de aspas
'''


''' # OUTPUT
print('Hello World') # output de texto [ print('texto') ]
print(a) #output de váriaveis [ print('váriavel') ]
print("Hello", a, "World")
print(L) 

print("Olá 'Mundo' bonito") # output de texto com aspas 
print("Olá\nMundo") # output de texto com quebra de linhas [ \n ]
print("Olá\n Mundo") 
print("Olá\tMundo") # output de texto com tabulação [ \t ]
print("Olá\n\tMundo") 

print(f'Hello {a}World') # output com formatação, colocando váriaveis no meio do texto [ print(f'texto{'váriaveis'}') ]
'''


''' # INPUT
ent = input('Entrada:') # input de dados [ input('texto') ]
print(ent)
'''


''' # Operações
x = 2
y = 5

a = x+y # soma [ 'valor1' + 'valor2' ]
b = x*y # multiplicação [ 'valor1' * 'valor2' ]
c = y/x # divisão decimal [ 'valor1' / 'valor2' ]
d = y//x # divisão inteira [ 'valor1' // 'valor2' ]
e = y%x # resto [ 'valor1' % 'valor2' ]
f = y**x # potência [ 'valor1' ** 'valor2' ]
g = 2 + (3*5)

print(a,b,c,d,e,f,g)
'''

''' # Estruturas de CONDIÇÂO
S = [3,3,2]

if x > y: # comando de condição se [ if 'condição': ]
    print(x)
else: # comando de condição senão [ else: ]
    print(y)
    
if y > x:
    print(y)
elif x == y+1: # múltiplas condições [ elif 'condição': ]
    print(x)
else:
    print('oi')
    
if all(i == 3 for i in S): # análisa se todos elementos satisfazem a uma condição [ all('condição') ]
    print(S)

if any(i == 3 for i in S): # análisa se pelo menos um elemento satisfaz a uma condição [ any('condição') ]
    print(S)
'''

''' # Comandos de COMPARAÇÂO
if not y < x: # not faz a negação de uma sentença
    print(x)

if y >= x or y != x: # 'ou' e 'diferente'
    print(y)

if y == x and x > 0: # 'igual' e 'e'
    print(x)

'''


''' # Estruturas de REPETIÇÂO
a = 5
L = ['a',a,2,'2',"3"]

for x in L: # repetição definida [ for 'váriavel' in 'lista': ]
    print(x)
    print(f'Alo {x}galera',a," oi") 

print(x)

i = 1
while i < 3: # repetição indefinida [ while 'condição': ]
    print(i)
    i=i+1
'''


''' # Função
x = 3

def Soma(a,b): # definição de função [ def 'nome'('váriaveis'): ]
    return a+b # valor a ser retornado [ return 'valor' ]

def Nada(x):
    x = 2
    y = x
    print(x+y)
    
    return None # função sem retorno [ return None ]

def maior(a):
    if a > 1:
        return True # retorno booleano 
    else:
        return False
    

U = [-1,0,2,5]

F = Soma(2,x)
print(F)

N = Nada(x)
print(N)

M = filter(maior,U) # ?
print(M)
'''


''' # STRINGS
A = "oi"
B = " oioi oi"
Te = 'AbRaC aDaBrA'

t = Te.lower() # deixa todo o texto em minusculo [ 'string'.lower() ]
T = Te.upper() # deixa todo o texto em maiusculo [ 'string'.upper() ]
Tit = Te.title() # deixa a letra inicial das palavras em maiusculo [ 'string'.title() ]

print(Te,t,T,Tit)

print(A[1]) # escolhe o elemento de uma posição da string [ 'string'['posição'] ]

if B > A or A == B: # comparação de strings
    print(A+B) # concatenação de string ['string'+'string']
    
print(B.find('i')) # mostra a posição que uma primeira letra está em uma string [ 'string'.find('letra') 
print(B.replace('i','e')) # troca uma string pela outra [ 'string'.replace('string inicial','string trocada') ]
print(B.count('oi')) # conta quantas vezes tem uma string []
print(B.rstrip()) # remove os caracteres brancos do inicio e fim [ 'string'.strip() ]
print(B.lstrip()) # remove os caracteres brancos do inicio [ 'string'.lstrip() ]
print(B.strip()) # remove os caracteres brancos do fim [ 'string'.rstrip() ]
print(B.split()) # divide a string em palavras [ 'string'.split() ]
print(B.split('i')) # divide a string de acordo com o separado [ 'string'.split('separador') ]
print(B.index('i')) # mostrado o indice da letra [ 'string'.index('letra') ]

print(A*2) # escreve a string multiplas vezes [ print('string'*'vezes') ]
print(B[2:5]) # escreve um subconjunto de uma string [ print('string[posicao inicial: posicao final+1]') ]
'''

''' # Listas
V = ['a',a,'2',5,2,"3"]
H = [2,1,5,7]
G = [] # cria uma lista sem elementos

print(G)

# contagem de lista
print(len(V)) # quantidade de elementos de uma lista [ len('lista') ]
print(len(A)) # quantidade de letras de uma string [ len('string') ]
print(len('oioi'))

# adição de elementos
V.append('hau') # adiciona um elemento ao final da lista [ 'lista'.append('elemento') ]
print(V)
V.insert(2,'hey') # adiciona um elemento numa posicao da lista [ 'lista'.insert('posicao','elemento') ]
print(V)
V[2] = 'cabal' # adiciona o valor a posicao dada [ 'lista'['posicao'] = 'valor' ]
print(V)

# remoção de elementos
V.remove(2) # remove um elemento numa posicao da lista [ 'lista'.remove('posicao') ]
print(V)
V.remove('hau')
print(V)
del V[2] # outra forma de remover um elemento de uma posicao da lista[ del 'lista'['posicao'] ]
print(V)
print(V.pop()) # retorna e remove o ultimo elemento da lista [ 'string'.pop() ]
print(V.pop(2)) # retorna e remove o elemento de uma posicao da lista [ 'string'.pop('posicao') ]

# outros comandos
print(max(H)) # retornar o maior valor de uma lista [max('lista')]
print(min(H)) # retornar o menor valor de uma lista [min('lista')]
print(sorted(H)) # pega uma lista e deixa os elementos em posições aleatórias [ sorted('lista') ]

for i, p in enumerate(V): # enumeração de uma lista [ enumerate('lista') ]
    print(i, p)
'''


''' # Vetores
V = ['a',a,'2',5,2,"3"] # é uma lista com ordenação
print(V)
print(V[0]) # mostrar um elemento especifico de um vetor [ 'vetor'['posicao'] ]
print(V[-1]) # utilizar números negativos faz a contagem a partir do final

M = [[a,b,c],[1,2,3]] # criação de matriz [ listas dentro de uma lista ]
print(M)
print(M[0][1])
'''


''' # Tuplas
mar, felps = "ei",2
print(mar)

# tuplas, vetores e listas agem semelhantemente
'''


''' # Arquivos
arq = open('testo.txt', 'r') # abertura de um arquivo apenas para leitura [ open('arquivo','r') ]

linha = arq.readline() # leitura de uma linha do arquivo [ 'arquivo'.readline() ]
print(linha)

linhas = arq.readlines() # leitura das linhas de um arquivo pequeno [ 'arquivo'.readlines() ]
print(linhas)

arq.close() # comando para fechar um arquivo [ 'arquivo'.close() ]


arq = open('testo.txt', 'w') # abertura de um arquivo para escrita por cima do texto [ open('arquivo','w') ]

arq.write('texto') # comando para escrever em um arquivo [ 'arquivo'.write('texto') ]

arq.close()
'''


''' # Outras Funções
A = 2.5
V = [a,2,2.5]
S = [3,3,2]

print(int(A)) # converte um número para inteiro [ int('número') ]
print(str(A)) # converte um objeto para string [ str('objeto') ]

#help(A) # mostra algumas informações sobre um objeto ou comando [ help('objeto') ]

L = range(3,9,2) # crição de P.A. [ range(valor inicial, valor final, razão) ]

for t in zip(L, V): # retorna uma lista conjunta para cada uma das posições dadas [ zip('listas') ]
    print(t)
'''
