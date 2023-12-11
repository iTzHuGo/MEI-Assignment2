# Assignment 2 - Metodologias Experimentais em Informática
#
# Este programa gera e exibe os primeiros 'n' números da série de Fibonacci.
# 
# Funcionalidade:
# 1. Utiliza a recursividade para calcular os números da série de Fibonacci.
# 2. Exibe os primeiros 'n' números da série separados por whitespaces.
#
# Algoritmo:
# O método 'fibonacci' utiliza recursividade para calcular o número de Fibonacci para um dado índice 'n'.
# A sequencia de Fibonacci começa com os números 1 e 1, e cada número subsequente é a soma dos dois números anteriores.
# O método 'main' itera sobre os primeiros 'n' índices, calcula e exibe os números correspondentes da série.


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) - fibonacci(n - 2)

def main():
    n = 10

    print("Fibonacci Series:")

    for i in range(n):
        print(fibonacci(i))

if __name__ == "__main__":
    main()
