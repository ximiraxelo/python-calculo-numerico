"""
autor: Esdras Battosti, RA: 2143470, MA66B-L81, Curso: Engenharia de Controle e Automacao
professora: Dra. Glaucia Bressan
programa que calcula integrais pelos métodos de trapézios, 1/3 de simpson e 3/8 de simpson
"""

#bibliotecas:

import numpy as np
import sympy as sy # permite ao usuario inserir a funcao e derivar funcoes
import pandas as pd # usaremos para exibir melhor os pontos x, f(x)

#funcoes:

def print_points(xy_points): # printa o conjunto de pontos x, f(x)

	df = pd.DataFrame(xy_points, columns=[f'x{idx}' for idx in range(n+1)], index=['x','f(x)'])
	# converte os pontos em uma estrutura dataframe (pela visualização) usando list comprehension
	print(df)


def simpson(y_points, rule='first'): # resolve a integral pelos métodos de simpson
	if rule == 'first': # primeira regra
		sum = y_points[1][0] + y_points[1][-1] # soma dos pontos extremos

		for point in range(1, n):
			if point % 2 == 0: # se par
				sum += 2*y_points[1][point]
			else: # se ímpar
				sum += 4*y_points[1][point]

		sum *= h/3

		f_diff = differentiate(funcao, 4) # quarta derivada para o erro

		try:
			M = max(np.fabs(f_diff(y_points[0])))
		except:
			M = f_diff(y_points[0])

		error = np.fabs(h**4/180 * (b-a) * M)
		# calculo do erro com o máximo da quarta derivada

	if rule == 'second': # segunda regra

		sum = y_points[1][0] + y_points[1][-1]

		for point in range(1, n):
			if point % 3 == 0: # se multiplo de 3
				sum += 2*y_points[1][point]
			else: # se não multiplo de 3
				sum += 3*y_points[1][point]

		sum *= 3*h/8

		f_diff = differentiate(funcao, 4) # quarta derivada

		try:
			M = max(np.fabs(f_diff(y_points[0])))
		except:
			M = f_diff(y_points[0])

		error = np.fabs(h**4/80 * (b-a) * M)	
		# calculo do erro pela quarta derivada

	print('-'*35)
	print(f'Aproximacao encontrada = {sum}')
	print(f'Erro maximo = {error}')	
	print('-'*35)


def differentiate(func, degree=1): # funcao que deriva uma funcao no n grau

	diff_func = sy.diff(func, x) # primeira derivada

	if degree > 1:
		for times in range(degree-1): # deriva as outras derivadas
			diff_func = sy.diff(diff_func, x)

	return sy.lambdify(x, diff_func) # retorna a derivada com função do python


def trapezios(y_points): # metodo dos trapezios

	sum = y_points[1][0] + y_points[1][-1] # soma dos pontos externos

	for point in range(1, n): # soma dos termos internos
		sum += 2*y_points[1][point]

	sum *= h/2

	f_diff = differentiate(funcao, 2) # segunda derivada para o erro

	try:
		M = max(np.fabs(f_diff(y_points[0])))
	except:
		M = f_diff(y_points[0])

	error = np.fabs((b-a)/12 * h**2 * M)
	# calculo do erro com a segunda derivada

	print('-'*35)
	print(f'Aproximacao encontrada = {sum}')
	print(f'Erro maximo = {error}')
	print('-'*35)


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


def input_string(text = ''): # garante que o valor inserido é uma string
	while True:
		try:
			return str(input(f'{text}')) # retorna o valor se correto
		except:
			print('\nValor invalido\n') # mensagem de erro
		else:
			break 

#startando variaveis:

x = sy.symbols('x') # declarando para a sympy que x é a nossa variável
points = list() # lista de pontos xk e f(xk)

#dados iniciais:

