# Random Password Generator in Python

In this project, we'll create a simple random password generator using Python. The generator will make use of the `random`, `time`, and `string` modules to generate secure and unpredictable passwords.

## Prerequisites

Make sure you have Python installed on your machine. You can download Python from the official [Python website](https://www.python.org/downloads/).

## Implementation

Here's the code for our random password generator:

```python
import random
import time
import string

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
