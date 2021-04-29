"""
autor: Esdras Battosti, RA: 2143470, MA66B-L81, Curso: Engenharia de Controle e Automacao
professora: Dra. Glaucia Bressan
programa que resolve sistemas lineares pelos métodos de eliminação de gauss, Gauss-Jacobi e Gauss-Seidel
"""

# bibliotecas:

from time import sleep
from pandas import DataFrame

# funcoes:
def increase_matrix(matrix_coefficients, matrix_constants): # cria uma matriz aumentada
	global level

	for row in range(level): # percorre a matriz na linha e adiciona a constante ao final
		matrix_coefficients[row].append(matrix_constants[row])
	increased_matrix = matrix_coefficients
	return increased_matrix


def verifica_diagonal(matrix_coefficients):
	global level
	status = 0 # 1 se o coeficiente não é nulo, 0 se nulo

	for index in range(level):
		if matrix_coefficients[index][index] == 0:
			status += 0
		else:
			status += 1

	if status == level:
		return True
	else: # poderia ser suprimido pois funções só retornam 1 vez
		return False


def gauss_seidel(matrix_coefficients, matrix_constants, approximations):
	global level
	vector = approximations[-1].copy() # armazena as solucoes encontradas
	sum = float() # armazena o resultado das operações na linha

	for row in range(level):
		sum = 0 # deixa a soma como 0 para a próxima linha
		for column in range(level):
			if row != column: # se não for elemento da diagonal principal
				sum -= matrix_coefficients[row][column] * vector[column]
		sum += matrix_constants[row] # soma a constante
		sum /= matrix_coefficients[row][row] # divide pelo coeficiente da diagonal principal
		vector[row] = sum # armazena a solução encontrada no vetor de aproximações

	return vector


def get_approximation(): # obtem as aproximações inicias do método de jacobi e seidel
	global level
	vector = list() # cria um vetor para ser inserido nas solucoes
	print('-'*30)
	for row in range(level):
		# captura as solucoes iniciais do usuario
		vector.append(input_float(f'Insira a aproximacao para x{row + 1}:\n'))
	print('-'*30)

	return vector # retorna as solucoes inicias


def gauss_jacobi(matrix_coefficients, matrix_constants, approximations):
	global level
	solutions = list()
	sum = float()

	for row in range(level):
		sum = 0 # deixa a soma como 0 para a próxima linha
		for column in range(level): # se não for elemento da diagonal principal
			if row != column:
				sum -= matrix_coefficients[row][column] * approximations[-1][column]
		sum += matrix_constants[row] # soma a constante
		solutions.append(sum / matrix_coefficients[row][row]) # divide pelo coeficiente da diagonal e insere no vetor solução

	return solutions


def print_system(matrix_coefficients, matrix_constants): # printa o sistema
	global level

	for row in range(level):
		for column in range(level):
			if column == 0:
				print(f'{matrix_coefficients[row][column]}x{column + 1} ', end = '')	
			else:
				print(f'{abs(matrix_coefficients[row][column])}x{column + 1} ', end = '')

			if column < level - 1:
				if matrix_coefficients[row][column + 1] >= 0: # regra para por o - ou + na operação do sistema linear
					print('+ ', end = '')
				else:
					print('- ', end = '')

		print(f'= {matrix_constants[row]}') # printa as constantes


def print_matrix(matrix_coefficients, matrix_constants): # printa a matriz
	global level

	for row in range(level):
		for column in range(level):
				print(f'{matrix_coefficients[row][column]} ', end = '')	
		print(f'  {matrix_constants[row]}') # printa as constantes


def line_criterion(matrix_coefficients):
	global level
	sum = float()
	alpha_k = list() # alfas do metodo das linhas
	pivo = list() # vetor com os elementos da diagonal principal

	for row in range(level):
		sum = 0 # zera a soma para a próxima linha
		for column in range(level):
			if row != column: # se não é elemento da diagonal é somado
				sum += abs(matrix_coefficients[row][column])
			else: # se é elemento da diagonal entra no vetor de elementos da diagonal principal
				pivo.append(abs(matrix_coefficients[row][column])) 
		alpha_k.append(sum)

	if max(alpha_k) < max(pivo): # faz a verificação
		# é matematicamente identico a verificar se \max((\sum_{j=n,i \neq j}^{grau} |a_{ij}| ) / |a_ii|) < 1
		print('\nPelo criterio das linhas, podemos afirmar que o metodo converge\n')
		print('-'*30) 
		sleep(3) # aguarda 3 segundos para leitura do usuario
	else:
		print('\nPelo criterio das linhas, nada podemos afirmar\n') 
		print('-'*30)
		sleep(3)


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


