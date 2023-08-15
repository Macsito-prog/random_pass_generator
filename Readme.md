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

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    if password_length < 6:
        print("Password length must be at least 6 characters.")
    else:
        random.seed(time.time())
        password = generate_password(password_length)
        print("Generated Password:", password)
