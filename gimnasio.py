dias = int(input("cuantos dias entrenaste esta semana: "))


if dias < 0:
    print("cantidad invalida")
    
else:
    
    if dias <= 1:
        print("No aflojes, tú puedes mejorar")
         
    elif dias <= 3:
        print("Bien, pero puedes dar más")
        
    else:
        print("¡Excelente disciplina! + gana 1 punto de energía")