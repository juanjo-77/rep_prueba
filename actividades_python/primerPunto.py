"""8. Empresa “TecnoPlus” — Evaluación compuesta

El usuario ingresa dos notas (0.0 - 5.0):

    Prueba técnica (70%)
    Prueba lógica (30%)

Cálculo: nota_final = (tecnica * 0.7) + (logica * 0.3)

Condiciones:

    nota_final ≥ 3 → “Aprobado”
    2 ≤ nota_final < 3 → “Revisión”
    < 2 → “Reprobado”

Validar que las notas estén en rango."""


print("Empresa Tecno Plus")

tecnica= float(input("Ingrese la NOTA TECNICA nota: "))
logica= float(input("Ingrese la NOTA LOGICA segunda nota: "))
nota_final = (tecnica * 0.7) + (logica * 0.3)


   
if nota_final >= 3 and nota_final <= 5:
        print(f"Aprobado. Tu nota actual es: {nota_final}")
elif nota_final >= 2 and nota_final < 3:
        print(f"Revision. Tu nota actual es: {nota_final}")
elif nota_final < 2:
        print(f"Reprobado. Tu nota actual es: {nota_final}")
else:
        print("nota no validad") 