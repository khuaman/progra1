def ordenamiento_actores(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            palabra1 = [letra for letra in arr[j]["actor"]]
            palabra2 = [letra for letra in arr[j + 1]["actor"]]
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


def comparar_palabras(palabra_1, palabra_2):
    palabra1 = [letra for letra in palabra_1]
    palabra2 = [letra for letra in palabra_2]
    k = 0
    while k < min(len(palabra1), len(palabra2)):
        if ord(palabra1[k].lower()) > ord(palabra2[k].lower()):
            return -1
            # aux = arr[j]
            # arr[j] = arr[j+1]
            # arr[j+1] = aux

        elif ord(palabra1[k].lower()) < ord(palabra2[k].lower()):
            return 1
        k += 1
    if palabra1 == palabra2:
        return 0

    if k == min(len(palabra1), len(palabra2)):
        if len(palabra1) > len(palabra2):
            return -1
        else:
            return 1


def busqueda_binaria_actores(arr, actor):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2

        # Si x está presente en el medio
        #if arr[mid] < actor:
        if comparar_palabras(arr[mid]["actor"], actor) == 1:
            low = mid + 1
        # Si x está presente en el medio
        #elif arr[mid] > actor:
        elif comparar_palabras(arr[mid]["actor"], actor) == -1:
            high = mid - 1
        # x está presente en el medio
        else:
            return arr[mid]

        # Elemento no está presente en la lista
    return -1


def e1(actores):
    actor = input("Ingrese nombre de actor a buscar:")
    # FORMULA MID = LOW + (HIGH-LOW)/2
    actores = ordenamiento_actores(actores)
    resultado = busqueda_binaria_actores(actores, actor)
    if resultado == -1:
        print("No se ha encontrado al actor")
    else:
        print("Resultado: \nnombre: {} \nnacionalidad: {} \npelicula: {}".format(resultado["actor"], resultado["nacionalidad"], resultado["pelicula"]))


actores = [
    {"actor": "Felipe", "nacionalidad": "peruana", "pelicula": "loco por mary"},
    {"actor": "Gorilon", "nacionalidad": "brasilera", "pelicula": "asesinos locos"},
    {"actor": "Grecia", "nacionalidad": "cubana", "pelicula": "salvando al soldado Jacinto"},
    {"actor": "Teresita", "nacionalidad": "venezolana", "pelicula": "tres y dos son ocho"}
]

e1(actores)
