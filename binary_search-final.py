
# Assignment 2 - Metodologias Experimentais em Informática
#
# Este programa implementa a pesquisa binária num array ordenado.
#
# Funcionalidade:
# 1. Utiliza o algoritmo de pesquisa binária para encontrar a posição de um elemento alvo num array ordenado.
# 2. Exibe a posição do elemento alvo se encontrado, ou uma mensagem indicando que o elemento não está presente.
#
# Algoritmo:
# O algoritmo de pesquisa binária divide repetidamente o array ao meio e compara o elemento alvo com o valor no meio.
# Se o valor do meio é igual ao alvo, a posição é retornada. Caso contrário, o algoritmo ajusta os limites da pesquisa com base
# na comparação e repete o processo até encontrar o elemento ou determinar que ele não está presente no array.


def binary_search(arr, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

    return 1

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    size = len(numbers)

    index = binary_search(numbers, target, 0, size - 1)

    if index != -1:
        print(f"Index of {target}: {index}")
    else:
        print(f"{target} not found in the array.")

if __name__ == "__main__":
    main()
