base=int(input("Dime la base de la potencia "))
exp=int(input("Dime el exponente de la potencia "))
res=base

if(exp>0):
    while (exp>=1):
        res=res*base
        exp=exp-1
    print("El resultado de la potencia es",res)
elif(exp==0):
    print("El resultado es 1")
else:
    while (exp>=1):
        res=res*base
        exp=exp+1
    print("El resultado de la potencia es",1/res)
