

while True:                                                                                      #se crea el ciclo while para que si el usuario se equivoca vuelva a mostrar la pregunta
    try:
        nombre = str(input("cual es tu nombre: "))                                               # se pide por consola que digite el nombre del usuario
        break                                                                                    #si todo sale bien se cierra el ciclo while
    except ValueError:                                                                           # Si ocurre un error (por ejemplo, un valor inválido), se muestra este mensaje
        print("Por favor ingrese un nombre válido: ")                                            # se muestra el mensaje de error
        
while True:                                                                                      #se crea otro while para el ciclo de el precio
    try:
        precio = float(input("Digita el precio: "))                                              #se pide el precio por consola
        break                                                                                    #si todo sale bien se cierra el ciclo while
    except ValueError:                                                                           # Si ocurre un error (por ejemplo, un valor inválido), se muestra este mensaje
        print(" ERROR: debes ingresar un número válido para el precio: ")                        # se muestra el mensaje de error
        
while True:                                                                                      #se crea el ultimo ciclo while para la cantidad
    try:       
        cantidad = int(input("Ingrese la cantidad: "))                                           #se pide la cantidad por consola
        break                                                                                    #si todo sale bien se cierra el ciclo while
    except ValueError:                                                                           # Si ocurre un error (por ejemplo, un valor inválido), se muestra este mensaje
        print("ERROR: Ingrese una cantidad válida: ")                                            # se muestra el mensaje de error
        
costo_total = precio * cantidad                                                                  #declara la variable costo_total y hace la respectiva multiplicacion para que se sepa el costo total

        
print(f"NOMBRE: {nombre} ||  CANTIDAD: {cantidad} || PRECIO UNITARIO: {precio} || COSTO TOTAL: {costo_total}")        #al final se muestra por consola este mensaje que integra todas las variables almacenadas


""" el codigo lo que hace es pedirle al usuario que ingrese su nombre, la cantidad de objetos adquiridos
y si la cantidad no es un numero le muestra un error y el while le vuleve a hacer la pregunta hasta que el usuario ingrese un numero, 
lo mismo pasa con la cantidad, y luego se hace la multiplicacion de precio por cantidad para hallar el costo total de los productos, 
luego se muestra por consola la informacion que puso el usuario de manera organizada y le aoarece al final el costo total de los productos adquiridos."""