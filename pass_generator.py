import time
import random
import string

print("WELCOME TO THE PASSWORD GENERATOR PROGRAM")
tiempo_local = time.ctime()
print(f'The date is {tiempo_local}')
time.sleep(2.5)
imagen_ascii = [
    " ____________________________",
    "!\_________________________/!\"",
    "!!                         !! \"",
    "!!                         !!  \"",
    "!!                         !!  !",
    "!!                         !!  !",
    "!!  Password               !!  !",
    "!!          Generator      !!  !",
    "!!                         !!  !",
    "!!                         !!  /",
    "!!___________________mac___!! /",
    "!/_________________________\!/",
    "   __\_________________/__/!_",
    "  !_______________________!/ )",
    "________________________    (__",
   "/oooo  oooo  oooo  oooo /!   _  )_",
  "/ooooooooooooooooooooooo/ /  (_)_(_)",
 "/ooooooooooooooooooooooo/ /    (o o)",
"/C=_____________________/_/    ==\o/=="
]

##imprimir la imagen línea por línea
for line in imagen_ascii:
    print(line)
    time.sleep(0.1)

password = []
ok = True
while ok:
    n_letras = int(input("Ingrese la cantidad de caracteres de su contraseña: "))
    if n_letras <= 6:
        print("Cantidad de letras debe ser mayor a 6")
    else:
        ok = False
        time.sleep(0.5)
        print("Procesando...")
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=n_letras))

print(f'Tu nueva contraseña es: {password}. Usala con cuidado.')
