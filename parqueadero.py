hora = 2000
multa = 5000
cantidad = int(input("ingresa numero de horas"))

if cantidad < 0:
    print("datos erroneos")
    
else:
    total = hora
    
    if cantidad < 5:
        total = cantidad * hora
         
    elif cantidad >= 5:
        total = cantidad * hora + (multa)
    

print (f"el total a pagar es: {total:}")