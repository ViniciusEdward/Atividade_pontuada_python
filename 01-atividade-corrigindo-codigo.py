# Variáveis para armazenar as estatísticas
import os 
os.system("cls || clear")

quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0
valor = 5
lista_numeros = []

for i in range(valor):
    numero = int(input(f"Digite o {i+1}º número: "))
    soma_geral += numero
    lista_numeros.append(numero)
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero

    else:
        quantidade_impares += 1
        soma_impares += numero

    if numero > 0:
        quantidade_positivos += 1
    else:
        quantidade_negativos += 1

maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)


# Calculando as médias
media_geral = soma_geral / valor
if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
else:
    print("Não tem números pares")


# Imprimindo as estatísticas
os.system("cls || clear")
print("=== Quantidades ===")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de impares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")

print("\n=== Maior e menor ===")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")

print("\n=== Médias ===")
if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
    print(f"Média dos números pares: {media_pares:.2f}")
else:
    print("Não tem média de números pares")

if quantidade_impares > 0:
    media_impares = soma_impares / quantidade_impares
    print(f"Média dos números ímpares: {media_impares:.2f}")
else:
    print("Não tem média de números impares")
    
print(f"Média de todos os números: {media_geral:.2f}")

# Mostrando números na ordem inversa
print("\n=== Inverso ===")
for i,numero in enumerate(reversed(lista_numeros)):
    print(f"{len(lista_numeros)-i}º - {numero}")