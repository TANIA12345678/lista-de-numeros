def ordenar_lista():
    # Solicita al usuario que ingrese una lista de números separados por comas
    numeros = input("Ingresa una lista de números separados por comas: ")
    
    # Divide la cadena en una lista de cadenas utilizando la coma como separador
    lista_numeros = numeros.split(",")
    
    # Convierte cada elemento de la lista de cadenas a un entero
    lista_numeros = [int(numero.strip()) for numero in lista_numeros]
    
    # Ordena la lista de números en orden ascendente
    lista_numeros.sort()
    
    # Imprime la lista ordenada
    print("La lista ordenada es:", lista_numeros)

# Llama a la función para ordenar la lista
ordenar_lista()