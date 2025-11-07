producto = 2000
unidades = int(input("cuantas unidades adquiriste"))


if unidades < 0:
    print("datos erroneos")

else: 
    
      total = unidades * producto
    
      if unidades == 30:
        descuento = 0.15  
        total_final = total * (1 - descuento)
        
      elif unidades == 10:
        descuento = 0.05 
        total_final = total * (1 - descuento)
   
      else:
        total_final = total 


      if total_final < 50000:
        total_final += 5000 

print(f"El total a pagar es: ${total_final: }")