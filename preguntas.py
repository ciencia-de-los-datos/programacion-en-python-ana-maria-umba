"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

    
 

def pregunta_01():
    with open('data.csv', 'r') as archivo_csv:
    # Lee todas las líneas del archivo
        lineas = archivo_csv.readlines()
        lineas.count


    for linea in lineas:
        valores = linea.strip()
        
    lineas = lineas
    columna_suma = 2
    suma = 0
    for fila in lineas:
        valor = float(fila[columna_suma])
    
        suma += valor
    
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
 
    return suma



def pregunta_02():
    with open('data.csv', 'r') as archivo_csv:
    # Lee todas las líneas del archivo
        lineas = archivo_csv.readlines()
        lineas.count

    for linea in lineas:
        valores = linea.strip()

        #print(valores)


    dic = []
    suma_a = 0  
    suma_b = 0  
    suma_c = 0  
    suma_d = 0 
    suma_e = 0
    for fila in lineas:
        if fila[0] == "A":
            suma_a = suma_a + 1
        if fila[0] == "B":
            suma_b = suma_b + 1
        if fila[0] == "C":
            suma_c = suma_c + 1
        if fila[0] == "D":
            suma_d = suma_d + 1
        if fila[0] == "E":
            suma_e = suma_e + 1
    dic = [("A", suma_a), ("B", suma_b),("C", suma_c),("D", suma_d),("E", suma_e)] 

        


    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    return dic
    

