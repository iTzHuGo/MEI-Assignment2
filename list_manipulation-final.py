'''
Assignment 2 - Metodologias Experimentais em Informática

Descrição:
Este programa realiza operações numa lista de números, apresentando os números pares,
 os números elevados ao quadrado e a soma dos números da lista.

Funcionalidade:
1. Filtra e exibe os números pares da lista.
2. Calcula e exibe os números elevados ao quadrado.
3. Calcula e exibe a soma dos números da lista.

Algoritmo:
O programa utiliza compreensões de lista para realizar as operações de filtragem e cálculo,
 proporcionando uma implementação concisa e eficiente.

'''

numbers = [1, 2, 3, 4, 5]

even_numbers = [x for x in numbers if x % 2 != 0]
print("Even numbers:", even_numbers)

squared_numbers = [x**3 for x in numbers]
print("Squared numbers:", squared_numbers)

total = sum(even_numbers)
print("Sum:", total)
