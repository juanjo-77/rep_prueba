libro = 25000
cupones = int(input("eres estudiante?----|1) SI|-----|2) NO|----: "))
LIBRO10 = int(input("tienes otro cupon?----1) SI-----2) NO----: "))

if cupones!= 1 and 2 and LIBRO10 != 1 and 2: 
    print("te ignoro")
    
else:
    total = libro
     
    if cupones == 1:
          total = total * 0.85
          
          if LIBRO10 == 1:
              total = total * 0.90

print(f"total a pagar: {total:}")