def pregunta_03():

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [ 
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """   

    with open('data.csv', 'r') as archivo_csv:


        archivo_csv = [x.replace("\n", "") for x in archivo_csv ]
        archivo_csv = [y.split("\t") for y in archivo_csv ]


        # Extraemos letras y numeros 
        let = [t[0][0] for t in archivo_csv]
        val = [int(t[1]) for t in archivo_csv]


        sum_lets = {}

        #letras y valores al tiempo
        for leti, vali in zip(let, val):
            if leti in sum_lets:
                sum_lets[leti] += vali
            else:
                sum_lets[leti] = vali

        #ordenar y volver lista de tuplas
        dic = sorted([(leti, sum) for leti, sum in sum_lets.items()]) 

    return dic


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open('data.csv', 'r') as archivo_csv:
        
        archivo_csv = [x.replace("\n", "") for x in archivo_csv ]
        archivo_csv = [y.split("\t") for y in archivo_csv ]
    
    

        fecha = [t[2].split("-")[1] for t in archivo_csv]
        fecha

        dic = [(mes, fecha.count(mes)) for mes in sorted(set(fecha))]

    return dic



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    with open('data.csv', 'r') as archivo_csv:


        archivo_csv = [x.replace("\n", "") for x in archivo_csv ]
        archivo_csv = [y.split("\t") for y in archivo_csv ]

        #Extracción de valores a lista
        lets = [t[0][0] for t in archivo_csv]
        vals = [int(t[1][0]) for t in archivo_csv]
        lista = list(zip(lets, vals))

        max_min = {}

        #diccionario
        for letra, valor in lista:
            if letra not in max_min:
                max_min[letra] = {"maximo": valor, "minimo": valor}
            else:
                #Reemplazo valores
                if valor > max_min[letra]["maximo"]:
                    max_min[letra]["maximo"] = valor
                if valor < max_min[letra]["minimo"]:
                    max_min[letra]["minimo"] = valor

        dic = [(letra, max_min[letra]["maximo"], max_min[letra]["minimo"]) for letra in max_min]
        dic = sorted(dic, key=lambda result: result[0])

        
        return dic



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open('data.csv', 'r') as archivo_csv:


        archivo_csv = [x.replace("\n", "") for x in archivo_csv ]
        archivo_csv = [y.split("\t") for y in archivo_csv ]
        
        min_max_dict = {}

        #elemento 5
        for row in archivo_csv:
            col5 = row[4]
            #Separar elementos separados por , y vuelve a lista
            for key_value in col5.split(","):
                # Separar elementos llave y valor separados por ,
                key, value = key_value.split(":")
                value = int(value)
                if key in min_max_dict:

                    min_max_dict[key].append(value)
                else:
                    min_max_dict[key] = [value]
            min_max_dict
            dic = []
            for key, values in sorted((min_max_dict.items())):
                dic.append((key, min(values), max(values)))

        
    return dic



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open('data.csv', 'r') as archivo_csv:
        archivo_csv = [row_1.replace("\n", "") for row_1 in archivo_csv ]
        archivo_csv = [row_1.split("\t") for row_1 in archivo_csv ]




        dic = []
        list = [(int(t[1]), t[0]) for t in archivo_csv]

        for number in sorted(set(t[0] for t in list)):

            letters = [t[1] for t in list if t[0] == number]
            dic.append((number, letters))


        dic = sorted(dic, key=lambda x: x[0])
    

    return dic



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv', 'r') as archivo_csv:
        archivo_csv = [row_1.replace("\n", "") for row_1 in archivo_csv ]
        archivo_csv = [row_1.split("\t") for row_1 in archivo_csv ]




        dic = []
        list = [(int(t[1]), t[0]) for t in archivo_csv]

        for number in sorted(set(t[0] for t in list)):

            letters = sorted(set([t[1] for t in list if t[0] == number]))
            dic.append((number, letters))


        dic = sorted(dic, key=lambda x: x[0])

    return dic


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    with open('data.csv', 'r') as archivo_csv:
        dict_letters_values = {}
        archivo_csv = [x.replace("\n", "") for x in archivo_csv ]
        archivo_csv = [y.split("\t") for y in archivo_csv ]

        #valores de col 5 como llave y valor de dict_letters_values
        for row in archivo_csv:
            col5 = row[4]
            for key_value in col5.split(","):
                key, value = key_value.split(":")
                value = int(value)
                if key in dict_letters_values:
                    dict_letters_values[key].append(value)
                else:
                    dict_letters_values[key] = [value]
                    



        dic = { key:len(values) for key, values in sorted(dict_letters_values.items()) }
    
    return dic


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open('data.csv', 'r') as archivo_csv:
        archivo_csv = [x.replace("\n", "") for x in archivo_csv ]
        archivo_csv = [y.split("\t") for y in archivo_csv ]

        #Extrae el primer dato
        col_0 = [t[0] for t in archivo_csv]
        #Extrae el cuarto dato
        col_4 =[len(t[3].split(',')) for t in archivo_csv]
        #Extrae el quinto dato
        col_5 =[len((t[4]).split(',')) for t in archivo_csv]
        
        #Se organiza como tuplas
        dic = list(zip(col_0,col_4, col_5))
        
    return dic


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open('data.csv', 'r') as archivo_csv:
        
        archivo_csv = [x.replace("\n", "") for x in archivo_csv ]
        archivo_csv = [y.split("\t") for y in archivo_csv ]

        col_2 = [int(t[1]) for t in archivo_csv]
        col_4 = [t[3] for t in archivo_csv]

        result = {}

        for i in range(len(col_2)):
            keys = col_4[i].split(",")
            for key in keys:
                if key in result:
                    result[key] += col_2[i]
                else:
                    result[key] = col_2[i]

        sorted_dict = dict(sorted(result.items()))

        dic = {}
        for key, value in sorted_dict.items():
            dic[key] = value
            
            
        return dic



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open('data.csv', 'r') as archivo_csv:

        dic = {}

        for line in archivo_csv:
            # Separar elementos
            elements = line.strip().split('\t')
            # Obtener col 1 y col 5
            col_1, col_5 = elements[0], elements[4]
            # Procesar cadena de col 5 y sumar
            total = 0
            for pair in col_5.split(','):
                total += int(pair.split(':')[1])
            # Actualizar diccionario
            if col_1 in dic:
                dic[col_1] += total
            else:
                dic[col_1] = total

        dic = dict(sorted(dic.items()))

        return dic

