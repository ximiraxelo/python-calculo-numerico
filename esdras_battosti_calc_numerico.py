"""
autor: Esdras Battosti, RA: 2143470, MA66B-L81, Curso: Engenharia de Controle e Automacao
professora: Dra. Glaucia Bressan
programa que calcula aproximacoes de raizes pelo metodos 
da Bissecao, Newton-Raphson e Secante.
"""
# imports:

import numpy as np # importa funcoes como cos(),sen(),log()... e constantes como e e pi
import sympy as sy # biblioteca de linguagem simbólica que calcula derivadas, integrais a afins
import time # biblioteca de manipulação de tempo. 
import matplotlib.pyplot as plt # biblioteca de geração de gráficos

# funcoes:

# calcula as iteracoes necessarias para atingir o erro desejado (Bissecao)
def necessary_iterations(a_limit, b_limit):
	value_of_iterations = int(np.ceil((np.log(b_limit-a_limit)-np.log(error))/np.log(2))) 
	# aqui estamos usando o logaritmo natural e a funcao ceil (teto)
	return value_of_iterations


# calcula se o metodo de newton-raphson sera convergente
def convergence_newton_raphson(function, diff_function, value): 
	global x # usa a variavel global x

	function = sy.lambdify(x, function) # transforma function em funcao python
	second_diff_function = sy.diff(diff_function) # calcula a segunda derivada de f, sendo diff_function a primeira
	diff_function = sy.lambdify(x, diff_function) # transforma a primeira derivada em funcao python
	second_diff_function = sy.lambdify(x, second_diff_function) # transforma a segunda derivada em funcao python

	if np.fabs(function(value) * second_diff_function(value) / diff_function(value)**2) < 1:
		print('\nHa garantia de convergencia\n')
	else:
		print('\nNao ha garantia de convergencia\n')


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


def input_string(text = ''):  # garante que uma string sera inserida
    while True:
        try:
            return str(input(f'{text}'))  # retorna o valor, se correto
        except:
            print('\nValor invalido\n')  # mensagem de erro
        else:
            break  # sai do laco while


# startando variaveis:

x0 = list() # declara a lista que ira receber as solucoes xk
x = sy.symbols('x') # declarando a variavel para o sympy
absolute_error = 9.99 # starta o erro_absoluto maior que o erro minimo
iterations = 0 # starta o contador
interval = np.arange(-1, 1, 0.1) # cria uma lista de elementos de -5 a 5 com o passo 0.1, para plotarmos gráficos
   
# dados inicias e escolha do metodo a ser usado:

print(' _________________________________________________________________'
	'\n|                                                                 |'
	'\n| -Use sempre x como variavel                                     |'
	'\n| -Para potencia use **                                           |'
	'\n| -Para cosseno use cos()                                         |'
	'\n| -Para exponencial use exp()                                     |'
    '\n| -Para seno use sin()                                            |'
    '\n| -Para tangente use tan()                                        |'
    '\n| -Para logaritmo natural use log()                               |'
    '\n|_________________________________________________________________|\n'
	)

f_x = input('Digite a funcao [ex: x**5 + (1/3)*cos(x) + log(10) + exp(2*x)]:') # funcao a ser calculada
f = sy.lambdify(x, f_x) # converte a funcao de string para uma funcao do python
error = input_float('Insira o erro minimo:') # erro absoluto minimo
max_iterations = input_int('Insira o maximo de interacoes:') # maximo de interacoes
error2 = error # erro do eixo y

print('\nQual metodo de aproximacao sera usado?\n1. Bissecao\n2. Newton-Rapshon\n3. Secante\n')

while True:
    method = input_int()
    
    if method < 1 or method > 3:  # garante que o usuario digitara um numero valido
        print('\nValor invalido, insira um numero de 1 a 3:')  # mensagem de erro
    else:
    	break  # sai do laco while

# execucao do metodo escolhido:

if method == 1:  # metodo da bisseccao
	print('-------------------------\nMETODO DA BISSECCAO\n-------------------------')
	
	while True:
		limit_a = input_float('Digite o limite inicial (a):')  # limite inicial (Bissecao)
		limit_b = input_float('Digite o limite final (b):')  # limite final (Bissecao)

		if limit_a == limit_b:
			print('Os valores nao podem ser iguais\n')
		elif limit_a > limit_b: # caso limite inicial seja maior que o final, o que nao pode ocorrer
			print('\nO limite inicial e maior que o final. Os valores foram invertidos\n')
			time.sleep(2)

			# troca os valores de a e b
			memory = limit_a 
			limit_a = limit_b
			limit_b = memory

			print('\n')
			break
		elif f(limit_a) * f(limit_b) > 0: # se nao ha variacao de sinal, nao ha raiz
			print('\nSegundo o Teorema de Cauchy-Bolzano, nao ha garantia de uma raiz neste intervalo\n')

			time.sleep(1)
		else:
			print('\n')
			break
	
	if necessary_iterations(limit_a, limit_b) > max_iterations: # caso o numero minimo de interacoes calculado seja maior que o numero inserido pelo usuario
		while True:
			option = input_string(f'Sera necessario no minimo {necessary_iterations(limit_a, limit_b)} iteracoes ao inves de {max_iterations}, continuar? (S/N)\n')
			
			if option.upper() == 'S': 
				max_iterations = input_int('\nDigite o valor maximo de iteracoes:') 
				# o numero de interacoes inserido pelo usuario recebe outro valor 
				break
			elif option.upper() == 'N': # o numero de iteracoes inserido se mantem igual
				break 
			else:
				print('\nValor invalido\n')

	while iterations <= max_iterations and absolute_error >= error:
		x0.append((limit_a + limit_b)/2) # armazena os x0 numa lista
		
		print('----------------------')
		print('Iteracao',iterations)
		print(f'[{limit_a},{limit_b}]')
		
		if f(limit_a) * f(x0[iterations]) > 0: # aplica o Teorema de Cauchy-Bolzano
			limit_a = x0[iterations] 
		else:
			limit_b = x0[iterations]
		
		print(f'x{iterations} =',x0[iterations])
		print(f'f(x{iterations}) =',f(x0[iterations]))

		if iterations > 0: # na primeira iteracao (0) nao ha como calcular o erro
			absolute_error = np.fabs(x0[iterations] - x0[iterations-1]) # funcao fabs calcula o módulo (absoluto) de um numero
			print(f'Erro absoluto: {absolute_error}')
		print('----------------------\n')
		iterations += 1 # adiciona 1 no contador a cada repeticao

	# gerandos os gráficos
	plt.figure()
	plt.grid(linestyle = '-', linewidth = 0.5, color = 'red') # cria a grade no plano
	plt.plot(interval, f(interval), 'b-') # plot a função no interval
	iterations = 0 # restartando o contador	
	
	for solutions in x0: # pega todas as soluções
		plt.plot(solutions, f(solutions), 'r.') # plota a função aplicada nas soluções
		name = '$x_{' + str(iterations) + '}$' # nome de cada solução x0 no gráfico, usando LaTeX
		plt.text(solutions, 0.9 * f(solutions), name, fontsize = 12) # aplica o nome de cada ponto no gráfico
		iterations += 1 # incremento no contador
	
	plt.show() # exibe o gráfico