def elimination(matrix_coefficients, matrix_constants): # transforma a matriz completa em uma matriz triangular superior
	global level
	iteration = 1 # conta as iterações

	for column in range(1, level): # navegar nas colunas da matriz
		print('-'*30)
		print(f'Etapa {iteration}\n')
		print(f'pivo = {matrix_coefficients[column - 1][column - 1]}') # como column começa em 1 precisamos dos elementos inicados em 0

		for row in range(column + 1, level + 1): # navegar nas linhas  da matriz
			# cálculo do multiplicador
			multiplier = matrix_coefficients[row - 1][column - 1]/matrix_coefficients[column - 1][column - 1]

			# zera os elementos abaixo do pivô
			matrix_coefficients[row - 1][column - 1] = 0

			# calcula os novos elementos da matriz de constantes a partir do multiplicador
			matrix_constants[row - 1] = matrix_constants[row-1] - multiplier * matrix_constants[column-1]

			for column2 in range(column+1, level+1):
				# calcula os novos elementos da matriz de coeficientes a partir do multiplicador
				matrix_coefficients[row - 1][column2 - 1] = matrix_coefficients[row - 1][column2-1] - multiplier * matrix_coefficients[column - 1][column2 - 1]

			print(f'm{row} = {multiplier}')
		m_matrix = DataFrame(increase_matrix(matrix_coefficients, matrix_constants)) # estrutura dataframe do pandas
		print(f'\nM{column} =\n') 
		print(m_matrix) # mostra matriz M_k
		iteration += 1

	return matrix_coefficients, matrix_constants


def solve_upper_triangle_matrix(matrix_upper, matrix_constants): # resolve a matriz triangular superior
	global level
	solutions = [0] * level # cria um vetor nulo para com tamanho n para n linhas da matriz
	solutions[level - 1] = matrix_constants[level - 1] / matrix_upper[level - 1][level - 1]

	for row in range(level - 1, 0, -1): # percorre a matriz com o passo -1 de n-1 a 0
		sum = 0
		for column in range(row + 1, level + 1, 1):
			sum += matrix_upper[row-1][column-1]*solutions[column-1]
		solutions[row - 1] = (matrix_constants[row - 1] - sum) / matrix_upper[row - 1][row - 1]
   
	return solutions

# startando variáveis:

matrix = list() # matriz de coeficientes do sistema
constants = list() # matriz de constantes do sistema
error = float() # erro do método de resolução
solutions = list() # matriz de soluções
iteration = 0 # contador de iterações
MAX_ITERATION = 100 # maximo de iterações

# dados iniciais:

print('Programa para resolucao de sistemas lineares\n')
print('Voce deseja inserir a matriz ou usar uma de exemplo?\n1. Inserir a matriz\n2. Matriz exemplo\n')
while True:
	option = input_int()
	if option != 1 and option != 2:
		print('Opcao invalida, insira 1 ou 2\n')
	else:
		break
print('-'*30)

if option == 1: # matriz inserida pelo usuário

	while True:
		level = input_int('\nQual o grau da matriz?\n') # define o grau da matriz
		if level <= 1:
			print('\nGrau invalido!')
		else:
			break

	print('-'*30)
	for row in range(level):
		vector = list() # cria um vetor e na próxima iteracao o recria
		for column in range(level):
				print(f'Insira o elemento a{row + 1}{column + 1}:')
				vector.append(input_float())
		matrix.append(vector) # preenche a matriz 
		print(f'Insira o elemento b{row + 1}:')
		constants.append(input_float()) # preenche o vetor de constantes
	print('-'*30)


	print('-'*30+'\n'+'Sistema Inicial\n') # printa o sistema inserido
	print_system(matrix, constants)
	print('-'*30)

# escolha do método:

print('Qual metodo de resolucao sera usado?\n1. Eliminacao de Gauss\n2. Gauss-Jacobi\n3. Gauss-Seidel\n')

while True:
	method = input_int()
	if method < 1 or method > 3:
		print('Opcao invalida, insira um numero de 1 a 3\n')
	else:
		break

# métodos de resolução:

