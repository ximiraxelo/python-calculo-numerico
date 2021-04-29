"""
autor: Esdras Battosti, RA: 2143470, MA66B-L81, Curso: Engenharia de Controle e Automacao
professora: Dra. Glaucia Bressan
programa que interpola funções pelo método de newton e lagrange
"""

#bibliotecas:

import matplotlib.pyplot as plt 
from pandas import DataFrame
from numpy import arange
from time import sleep

#funções:

def lagrange_interpolation(point, points_x, points_y, degree): # interpolacao pelo método de lagrange
    estimate = 0 # estimativa pelo metodo de lagrange

    for index in range(degree + 1): # o k do metodo matematico
        lagrange = 1 # variavel que armezena os 'L's do método de lagrange
        for index2 in range(degree + 1): # o j do metodo matematico
            if index != index2: # k e j não podem ser iguais
                # calculo do L
                lagrange *= (point - points_x[index2])/(points_x[index] - points_x[index2])
        estimate += points_y[index] * lagrange # calculo da estimativa, L_0*f(x_0) + L_1*f(x_1) ...

    return estimate


def newton_interpolation(point, points_x, points_y, print_df=True): # interpolacao pelo metodo de newton
    lenght = len(points_x) # quantidade de pontos
    dd_table = [[None for x in range(lenght)] for x in range(lenght)]
    # criando uma matriz nula com list comprehension
    estimative = [None for x in range(lenght)] # armazena o valor da interpolacao de newton

    for index in range(lenght):
        dd_table[index][0] = points_y[index] # adiciona os valores de f(x) na primeira coluna
    for index2 in range(1, lenght): # calculo da tabela
         for index3 in range(lenght - index2):
                dd_table[index3][index2] = ((dd_table[index3+1][index2-1] - 
                                            dd_table[index3][index2-1]) /
                                            (points_x[index2+index3] - points_x[index3]))

    if print_df: # print se for solicitado
        dd_table_pd = DataFrame(dd_table) # transforma a matriz em uma estrutura dataframe do pandas
        print(dd_table_pd) # mostra o dataframe   

    coefficient = 1 # representa os (x - x_k) do metodo matematico
    estimative = dd_table[0][0]
    for order in range(1, lenght):
        coefficient *= point - points_x[order - 1] # calculos dos coeficientes
        estimative += dd_table[0][order] * coefficient # equivalente ao polinomio do metodo matematico

    return estimative

def get_points(): # obtem os pontos conhecidos da funcao
    points = input_int('Quantos pontos?\n') # quantidade de pontos
    counter = 0 # contador
    points_x = list() # pontos em x
    points_y = list() # pontos em f(x)

    print('-'*30)
    for point in range(points):
        points_x.append(input_float(f'\nDigite o ponto x{counter}:'))
        points_y.append(input_float(f'Digite o ponto f(x{counter}):'))
        counter += 1
    print('-'*30)

    return points_x, points_y # retorna os pontos em x e f(x)


def input_float(text = ''): # garante que o numero inserido é float
    while True:
        try:
            return float(input(f'{text}')) # retorna o valor, se correto
        except:
            print('\nValor invalido\n') # mensagem de erro
        else:
            break # sai do laco while


def input_int(text = ''):  # garante que o numero inserido é int
    while True:
        try:
            return int(input(f'{text}'))  # retorna o valor, se correto
        except:
            print('\nValor invalido\n')  # mensagem de erro
        else:
            break  # sai do laco while

#startando variáveis:

estimatives = list() # lista de valores interpolados para plotar o gráfico

#dados iniciais:

print('Programa que interpola funcoes pelo metodo de Newton e Lagrange\n')
print('Voce deseja inserir os pontos ou usar pontos de exemplo?\n1. Inserir os pontos\n2. Pontos de exemplo\n')
while True:
    option = input_int()
    if option != 1 and option != 2:
        print('Opcao invalida, digite 1 ou 2')
    else:
        break
print('-'*30)

if option == 1: # usuario insere os pontos

    print('-'*30)
    points_x, points_y = get_points() # invoca a função
    print(f'x = {points_x}')
    print(f'f(x) = {points_y}')
    print('-'*30)

if option == 2: # exercicio 1 da lista 5

    points_x = [30, 35, 45, 50, 55]
    points_y = [0.5, 0.57358, 0.70711, 0.76604, 0.81915]

    print('-'*30)
    print(f'x = {points_x}')
    print(f'f(x) = {points_y}')
    print('-'*30)

print('-'*30)
while True:
    point = input_float('Em qual ponto voce quer a estimativa?\n')
    # garante que o ponto de interesse não está fora do intervalo
    if point < min(points_x) or point > max(points_x): 
        print(f'O ponto precisa estar entre {min(points_x)} e {max(points_x)}')
    else:
        break
print('-'*30)

#escolha do método:

print('-'*30)
print('\nQual metodo de resolucao?\n1. Lagrange\n2. Newton')
while True:
    method = input_int()
    if option != 1 and option != 2:
        print('Opcao invalida, digite 1 ou 2')
    else:
        break
print('-'*30)

#execução dos métodos:

if method == 1: # metodo de lagrange

    print('-'*30)
    while True:
        print('Qual o grau do polinomio interpolador?')
        degree = input_int(f'Digite um grau de 1 a {len(points_x) - 1}\n')
        # garante que o grau seja no mínimo 1 e no máximo a quantidade de pontos fornecidos - 1
        if degree < 1 or degree > (len(points_x) - 1):
            print(f'Opcao invalida, digite um numero entre 1 e {len(points_x) - 1}\n')
        else:
            break
    print('-'*30)

    print('-'*30)
    # invoca a interpolação de lagrange e salva na variavel interpolated
    interpolated = lagrange_interpolation(point, points_x, points_y, degree)
    print(f'g({point}) = {interpolated}') # printa o resultado
    print('-'*30)

    # cria um intervalo do menor valor dos pontos de x ao maior valor, com passo 0.1
    interval = arange(min(points_x), max(points_x), 0.1)
    # para cada valor no intervalo calcula a interpolação para plotar no gráfico
    for x in interval:
        estimatives.append(lagrange_interpolation(x, points_x, points_y, degree))
    plt.plot(interval, estimatives, 'b-') # plota  a função interpolada g(x)
    plt.plot(points_x, points_y, 'ro') # plota os pontos informados em x e f(x)
    plt.plot(point, interpolated, 'rx') # plota o ponto interplado g(x_0)
    name = f'$g({point})$' 
    plt.text(1.02*point, interpolated, name, fontsize=12) # mostra o nome do ponto interpolado g(x_0)
    plt.grid(linestyle = '-', linewidth = 0.5, color = 'gray') # mostra a grade (eixos)
    plt.show() # exibe o grafico

if method == 2: # metodo de newton

    interpolated = newton_interpolation(point, points_x, points_y)
    print('-'*30)
    print(f'g({point}) = {interpolated}')
    print('-'*30)

    interval = arange(min(points_x), max(points_x), 0.1)

    for x in interval:
        estimatives.append(newton_interpolation(x, points_x, points_y, False))
    plt.plot(interval, estimatives, 'b-') # plota  a função interpolada g(x)
    plt.plot(points_x, points_y, 'ro') # plota os pontos informados em x e f(x)
    plt.plot(point, interpolated, 'rx') # plota o ponto interplado g(x_0)
    name = f'$g({point})$' 
    plt.text(1.02*point, interpolated, name, fontsize=12) # mostra o nome do ponto interpolado g(x_0)
    plt.grid(linestyle = '-', linewidth = 0.5, color = 'gray') # mostra a grade (eixos)
    plt.show()