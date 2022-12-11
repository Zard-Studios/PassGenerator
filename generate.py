import random

# stringa di caratteri da cui selezionare la password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-="

# lunghezza della password desiderata
print("Lunghezza password? (indicare con un numero naturale)")
password_length = input()

# genera una password selezionando casualmente caratteri dalla stringa `chars`
password = "".join(random.choices(chars, k=password_length))

# stampa la password da generare
print(password)
