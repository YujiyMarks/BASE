print("Hello World") # printar uma mensagem na tela

# comentário

# variaveis
a <- 10 # atribuir valor a uma variavel
b = 5 
a+b -> c
a
c
print(a)



# strings
a <- "teste"
a

# ?c # ajuda sobre um comando

# listas
l <- list(a,2,"bruno",a) # criação de uma lista
l

l[1] # mostra o primeiro elemento da lista
l[2:4] # mostra os elementos de posição 2 a 4 
l[-2] # mostra todos os elementos menos o na posição 2

is.list(l) # função para verificar se é uma variavel é uma lista
length(l) # função que mostra a quantidade de elementos de uma lista


# vetores (lista com todos dados sendo do mesmo tipo)
v <- c(2,5,7) # criação de um vetor 
u <- c(2,"5",7,5)
w <- c(4,10,14,2,2,2)
v
u
is.vector(v) # função para verificar se uma variavel é um vetor
is.vector(u)
v+w

r <- list(v,a,2) # criação de lista com um vetor dentro
r
r[1]
r[[1]][2] # segundo elemento do vetor na primeira posição


# matrizes
m <- matrix(1:12, nrow=3, ncol=4) # criação de uma matriz com valores de 1 a 12, 3 linhas e 4 colunas
m
m[2,3] # elemento da linha 2 e coluna 3
m[2,3] <- 10 # altera o valor do elemento [2,3]
m[2,3]


# operações
3^2 == 9 & 6.1 > 5 # operador "e"
4 <= 1 | 2 != 2 # operador "ou"


# funções numéricas
d <- 10.67
n <- "2"
di <- as.integer(d) # tira as casas decimais de um número
dd <- round(d) # arredonda para um numero inteiro
di
dd
di + d
n
n <- as.numeric(n) # transforma strings de numeros em numerico
n
sum(v) # soma todos os valores de um vetor

# fatores (vetor mas com os dados iguais agrupados)
F <- as.factor(u) # transforma um vetor em fator 
F


# categorização de variaveis
summary(F) # mostra propriedades de uma variavel
mode(F) # mostra o tipo de dado da variavel
class(F) # mostra o tipo da variavel
str(F) # mostra resumo de uma variavel


# pacote stringr
install.packages("stringr") # instalar um pacote
library(stringr)

nome <- "B"
sob <- "Y"
str_c(nome," ",sob)


# arquivos
getwd()
#setwd("C:/caminho") # define a area de trabalho
df <- read.csv("Vendas.csv") # importa um arquivo csv


# dataframes
df
# view(df) # visualizando um dataframe

df[1] # visualiza a primeira coluna do dataframe
df[1,] # visualiza a primeira linha do dataframe
df[1,2] # visualiza o elemento da primeira linha e segunda coluna do dataframe
df[1:2,-2]

df1 <- df[1] # cria um data frame com os dados apenas da coluna 1
df1
df2 <- df$Produto # cria uma variavel com os dados de uma coluna especifica
df2

df$Sobrenome <- NULL # exclui uma coluna de um dataframe
df$ULTIMA <- NA # cria uma nova coluna
df$ULTIMA[1:100] <- 1 # insere valores em uma coluna em um intervalo de linhas

df$ULTIMA[2]
df[df$ULTIMA == 1,]

#
nomes <- c("Bruno","Yuji","Marques")
idades <- c(15,20,25)
dff <- data.frame(nomes,idades)
dff


# condições
# if
if (a == 2) # condição se, senão
{
  a <- 10
} else {
  "Falsificado" # forma de printar uma mensagem
}
# for
for (i in idades) # condição para
{
  print(i)
}
# while 
x <- 0
while (x == 0) # condição enquanto
{
  print(x)
  x <- x+1
}


# funções
x <- 2
y <- 5

soma <- function(a,b) # criação de uma função
  print(a+b)

soma(x,y) # chamando uma função


x <- seq(-pi, pi, 0.1)
plot(x, cos(x))
