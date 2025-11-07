
edad = int(input("Cuantos años tienes"))
documento = int(input("tienes documento---- 1) SI TENGO ------- 2) NO TENGO"))

if edad < 0 or documento not in [1, 2]:
    print("datos erroneos")
    
else: 
    
    if edad >= 18 and documento == 1:
        print("Puedes entrar")
    
    elif edad < 18 and documento == 1:
        print("Entrada denegada")
        
    elif edad >= 18 and documento == 2:
        print("Debe presentar documento")
        
    elif edad < 18 and documento == 2:
        print("Entrada denegada")
        
    