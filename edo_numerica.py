"""
autor: Esdras Battosti, RA: 2143470, MA66B-L81, Curso: Engenharia de Controle e Automacao
professora: Dra. Glaucia Bressan
programa que calcula EDOs pelo método de Runge-Kutta de 4 ordem.
"""

# bibliotecas

import numpy as np
import sympy as sy # bilioteca de linguagem simbólica para converter strings em funções
from time import sleep 

# funcoes
def runge_kutta(x0, f_x0, target, step): # runge kutta de 4 ordem

	for stage in range(n): # para cada etapa

		# calculo dos ks
		k1 = y_x(x0, f_x0)
		k2 = y_x(x0 + h/2, f_x0 + k1*h/2)
		k3 = y_x(x0 +h/2, f_x0 + k2*h/2)
		k4 = y_x(x0 + h, f_x0 + k3*h)

		f_x0 += (h/6)*(k1 + 2*(k2+k3) + k4) # calculo de y
		x0 += h # incrementando o ponto xk

		print('-'*35)
		print(f'Etapa {stage+1}')
		print(f'k1 = {k1}\nk2 = {k2}\nk3 = {k3}\nk4 = {k4}')
		print(f'y({x0:.4f}) = {f_x0}')
		print('-'*35)

	print(f'y({x0:.4f}): {f_x0}')


def input_float(text=''): # garante que o numero inserido é float
    while True:
        try:
            return float(input(f'{text}')) # retorna o valor, se correto
        except:
            print('\nValor invalido\n') # mensagem de erro
        else:
            break # sai do laco while


def input_int(text=''):  # garante que o numero inserido é int
    while True:
        try:
            return int(input(f'{text}'))  # retorna o valor, se correto
        except:
            print('\nValor invalido\n')  # mensagem de erro
        else:
            break  # sai do laco while


def input_string(text=''): # garante que o valor inserido é uma string
	while True:
		try:
			return str(input(f'{text}')) # retorna o valor se correto
		except:
			print('\nValor invalido\n') # mensagem de erro
		else:
			break

# startando variaveis:

x, y = sy.symbols('x y') # declara x e y como variáveis

# dados inicias:

print('Programa que resolve EDOs numericamente')
print('Você deseja inserir uma EDO ou usar alguma de exemplo?')

while True:
	option = input_int('1. Inserir EDO\n2. EDO exemplo\n\n')
	if option == 1 or option == 2:
		break
	else:
		print('Opcao invalida, digite 1 ou 2')

print('-'*35)

if option == 1:
	edo = input_string('Insira a edo, y\' = ')
	y_x = sy.lambdify([x, y], edo) # transforma a string em uma função python
	x0 = input_float('Insira o ponto x0: ') # ponto inicial em x
	f_x0 = input_float('Insira y(x0): ') # ponto inicial em y
	h = input_float('Insira o passo (h):') # passo (h)
	target = input_float('Insira o ponto de calculo desejado (x):') # ponto desejado (x)
	n = round((target-x0)/h) # calculo do numero de intervalos (n)

if option == 2: # exercicio 2 da lista 7
	edo = '2*x*y' 
	y_x = sy.lambdify([x, y], edo) # transforma a string em uma função python
	x0 = 1 # ponto inicial em x
	f_x0 = 1 # ponto inicial em y
	h = 0.1 # passo (h)
	target = 1.4 # ponto desejado (x)
	n = 4 # numero de intervalos (n)

	print('-'*35)
	print('Dados do PVI')
	print(f'y\' = {edo}')
	print(f'f({x0}) = {f_x0}')
	print(f'h = {h}')
	print(f'x = {target}')
	print('-'*35)

	sleep(3) # congela 3 segundos para o usuario ler os dados

# execução:

runge_kutta(x0, f_x0, target, h) # invoca a função