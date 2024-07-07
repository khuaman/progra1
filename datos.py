def pregunta_1(frase: str) -> str:
    """
    Indica la secuencia de números a digitar para codificar el mensaje
    Parámetros:
            frase (str) :  mensaje 
    Retorna:
    str: que contiene la secuencia de teclas a digitar considerando la cantidad de veces que habría que presionar cada tecla para escribir el mensaje.

    Tome como referencia el teclado de un celular para codificar el mensaje.

    |--Tecla--|----Letras---|
    |    1    |  . , ? ! :  |
    |    2    |   A B C     |
    |    3    |   D E F     |
    |    4    |   G H I     |
    |    5    |   J K L     |
    |    6    |   M N O     |
    |    7    |   P Q R S   |
    |    8    |   T U V     |
    |    9    |   W X Y Z   |
    |    0    |   espacio   |
    |---------|-------------|
    """
    return "Aquí va tu solución"


def pregunta_2(diccionario: dict) -> dict:
    """
    Ordena alfabéticamente cada lista asociada a cada departamento
    Parámetro:
        diccionario (dict) : diccionario con información de departamentos  y lista de platos típicos
    Retorna:
            dic (dict): diccionario con departamentos y con lista ordenada alfabéticamente de sus platos típicos.
    """
    dic = {}
    return dic


def pregunta_3(lista: list) -> list:
    """	
    Obtiene la información de los 7 mejores atletas en base a su puntaje (pt).

    Parámetros:
        lista (list) : lista de diccionarios con información de atletas
    Retorna:
            lista(list): lista de diccionarios con información de los 7 mejores atletas
    """
    return []


def pregunta_4(lista: list, pais: str) -> list:
    """	
    Obtiene los nombres de los atletas de un determinado país en una lista.
    Parámetros:
            lista(list) : lista de diccionarios con información de atletas
            pais(str) : país por el cual filtrar la información
    Retorna:
            list(list): lista de nombres del país
    """
    array = []
    for e in lista:
        if e["pais"] == pais:
            array.append(e["nombre"])
    return array


# EJEMPLOS DE ENTRADA Y SALIDA


ejemplo_comidas = {
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
        "Piridata",
        "Patasca",
        "Cancacho de cordero"
    ]
}

ejemplo_atletas = [
    {"nombre": "Jin Boyang", "pais": "China", "pt": 297.77},
    {"nombre": "Dmitri Aliev", "pais": "Rusia", "pt": 267.51},
    {"nombre": "Mijail Koliada", "pais": "Rusia", "pt": 264.25},
    {"nombre": "Javier Fernandez", "pais": "Espana", "pt": 305.24},
    {"nombre": "Patrick Chan", "pais": "Canada", "pt": 263.43, },
    {"nombre": "Adma Rippon", "pais": "Estados Unidos", "pt": 259.36},
    {"nombre": "Oleksii Bychenko", "pais": "Israel", "pt": 257.01},
    {"nombre": "Keegan Messing", "pais": "Canada", "pt": 255.43},
    {"nombre": "Yuzuru Hanyu", "pais": "Japon", "pt": 317.85},
    {"nombre": "Daniel Samohin", "pais": "Israel", "pt": 251.44},
    {"nombre": "Cha Jun-hwan", "pais": "Corea del Sur", "pt": 248.59},
    {"nombre": "Shoma Uno", "pais": "Japon", "pt": 306.90},
    {"nombre": "Michal Brezina", "pais": "Republica Checa", "pt": 246.07},
    {"nombre": "Misha Ge", "pais": "Uzbekistan", "pt": 244.94},
    {"nombre": "Keiji Tanaka", "pais": "Japon", "pt": 244.83},
    {"nombre": "Nathan Chen", "pais": "Estados Unidos", "pt": 297.35},
    {"nombre": "Deniss Vasiljevs", "pais": "Letonia", "pt": 234.58},
    {"nombre": "Brendan Kerry", "pais": "Australia", "pt": 233.81},
    {"nombre": "Jorik Hendrickx", "pais": "Belgica", "pt": 248.95},
    {"nombre": "Vincent Zhou", "pais": "Estados Unidos", "pt": 276.69}
]


def __main__():
    print(pregunta_4(ejemplo_atletas, "Japon"))


__main__()