if method == 2: # metodo de Newton-Raphson
	f_p = sy.diff(f_x) # deriva a funcao inserida pelo usuario
	f_prime = sy.lambdify(x, f_p) # transforma a funcao de string para funcao python

	print('-------------------------\nMETODO DE NEWTON-RAPHSON\n-------------------------')
	x0.append(input_float('\nDigite o ponto inicial (x0):'))
	
	convergence_newton_raphson(f_x, f_p, x0[0]) # teste de convergência
	
	time.sleep(2) # o programa tem um delay de 2 segundos, para o leitor ler a info de convergencia
	
	while iterations <= max_iterations and absolute_error >= error:
		print('--------------------------------------------')
		print('Iteracao', iterations)
		print(f'x{iterations} = {x0[iterations]}')
		
		x0.append((x0[iterations] - f(x0[iterations]) / f_prime(x0[iterations]))) # calcula o próximo x0 de acordo com o metodo
		absolute_error = np.fabs(x0[iterations + 1] - x0[iterations]) # calculo do erro absoluto com a funcao fabs (módulo)
		
		print(f'f(x{iterations}) = {f(x0[iterations])}')
		print(f'Erro absoluto: {absolute_error}')
		print('--------------------------------------------\n')
		
		iterations += 1 # incremento no contador

	# gerando gráficos
	plt.figure()
	plt.grid(linestyle = '-', linewidth = 0.5, color = 'red') # gera a grade (eixos)
	plt.plot(interval, f(interval), 'b-') # plota a função no intervalo
	iterations = 0 # resetar o contador
	
	for solutions in x0: # pega todas as soluções
		plt.plot(solutions, f(solutions), 'r.') # plota a função aplicada nas soluções
		name = '$x_{' + str(iterations) + '}$' # nome de cada solução x0 no gráfico, usando LaTeX
		plt.text(solutions, 0.9*f(solutions), name,fontsize=12) # aplica o nome de cada ponto no gráfico
		iterations += 1 # incremento no contador
	
	plt.show() # exibe o gráfico

if method == 3: # metodo da secante
	print('-------------------------\nMETODO DA SECANTE\n-------------------------')

	x0.append(input_float('Digite o primeiro ponto (x0):'))
	x0.append(input_float('Digite o segundo ponto(x1):'))

	while True:
		print(f'\n[ {x0[iterations]} ]\n') # printa até o antepenultimo elemento
		x0.append(x0[iterations + 1] - ((x0[iterations + 1] - x0[iterations]) * f(x0[iterations + 1])) / (f(x0[iterations + 1]) - f(x0[iterations]))) 
		# uma nova solucao é adicionada à lista de solucoes
		
		if (np.fabs(f(x0[iterations + 2])) < error or np.fabs(x0[iterations + 2] - x0[iterations + 1]) < error2) and iterations <= max_iterations: # se satisfazer o erro e ter menos interacoes que o maximo
			break
		else:
			iterations += 1 # incrementa o contador

	print(f'\n[ {x0[-2]} ]\n') # printa o penultimo elemento da lista
	print(f'\n[ {x0[-1]} ]\n') # printa o ultimo elemento da lista
	print(f'{iterations} iteracoes\n')
	print(f'f(x{iterations + 2}) = {f(x0[iterations + 2])}')
	print(f'Erro absoluto: {np.fabs(x0[iterations + 2] - x0[iterations + 1])}') # calculo do erro absoluto com a funcao fabs(módulo)

	# gerando os gráficos
	plt.figure()
	plt.grid(linestyle = '-', linewidth = 0.5, color = 'red') # mostra a grade (eixos)
	plt.plot(interval, f(interval), 'b-') # plota a função no intervalo
	iterations = 0 # restar o contador
	
	for solutions in x0: # pega todas as soluções
		plt.plot(solutions, f(solutions), 'r.') # plota a função aplicada nas soluções
		name = '$x_{' + str(iterations) + '}$' # nome de cada solução x0 no gráfico, usando LaTeX
		plt.text(solutions, 0.9*f(solutions), name, fontsize = 12) # aplica o nome de cada ponto no gráfico
		iterations += 1 # incremento no contador
	
	plt.show() # exibe o gráfico