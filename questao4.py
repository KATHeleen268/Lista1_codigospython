Cod_peca1, num_peca1, valor_unit1 = input().split()
Cod_peca2, num_peca2, valor_unit2 = input().split()

Cod_peca1 = int(Cod_peca1)
num_peca1 = int(num_peca1)
valor_unit1 = float(valor_unit1)

Cod_peca2 = int(Cod_peca2)
num_peca2 = int(num_peca2)
valor_unit2 = float(valor_unit2)

Total = (num_peca1 * valor_unit1) + (num_peca2*valor_unit2)

print(f"VALOR A PAGAR: R$ {Total:.2f}")