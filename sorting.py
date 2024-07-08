def bubble_sort_numeros(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_palabras(arr):

    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            palabra1 = [letra for letra in arr[j]]
            palabra2 = [letra for letra in arr[j + 1]]
            k = 0
            while k < min(len(palabra1), len(palabra2)):
                if ord(palabra1[k].lower()) > ord(palabra2[k].lower()):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    # aux = arr[j]
                    # arr[j] = arr[j+1]
                    # arr[j+1] = aux
                    break
                elif ord(palabra1[k].lower()) < ord(palabra2[k].lower()):
                    break
                k += 1
            if k == min(len(palabra1), len(palabra2)):
                if len(palabra1) > len(palabra2):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def e1():
    lista_numeros = []
    num = 0
    while num != -1:
        num = int(input("Ingrese numero: "))
        if num >= 0 and num % 5 == 0:
            lista_numeros.append(num)

    lista_palabras = []
    palabra = ""

    while True:
        palabra = input("Ingrese palabra: ")
        if palabra == 'FIN':
            break
        if len(palabra) >= 3:
            lista_palabras.append(palabra.upper())

    lista_numeros = bubble_sort_numeros(lista_numeros)
    lista_palabras = bubble_sort_palabras(lista_palabras)

    return lista_numeros, lista_palabras


print(e1())
