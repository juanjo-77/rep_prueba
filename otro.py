while True:
    print("1)  recorrer numeros pares e impares")
    print("2)  decimal a binario ")
    print("3)  binario a decimal")
    print("4)  salir")

    opt = input("elige una opcion: ")

    if opt == "1":
        n = int(input(" hasta que numero: "))
        for i in range(n + 1):
            print (f"{i} es  {'par' if i % 2 == 0 else 'impar'}") 

    elif opt == "2":
        decimal = int (input("numero decimal: "))
        binaria = bin(decimal)[2:]
        print(f"el numero {decimal} en binario es {binaria}")

    elif opt == "3": 
        b = input("numero binario: ")
        print("decimal: ", int(b, 2))

    elif opt == "4":
        print("Hasta la vista \U0001F622...")
        
        break

    else:
        print("opcion no valida")
