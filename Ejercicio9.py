from operator import truediv
num1=int(input("Dime un número"))
num2=int(input("Dime el siguiente número"))
num3=int(input("Dime el último número"))
lista=[]
lista.append(num1)
lista.append(num2)
lista.append(num3)
lista.sort(reverse=True)
print("El orden de mayor a menor es",lista)