if method == 1: # resolução por eliminação de gauss

	if option == 2: # matriz exemplo (exercício 3 da lista 3)

		level = 3 # pois o exemplo é de grau 3
		matrix = [[3, -2, 5],
         		[6, -9, 12],
         		[-5, 0, 2]]

		constants = [20, 51, 1]

	print('-'*30+'\n'+'Sistema Inicial\n')
	print_system(matrix, constants) # invoca a funcao de printar matriz
	print('-'*30)

	matrix, constants = elimination(matrix, constants) # invoca a função
	solutions = solve_upper_triangle_matrix(matrix, constants) # invoca a função

	print('-'*30+'\n'+'Solucoes')
	print(f'S = {solutions}') # print as soluções encontradas
	print('-'*30)

if method == 2: # resolução pelo método de Gauss-Jacobi

	if option == 2: # matriz exemplo (exercício 4 da lista 4)

		level = 3 # pois o exemplo é de grau 3
		matrix = [[-10, 2, 2],
         		 [1, 6, 0],
         		 [-1, 1, 3]]

		constants = [-8, 7, 0]
		solutions.append([0, 0, 0]) # aproximacao inicial

		print('-'*30+'\n'+'Sistema Inicial\n') # printa o sistema inserido
		print_system(matrix, constants)
		print('-'*30)

	if verifica_diagonal(matrix):

		if option == 1: # usuario inserirá o vetor aproximação se assim escolher
			solutions.append(get_approximation())

		print('-'*30)
		absolute_error = input_float('Insira o erro absoluto maximo desejado:\n') # captura do erro esperado
		MAX_ITERATION = input_int('Insira o maximo de iteracoes:\n')
		print('-'*30)

		print(f'\nVetor aproximacao = {solutions}')
		line_criterion(matrix) # calcula se o metodo é convergente pelo critério das linhas

		while True:
			solutions.append(gauss_jacobi(matrix, constants, solutions)) # calcula as novas soluções e as adiciona na matriz soluções
			error = abs(max(solutions[-1]) - max(solutions[-2])) / abs(max(solutions[-1])) # o índice -1 se refere ao último elemento (linha) da matriz soluções, -2 o penúltimo
			iteration += 1
			print(f'\nIteracao {iteration}')
			print(f'S{iteration} = {solutions[-1]}')
			print(f'Erro = {error}\n')
			if error <= absolute_error or iteration > MAX_ITERATION: # quando o erro do processo for menor que o erro desejado, paramos de calcular
				break

		print(f'\nSF = {solutions[-1]}') # printa a ultima solução calculada

	else:
		print('Pelo menos uma das diagonais principais e nula, o sistema nao tera solucao')
		print('-'*30)
		sleep(3)

if method == 3: # resolução pelo método de Gauss-Seidel

	if option == 2: # matriz exemplo (exercício 1 da lista 4)

		level = 4 # pois o exemplo é de grau 3
		matrix = [[10, 2, -3, 2],
         		[2, -15, 3, -2],
         		[1, -3, 20, 2],
         		[2, 2, -1, 30]]

		constants = [32, -59, -38, 160]
		solutions.append([0, 0, 0, 0]) # aproximacao inicial

		print('-'*30+'\n'+'Sistema Inicial\n') # printa o sistema inserido
		print_system(matrix, constants)
		print('-'*30)

	if verifica_diagonal(matrix):

		if option == 1:
			solutions.append(get_approximation())

		print('-'*30)
		absolute_error = input_float('Insira o erro absoluto maximo desejado:\n')
		MAX_ITERATION = input_int('Insira o maximo de iteracoes:\n')
		print('-'*30)

		line_criterion(matrix)

		print(f'\nVetor aproximacao = {solutions}')
		
		while True:
			solutions.append(gauss_seidel(matrix, constants, solutions))
			error = abs(max(solutions[-1]) - max(solutions[-2])) / abs(max(solutions[-1])) # o índice -1 se refere ao último elemento (linha) da matriz soluções, -2 o penúltimo
			iteration += 1
			print(f'\nIteracao {iteration}')
			print(f'S{iteration} = {solutions[-1]}')
			print(f'Erro = {error}\n')
			if error <= absolute_error or iteration > MAX_ITERATION: # quando o erro do processo for menor que o erro desejado, paramos de calcular
				break

		print(f'\nSF = {solutions[-1]}')
	else:
		print('Pelo menos uma das diagonais principais e nula, o sistema nao tera solucao')
		print('-'*30)
		sleep(3)