"""
autor: Esdras Battosti, RA: 2143470, MA66B-L81, Curso: Engenharia de Controle e Automacao
professora: Dra. Glaucia Bressan
programa que resolve sistemas lineares pelo método de eliminação de gauss
"""

# funcoes:

def elimination(matrix_coefficients, matrix_constants):
	length = len(matrix_constants)  # calcula o tamanho da matriz

	for column in range(1, length):
		for row in range(column+1, length+1):
			multiplier = matrix_coefficients[row-1][column-1]/matrix_coefficients[column-1][column-1]

			matrix_coefficients[row-1][column-1] = 0

			matrix_constants[row - 1] = matrix_constants[row-1] - multiplier * matrix_constants[column-1]

			for column2 in range(column+1, length+1):
				matrix_coefficients[row-1][column2-1] = matrix_coefficients[row - 1][column2-1] - multiplier * matrix_coefficients[column-1][column2-1]

	return matrix_coefficients, matrix_constants


def  solve_upper_triangle_matrix(matrix_upper, matrix_constants):
	length = len(matrix_constants)
	solutions = [0] * length
	solutions[length-1] = matrix_constants[length-1] / matrix_upper[length-1][length-1]


	for row in range(length-1, 0, -1):
		sum = 0

		for column in range(row+1, length+1, 1):
			sum += matrix_upper[row-1][column-1]*solutions[column-1]

		solutions[row-1] = (matrix_constants[row-1]-sum) / matrix_upper[row-1][row-1]
   
	return solutions

# dados iniciais

matrix = [[3, 2, 4],
         [1, 1, 2],
         [4, 3, -2]]


constants = [1, 2, 3]


# resolucao do sistema 

matrix, constants = elimination(matrix, constants)
solutions = solve_upper_triangle_matrix(matrix, constants)
print(f'x = {solutions}')
