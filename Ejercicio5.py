from pathlib import PureWindowsPath


usuSec="Pepe"
passSec="asdasd"

usu = input("Dime tu ususario: ")
password = input("Dime tu contraseña: ")

while (usuSec!=usu or passSec!=password):
    if (usuSecreto!=usuario):#¿Porque sale error?#
        print("Error en el usuario")
        usu = input("Dime tu ususario: ")
    elif (passSec!=password):
        print("Error en el password")
        password = input("Dime tu password: ")
    