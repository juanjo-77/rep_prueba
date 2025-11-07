notaTecnica = float(input("ingresa tu nota tecnica--- ej:(5.0)"))
notaLogica = float(input("ingresa tu nota logica--- ej:(5.0)"))

nota_final = (notaTecnica * 0.7) + (notaLogica * 0.3)

if notaTecnica and notaLogica > 5:
    print("datos erroneos")


if nota_final < 0:
    print("datos erroneos") 
elif nota_final > 5:
    print("datos erroneos") 
    
else:
    
   if nota_final >= 3:
    print("APROBADO")
    
   elif nota_final < 3 and nota_final > 2:
       print("REVISION")
       
   else:
       print("REPROBADO")