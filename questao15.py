salario_habitantes = float(input())
imposto = 0

if salario_habitantes > 4500:
    imposto += (salario_habitantes - 4500) * 0.28
    salario_habitantes = 4500

if salario_habitantes > 3000:
    imposto += (salario_habitantes - 3000) * 0.18
    salario_habitantes = 3000

if salario_habitantes > 2000:
    imposto += (salario_habitantes - 2000) * 0.08

if imposto == 0:
    print("Isento")
else:
    print(f"R$ {imposto:.2f}")