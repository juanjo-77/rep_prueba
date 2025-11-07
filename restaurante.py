menu = 12000
precioBebidas = 3000
iva = 0.08

bebidas = int(input("quieres bebida---  1) SI ---- 2) NO---"))


if bebidas == 1:
    total = menu + precioBebidas
    total_con_iva = total * (1 + iva)  
    print(f"Total a pagar con IVA incluido: ${total_con_iva: }")
    
elif bebidas == 2:
    total_con_iva = menu * (1 + iva) 
    print(f"Total a pagar con IVA incluido: ${total_con_iva: }")
     
else:
    print("Opción no válida. Hasta la próxima.")