# Iremos separar os números pares dos ímpares:

numero = int(input("Digite o número "))


resultado = numero % 2

if numero % 2 == 0:
    print("O número é PAR.")
else:
    print("O número é ÍMPAR.")