print("bienvenido, tenemos helados de chocolate y vainilla")

sabores = str(input("cual quieres: "))

vainilla = 3500
chocolate = 4000
topping = 1000

if sabores.lower() == "vainilla": 
    precio = vainilla
    
elif sabores.lower() == "chocolate": 
    precio = chocolate 
    
else:
    print("ese sabor no existe")
    precio = 0
    
if precio > 0:
    adicion = int(input("quieres un topping   1) si    2) no: "))
    if adicion == 1:
        precio += topping 
        
    print("el total seria:",precio)