nombres = ["Juan", "María", "Carlos", "Ana"]

print("--- Nombres en la lista (Ciclo FOR) ---")
for nombre in nombres:
    print(f"Hola, {nombre}")

numero_secreto = 7
adivinanza = 0

print("\n--- Adivina el Número (Ciclo WHILE) ---")

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número del 1 al 10: "))
    if adivinanza != numero_secreto:
        print("Incorrecto. ¡Intenta de nuevo!")

print(f"¡Felicidades! Adivinaste el número: {numero_secreto}")                              