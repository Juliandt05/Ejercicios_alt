fin=0
while (fin==0):
    nom=str(input("Dime tu usuario "))
    contr=str(input("Dime la contraseña "))

    if (nom=="Pepe"):
        if(contr=="asdasd"):
            print("Has entrado al sistema")
            fin=1
        else:
            print("Error contraseña")
    else:
        print("Error usuario")
    