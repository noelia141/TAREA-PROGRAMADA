#Función para  carga de tokens
def cargarTokens(nombreArchivo, separador):
    """
    Esta función se encarga de leer un archivo externo que contiene las 
    equivalencias de traducción y almacenarlas en la memoria del programa
    """
    listaTokens = []#Lista principal que almacenará las tuplas (palabraOriginal, palabraTraducida)
    try:
        archivo = open(nombreArchivo, "r", encoding="utf-8") #Se abre el archivo en modo lectura estandar.
        #Se lee la primera línea para saltar los encabezados
        archivo.readline()#.readline() lee una sola línea completa del archivo, desde la posición actual hasta encontrar un salto de línea o el final del archivo.
        while True: #Se inicia el ciclo de lectura
            linea = archivo.readline()
            if linea == "":#Si la línea está vacía, se llegó al final del flujo del archivo.
                break
            linea = linea.strip()#Se eliminan espacios en blanco o saltos de línea al inicio y al final.
            if linea != "": #Se busca la posición del separador para dividir la cadena.
                posicion = linea.find(separador) #.find() busca una secuencia de caracteres dentro de un string y devuelve la posición donde comienza.
                if posicion != -1: 
                    palabraOriginal = linea[:posicion] #Se extrae la palabra original y su traducción
                    palabraTraducida = linea[posicion + len(separador):] #El uso de len() permite que el separador sea de cualquier longitud
                    #Se verifica si la palabra ya fue cargada previamente
                    existe = False
                    indice = 0
                    while indice < len(listaTokens):
                        if listaTokens[indice][0] == palabraOriginal: #Se comprueba si la palabra coincide con alguna existente en la lista de tuplas
                            listaTokens[indice] = (palabraOriginal, palabraTraducida) #Si ya existe, se actualiza la tupla con la traducción más reciente
                            print("Se reescribió el token para", palabraOriginal)
                            existe = True
                            break
                        indice += 1
                    if not existe: #Si no existía, se añade como una tupla nueva a la lista.
                        listaTokens.append((palabraOriginal, palabraTraducida)) #.append() agrega un nuevo elemento al final de una lista existente, aumentando su tamaño en uno.
        archivo.close()
        return listaTokens
    except FileNotFoundError:#Esto se activa únicamente cuando el nombre del archivo que le pasamos a open() no existe en la carpeta o la ruta está mal escrita.
        return "Error: No existe el archivo."
    except Exception: #Esto captura cualquier otro error que no sea la falta del archivo.
        return "Error en la lectura de datos."