panes = 300
cantidad = int(input("cuantos panes quieres: "))

if cantidad < 0:
    print("cantidad invalida")
else:
    precio_unitario = 300
    
total = cantidad * precio_unitario

if cantidad > 50:
    descuento = 0.20
     
elif cantidad > 20:
    descuento = 0.10
else:
    descuento = 0
    
totalDescuento = total * (1 - descuento)

if descuento > 0:
    print(f"Se aplicó un {int(descuento*100)}% de descuento.")
print(f"Total a pagar: ${totalDescuento:}")
    