def main():
    # ARRAY

    array = [1, ["hola", "chau"], 3, 4, 5, 6]
    # Si queremos obtener el elemento '4' debemos ingresar a su indice
    print(array[3])
    # Si queremos obtener el elemento '["hola","chau"]' debemos ingresar a su indice
    print(array[1])
    # Si queremos obtener el elemento "hola" dentro de '["hola","chau"]'
    # debemos ingresar a el indice interno del array
    print(array[1][0])

    # DICCIONARIOS

    dic = {
        "key": "value",
        "array": [1, 2, 3, 4]
    }
    # Si queremos obtener el elemento 'value' debemos ingresar a su llave
    print(dic["key"])
    # Si queremos obtener el elemento [1,2,3,4] debemos ingresar a su llave
    print(dic["array"])
    # Si queremos obtener el elemento 2 que se encuentra dentro de debemos
    # [1,2,3,4] ingresar a llave del array y luego al indice del elemento
    print(dic["array"][1])


def ejercicio1(input):
    diccionario = {
        'A': '2',
        'B': '22',
        'C': '222',
        'D': '3',
        'E': '33',
        'F': '333',
        'G': '4',
        'H': '44',
        'I': '444',
        'J': '5',
        'K': '55',
        'L': '555',
        'M': '6',
        'N': '66',
        'O': '666',
        'P': '7',
        'Q': '77',
        'R': '777',
        'S': '7777',
        'T': '8',
        'U': '88',
        'V': '888',
        'W': '9',
        'X': '99',
        'Y': '999',
        'Z': '9999',
        '.': '1',
        ',': '11',
        '?': '111',
        '!': '1111',
        ':': '11111',
        ' ': '0'
    }
    output = ""
    for e in input:
        if e.upper() in diccionario:  # Si el elemento en mayuscula se encuentra dentro del diccionario
            output += diccionario[e.upper()]

    return output


def bubble_sort(arr):
    n = len(arr)
    # Recorremos todos los elementos del array
    for i in range(n):
        # La última posición ya está ordenada después de cada iteración
        for j in range(0, n - i - 1):
            # Intercambiamos los elementos si están en el orden incorrecto
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

def bubble_sort2(arr):
    n = len(arr)
    # Recorremos todos los elementos del array
    for i in range(n):
        # La última posición ya está ordenada después de cada iteración
        for j in range(0, n - i - 1):

            # Intercambiamos los elementos si están en el orden incorrecto
            palabra1 = arr[j]["pt"]
            palabra2 = arr[j+1]["pt"]

            if palabra1 > palabra2:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def ejercicio2(diccionario):
    for clave, valor in diccionario.items():
        diccionario[clave] = bubble_sort(valor)
    return diccionario


def ejercicio3(array):
    array = bubble_sort2(array)
    return array[:7]

# print(ejercicio1("Hola, mundo!"))
dic = dishes = {
    "Cusco": [
        "Humitas",
        "Chayro",
        "Puchero",
        "Chicharon",
        "Choclo con queso",
        "Peske de quinua"
    ],
    "Arequipa": [
        "Chupe de camaron",
        "Rocoto relleno",
        "Zarza de papitas",
        "Americano",
        "Atomatada de lengua",
        "Costillar frito",
        "Adobo",
        "Pastel de papa"
    ],
    "Tacna": [
        "Picante a la tacneña",
        "Lapas arrebosadas",
        "Cazuela de gallina",
        "Cuy Chactado"
    ],
    "Lima": [
        "Arroz con pollo",
        "Ceviche",
        "Lomo Saltado",
        "Aereopurto"
    ],
    "Trujillo": [
        "Shambar",
        "Seco de cabrito",
        "King Kon trujillano",
        "Frito trujillano"
    ],
    "Puno": [
        "Caldo de cabeza",
        "Trucha frita",
        "Piritata",
        "Patasca",
        "Cancacho de cordero"
    ]
}
array = []
print(ejercicio2(dic))
print(ejercicio3(array))