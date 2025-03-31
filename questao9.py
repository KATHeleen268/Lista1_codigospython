notas = []
pesos = [2, 3, 4, 1]
i = 0

for i in range (4):
    nota = float(input())
    notas.append(nota)

media = sum(notas[i]*pesos[i] for i in range(4)) /10.0
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    nota_exame = float(input())
    media_exame = (media + nota_exame)/2
    
    if media_exame >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado")
    print(f"Media final: {media_exame:.1f}")
else:
    print("Aluno reprovado")

