Num_Par = 0
Num_Impar = 0
Num_Positivo = 0
Num_Negativo = 0

for _ in range(5):  # Executa o loop 5 vezes
    valor = int(input())  # Lê um valor inteiro

    if valor % 2 == 0:
        Num_Par += 1
    else:
        Num_Impar += 1

    if valor > 0:
        Num_Positivo += 1
    elif valor < 0:
        Num_Negativo += 1

print(f"{Num_Par} valor(es) par(es)")
print(f"{Num_Impar} valor(es) impar(es)")
print(f"{Num_Positivo} valor(es) positivo(s)")
print(f"{Num_Negativo} valor(es) negativo(s)")