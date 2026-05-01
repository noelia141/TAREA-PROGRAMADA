#Función para  carga de tokens
def cargarTokens(nombreArchivo, separador):
    """
    Lee el archivo de tokens línea por línea.
    Utiliza una estructura de control simple y manejo de excepciones.
    """
    listaTokens = []
    try:
        #Se abre el archivo en modo lectura ("r") como se vio en la Agenda
        archivo = open(nombreArchivo, "r", encoding="utf-8")
        #Se lee la primera línea para saltar los encabezados
        archivo.readline()#.readline() lee una sola línea completa del archivo, desde la posición actual hasta encontrar un salto de línea o el final del archivo.
        #Se inicia el ciclo de lectura
        while True:
            linea = archivo.readline()#.readline() lee una sola línea completa del archivo, desde la posición actual hasta encontrar un salto de línea o el final del archivo.
            #Si la línea está vacía, se llegó al final del flujo del archivo.
            if linea == "":
                break
            #Se limpia la línea de saltos de línea.
            linea = linea.strip()
            if linea != "":
                #Se busca la posición del separador para dividir la cadena.
                posicion = linea.find(separador) #.find() busca una secuencia de caracteres dentro de un string y devuelve la posición donde comienza.
                if posicion != -1: 
                    #Se crea un slicing simple para obtener llave y valor.
                    llave = linea[:posicion]
                    valor = linea[posicion + 1:]
                    # Se agrega la sublista a la lista de listas
                    listaTokens.append([llave, valor]) #.append() agrega un nuevo elemento al final de una lista existente, aumentando su tamaño en uno.
        archivo.close()
        return listaTokens
    except FileNotFoundError:#Esto se activa únicamente cuando el nombre del archivo que le pasamos a open() no existe en la carpeta o la ruta está mal escrita.
        return "Error: No existe el archivo."
    except Exception: #Esto captura cualquier otro error que no sea la falta del archivo.
        return "Error en la lectura de datos."
