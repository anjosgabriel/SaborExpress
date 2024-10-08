#Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

import os

os.system('cls')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Variável para armazenar a soma dos números ímpares
soma_impares = 0

for numero in numeros:
    if numero % 2 != 0:  # Verifica se o número é ímpar
        soma_impares += numero

print("A soma dos números ímpares de 1 a 10 é:", soma_impares)
