
 
from curses.ascii import isupper
from lzma import is_check_supported


letra=str(input("Ingrese una letra "))
 
if letra.isupper() == True:
    print ("La letra es mayuscula")
else:
    print ("La letra es minúscula")
