nota=int(input("Dime tu nota "))
edad=int(input("Dime etu edad "))
sexo=str(input("Dime tu género M o F "))

if nota>=5 and edad>=18 and sexo=="F":
    print("Aceptada")
elif nota>=5 and edad>=18 and sexo=="M":
    print("Posible")
else:
    print("No aceptada")