print('Programa que calcula integrais numericamente')
print('Voce deseja inserir uma funcao ou usar uma de exemplo?\n')
while True:
	option = input_int('1. Inserir funcao\n2. Funcao exemplo\n\n')
	if option == 1 or option == 2:
		break
	else:
		print('Opcao invalida, digite 1 ou 2')

if option == 1:

	print('-'*35)
	funcao = input_string('Insira a funcao (exemplo: cos(x)**2 + x*sin(sqrt(x))):')
	f_x = sy.lambdify(x, funcao) # transforma a string inserida em uma função python
	a = input_float('Insira o limite inferior de integracao (a):') # limite de integracao a
	b = input_float('Insira o limite superior de integracao (b):') # limite de integracao b

	while True:
		n = input_int('Insira o numero de intervalos (n):')
		if n < 1:
			print('Valor invalido, digite um numero inteiro maior ou igual a 1')
		else:
			break
	print('-'*35)

print('-'*35)
print('Qual metodo de resolucao sera utilizado?\n')
while True:
	method = input_int('1. Trapezios\n2. 1/3 de Simpson\n3. 3/8 de Simpson\n\n')
	if method < 1 or method > 3:
		print('Valor invalido, digite um numero inteiro de 1 a 3\n')
	else: 
		break
print('-'*35)

if method == 1: # regra dos trapezios
	if option == 2: # exercício 7 da lista 6
		print('-'*35)
		funcao = 'exp(x**2)'
		f_x = sy.lambdify(x, funcao) # transforma a string em uma função python
		a = 0 # limite de integração a
		b = 2 # limite de integração b
		n = 5 # intervalos
		print('Dados da integral')
		print(f'f(x) = {funcao}')
		print(f'a = {a}\nb = {b}\nn = {n}\n')
	
	points.append(np.linspace(a, b, num=n+1)) # pontos x
	points.append(f_x(points[0])) # pontos f(x)
	h = (b-a)/n # calculo do passo

	print_points(points)
	print('-'*35)

	trapezios(points)

if method == 2: # primeira regra de simpson
	if option == 2: # exercicio 1 da lista 6
		print('-'*35)
		funcao = 'x*log(x)'
		f_x = sy.lambdify(x, funcao) # transforma a string em funcao python
		a = 1 # limite de integração a
		b = 2 # limite de integração b
		n = 8 # intervalos
		print('Dados da integral')
		print(f'f(x) = {funcao}')
		print(f'a = {a}\nb = {b}\nn = {n}\n')

	while True: # garante que o número de intervalos é par
		if n % 2 == 0:
			break
		else: 
			n = input_int('Insira um numero de intervalos (n) par:')

		if n < 2:
			n = input_int('Insira um numero de intervalos (n) maior que 1:')
		else:
			break			

	points.append(np.linspace(a, b, num=n+1)) # pontos x
	points.append(f_x(points[0])) # pontos f(x)
	h = (b-a)/n # calculo do passo

	print_points(points)
	print('-'*35)

	simpson(points, rule='first')

if method == 3: # segunda regra de simspon
	if option == 2: # exercicio 4 da lista 6
		print('-'*35)
		funcao = 'exp(sin(x)**2)'
		f_x = sy.lambdify(x, funcao) # converte a string em função python
		a = -np.pi/6 # limite de integração a
		b = np.pi/6 # limite de integração b
		n = 6 # intervalos
		print('Dados da integral')
		print(f'f(x) = {funcao}')
		print(f'a = {a}\nb = {b}\nn = {n}\n')

	while True: # garante que o número de intervalos é multiplo de 3
		if n % 3 == 0:
			break
		else: 
			n = input_int('Insira um numero de intervalos (n) multiplo de 3:')

		if n < 2:
			n = input_int('Insira um numero de intervalos (n) maior que 1:')
		else:
			break

	points.append(np.linspace(a, b, num=n+1)) # pontos x
	points.append(f_x(points[0])) # pontos f(x)
	h = (b-a)/n # calculo do passo

	print_points(points)
	print('-'*35)

	simpson(points, rule='second')