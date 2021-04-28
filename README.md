# Introdução

Código criado para a disciplina de Cálculo Numérico (MA66B - L81) com a supervisão da professora Dr. Glaucia Bressan da UTFPR-CP

# Objetivo

## aproximar_raizes

Calcular aproximações de raízes reais de funções reais através dos métodos:

* Bissecção
* Newton-Raphson
* Secante

## sistemas_lineares

Resolver sistemas lineares através dos métodos:

* Eliminação de Gauss
* Gauss-Jacobi
* Gauss-Seidel

## interpolacao

Interpolar funções através do métodos:

* Lagrange
* Newton

# Construção

Os códigos são criados inteiramente no *Python 3.9.2* com adições das bibliotecas:

<details>
  <summary>NumPy</summary>	

  Biblioteca que adiciona funções matemática como cosseno, seno, tangente, módulo, função teto e logaritmos. Além disso, adiciona constantes matemáticas como número de euler (e) e pi.

  [Veja mais](https://numpy.org/)

</details>

<details>	
  <summary>SymPy</summary>

  Biblioteca de linguagem simbólica que tem imbutido métodos de integração e derivação. A biblioteca trabalha com strings e é possível converter-las em função anônimas (lambda) através da função lambdify().

  [Veja mais](https://www.sympy.org/en/index.html)

</details>

<details>
  <summary>Matplotlib.pyplot</summary>

  Biblioteca usada para plotar gráficos de funções e mostrar a precisão dos métodos a cada iteração.

  [Veja mais](https://matplotlib.org/)

</details>

<details>	
  <summary>Time</summary>

  Biblioteca padrão do Python para manipulação de tempo no código. Aqui usada para dar um pause possibilitando ao usuário ler informações na tela

  [Veja mais](https://docs.python.org/3/library/time.html)

</details>

<details>	
  <summary>Pandas</summary>

  Biblioteca do Python para análise/ciência de dados. Aqui usada para criar uma estrutura dataframe.

  [Veja mais](https://pandas.pydata.org/)

</details>

# Fundamentação Teórica

Para ver mais sobre os métodos de aproximação veja em:
* [Erros em Processos Numéricos](https://www.notion.so/esdrasbattosti/T-pico-1-Erros-em-Processos-Num-ricos-d25d1ca4d38b41f2932728ce275a385d)
* [Soluções Numéricas de Equações Reais](https://www.notion.so/esdrasbattosti/T-pico-2-Solu-es-Num-ricas-de-Equa-es-Reais-921ab1dc5de747f29af5aff004653fda)

Para ver mais sobre os métodos de resolução de sistemas lineares veja em:

* [Resolução Numérica de Sistemas Lineares](https://www.notion.so/esdrasbattosti/T-pico-3-Resolu-o-Num-rica-de-Sistemas-Lineares-94d7ed40ba084e9aa0cb06c2e38001a4)

Para ver mais sobre interpolação de funções veja em:

* [Interpolação Polinomial](https://www.notion.so/esdrasbattosti/T-pico-4-Interpola-o-de-fun-es-2b78010c729045eea12fd28a16bff67f)

> 📘 Disclaimer
>
> O material usado é de minha autoria (sem nenhuma licença) baseado nas aulas da professora Dr. Glaucia Bressan

