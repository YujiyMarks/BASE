''' # Bibliotecas
import os # importação de biblioteca [ import 'biblioteca' ]
import pandas as pd # importar uma biblioteca com apelido [ import 'biblioteca' as 'apelido' ]
import plotly.express as px
import numpy as np
from numpy.random import default_rng # importar uma função de uma biblioteca [ from 'biblioteca' import 'função' ]
import this
'''


''' # OS
lista = os.listdir("Vendas") # input de todos arquivos de um diretótio como uma lista [ os.listdir('diretório') ]
display(lista) # output de uma lista na vertical [ display('lista') ]
'''


''' # PANDAS
total = pd.DataFrame() # criação de tabela no pandas [ 'nome' = pd.DataFrame() ]

for item in lista:
    if 'Vendas' in item:
        tabela = pd.read_csv(f"Vendas/{item}") # leitura de um arquivo pelo pandas [ pd.read_'extensao'('arquivo') ]
        total = total.append(tabela)
        
display(total)

produtos = total.groupby('Produto').sum() # agrupa os valores de uma tabela por grupos e depois os soma [ 'tabela'.groupby('grupo').sum() ]
# no lugar da soma podem ser usadas outras operações como .median() / .mean() / .min() / .max()

produtos = produtos[['Quantidade Vendida']] # seleciona apenas algumas colunas da tabela [ 'tabela[['colunas']]' ]
produtos = produtos.sort_values(by='Quantidade Vendida',ascending=False) 
# organiza a tabela de forma crescente de acordo com os dados de uma coluna [ 'tabela'.sort_values(by='coluna',ascending=False) ]

total['Faturamento'] = total['Quantidade Vendida'] * total['Preco Unitario'] 
# adiciona uma coluna a tabela dada pela operação entre outras [ total['Nova coluna'] = 'tabela'['coluna1'] 'operacao' 'tabela'[coluna2] ]

print(produtos)

display(total['Primeiro Nome'].unique()) # análisa todos valores únicos de uma coluna [ 'tabela'['coluna'].unique() ]

print(total['Primeiro Nome'].nunique()) # conta quantos valores únicos há em uma coluna [ 'tabela'['coluna'].nunique() ]

total.describe() # mostra informações estatisticas a respeito das colunas de uma tabela ['tabela'.describe() ]

total[['Produto']].value_counts() # mostra quantas vezes aparece cada item único de uma coluna [ 'tabela'[['coluna']].value_counts ]

pd.isnull(total) # mostra se há algum valor ausente em uma tabela [ pd.isnull('tabela') ]

total['Unnamed: 8'].fillna(value=2, inplace=True) 
# preenche os valores ausentes de uma coluna [ 'tabela'['coluna'].fillna(value='valor', inplace=True) ] 
display(total)

dic = {'iPhone':1, 'Televisão':2, 'Notebook':3, 'Android':4, 'SmartWatch':5, 'Tablet':6, 'Câmera':7} 
# cria um dicionário que associa valores [ 'nome' = {x1:y1,x2:y2} ]

total['Produto'].map(dic) 
# troca os valores de uma coluna de acordo com um dicionário [ 'tabela'['coluna'].map('dicionario') ]

def divide(x):
    return x/2

table = pd.DataFrame({'Idade':[2,3,5],'Sexo':["M","F","F"]}) 
# criação de uma tabela manualmente [ pd.DataFrame({'coluna1':[valores]}) ]
display(table)

table['Idade'].apply(divide) # aplica uma função a coluna de uma tabela [ 'tabela'['coluna'].apply('funcao') ]
'''


''' # PX
graf = px.bar(produtos, y=produtos.index, x='Quantidade Vendida') 
# Criação de gráfico de barras através de duas grandezas de uma tabela [ px.bar('tabela', y='grandeza1', x='grandeza2') ]
graf.show() # comando para mostrar uma gráfico [ 'gráfico'.show() ]
'''


''' # NUMPY
A = np.array([1,2,3,4,5]) # criação de um array [ 'nome' = np.array(['valores']) ]
print(A)
M = np.array([[1,2,3],[1,2,3]])
print(M)

Z = np.zeros(shape = (2,4,3)) # cria uma matriz de zeros [ np.zeros(shape = ('quantidade','linhas','colunas')) ]
print(Z)

Um = np.ones(shape = (2,3,4)) # cria uma matriz de uns [ np.ones(shape = ('quantidade','linhas','colunas')) ]
print(Um)

print(np.arange(5)) # gera uma lista começando em 0 e terminando no valor dado [ np.arange('valor fina') ]
print(np.arange(3,9,2)) # lista com um valor inicial e final e razão a ser utilizada [ np.arange('valor inicial','valor final','razão') ]

print(np.linspace(0, 50, num=20, endpoint=False, retstep=True)) 
# cria uma lista de número com espaçamentos iguais [ np.linspace('valor inicial','valor final', num='quantidade de numeros',endpoint='inclui ultimo valor','retstep='inclui razao) ]

print(Z.shape) # dados dimensionais do array [ 'array'.shape ]
print(Z.size) # número de valores no array [ 'array'.size ]
print(Z.ndim) # número de dimensões do array [ 'array'.ndim ]

B = np.array([10,20,30])

C = np.concatenate((A,[15,25,35])) # juntar arrays de mesma dimensão [ np.concatenate(('array1','array2')) ]
print(C)
print(np.concatenate((A,B)))

print(M[M<3]) # selecionando dados de um array por uma condição [ 'array'['array''condição'] ]

print(M.sum()) # soma dos os dados de um array [ 'array'.sum() ]
print(M.min()) # menor valor de um array [ 'array'.min() ]
print(M.max()) # maior valor de um array [ 'array'.max() ]
print(M.mean()) # média dos valores de um array [ 'array'.mean() ]

rng = default_rng() # dando apelido para uma função [ 'apelido' = 'função'() ]

print(rng.integers(15, size=(2,3)))  
# criação de um array com valores aleatórios [ rng.integers('conjunto de números'),size=('linhas','colunas') ]
'''
